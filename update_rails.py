import bnsf
import cn_rail as cn
from constants import cn_scrape_url
import database as db
import unionpacific as uprr
from utilities import has_digits

'''
BNSF RAIL TRACING
'''
bnsf_container_list = db.get_containers_by_rail()['BNSF']
bnsf_container_list.sort()
bnsf = bnsf.BNSF(bnsf_container_list)
bnsf_tracing_results_list = bnsf.get_tracing_results_dict()

for i, container in enumerate(bnsf_tracing_results_list):
    tracing_template = 'Last location: {}\nFinal destination: {} {}'
    tracing_results = tracing_template.format(container['last_location'],
                                              container['final_destination'],
                                              container['eta'],
                                              )

    db.update_container_tracing(bnsf_container_list[i], tracing_results, 'rail')

    try:
        db.update_container_eta(bnsf_container_list[i], container['eta'].split()[0])
    except IndexError:
        pass

    if has_digits(container['last_free_day']):  # bnsf returns N/A before posting LFD
        db.update_container_lfd(bnsf_container_list[i], container['last_free_day'])

'''
CN RAIL TRACING
'''
# cn_container_list = db.get_containers_by_rail()['CN']
cn_container_list = ['OOLU9974071']
cn = cn.CanadianRail(cn_scrape_url, cn_container_list)
container_html = cn.extract_containers_from_html()

for i, item in enumerate(container_html['eta_html']):
    most_recent_location = cn.get_recent_location(i, container_html)['most_recent_location']
    destination = cn.get_next_destination(i, container_html)['destination']
    recent_event_dict = cn.get_recent_event(i, container_html)
    most_recent_event = recent_event_dict['most_recent_event']
    try:
        final_eta = cn.get_final_eta(i, container_html)['final_eta']
    except NameError:
        final_eta = recent_event_dict['datetime'].split()[0]

    tracing_results = 'Last location: {}\nLast event: {} {}\nFinal destination: {} ETA: {}'.format(
        most_recent_location,
        recent_event_dict['most_recent_event'], recent_event_dict['datetime'],
        destination, final_eta,
    )

    db.update_container_tracing(cn_container_list[i], tracing_results, 'rail')
    last_free_day = cn.get_last_free_day(most_recent_event)

    if last_free_day:
        db.update_container_lfd(cn_container_list[i], last_free_day)
    else:
        db.update_container_eta(cn_container_list[i], final_eta)

'''
UP RAIL TRACING
'''
up = uprr.UnionPacific()
up_container_list = db.get_containers_by_rail()['UP']
uprr_tracing_results_dict = up.get_tracking_dict(up_container_list)
updated_containers_list = []

for k, v in uprr_tracing_results_dict.items():
    scheduled_event = uprr.get_uprr_event(v, 'scheduled')
    past_event = uprr.get_uprr_event(v, 'past')
    billed_status = v['fields']['billed_status']

    if 'Pending' in billed_status:
        db.update_container_eta(k, '2019-12-31')
        db.update_container_tracing(k, 'Pending Rail')
    else:
        try:
            if 'Van Notification' in past_event:
                last_free_day = up.get_last_free_day(v)
                db.update_container_lfd(k, last_free_day)
        except TypeError:
            pass

        eta_keywords = ['Estimated', 'Arrival', 'Scheduled']
        try:
            if any(keyword in scheduled_event for keyword in eta_keywords):
                container_eta = up.get_container_eta(v)
                db.update_container_eta(k, container_eta)
        except TypeError:
            pass

        tracing_results = '{}\n{}\n\n'.format(past_event, scheduled_event)
        db.update_container_tracing(k, tracing_results, 'rail')
        updated_containers_list.append(k)

print('{} have been updated'.format(' '.join(updated_containers_list)))
