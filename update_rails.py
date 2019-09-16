import contextlib

import bnsf
import cn_rail as cn
import cp_rail as cp
from constants import cn_scrape_url
import database as db
import unionpacific as uprr
from utilities import has_digits, start_headless_driver


'''
BNSF RAIL TRACING
'''
bnsf_container_list = db.get_containers_by_rail()['BNSF']
if bnsf_container_list:
    bnsf_container_list.sort()
    bnsf = bnsf.BNSF(bnsf_container_list)
    bnsf_tracing_results_list = bnsf.get_tracing_results_dict()

    for i, container in enumerate(bnsf_tracing_results_list):
        tracing_result = bnsf.get_formatted_tracing_results(container)
        db.update_container_tracing(bnsf_container_list[i], tracing_result, 'rail')
        db.update_container_eta(bnsf_container_list[i], container['eta'])

        if has_digits(container['last_free_day']):  # bnsf returns N/A before posting LFD
            db.update_container_lfd(bnsf_container_list[i], container['last_free_day'])

'''
CN RAIL TRACING
'''
cn_container_list = db.get_containers_by_rail()['CN']

if cn_container_list:
    cn = cn.CanadianRail(cn_scrape_url, cn_container_list)
    container_html = cn.extract_containers_from_html()

    for i, item in enumerate(container_html['eta_html']):
        if 'NO RECORD' not in item:
            most_recent_location = cn.get_recent_location(i, container_html)['most_recent_location']
            destination = cn.get_next_destination(i, container_html)['destination']
            recent_event_dict = cn.get_recent_event(i, container_html)
            most_recent_event = recent_event_dict['most_recent_event']
            try:
                final_eta = cn.get_final_eta(i, container_html)['final_eta']
            except NameError:
                final_eta = recent_event_dict['datetime'].split()[0]

            tracing_results = 'Last location: {}\nLast event: {} {}\nFinal destination: {} ETA: {}\nLast Check On: {}'.format(
                most_recent_location,
                recent_event_dict['most_recent_event'], recent_event_dict['datetime'],
                destination, final_eta,
                datetime.now()
            )

            db.update_container_tracing(cn_container_list[i], tracing_results, 'rail')
            last_free_day = cn.get_last_free_day(most_recent_event)

            if last_free_day:
                db.update_container_lfd(cn_container_list[i], last_free_day)
            else:
                db.update_container_eta(cn_container_list[i], final_eta)
        elif 'NO RECORD' in item:
            tracing_result = 'Pending Rail\nLast Checked On: {}'.format(datetime.now())
            final_eta = '12/31/2019'
            db.update_container_tracing(cn_container_list[i], tracing_result, 'rail')
            db.update_container_eta(cn_container_list[i], final_eta)
            
'''
NORTHFOLK SOUTHERN
'''
ns_containers_list = db.get_containers_by_rail()['NORTHFOLK SOUTHERN']
if ns_containers_list:
    with requests.session() as s:
        for i, container in enumerate(ns_containers_list):
            ns = ns.NorfolkSouthern(s)
            tracing_results_dict = ns.get_tracing_results_dict(ns_containers_list[i], s)
            eta = ns.get_eta(tracing_results_dict, i).split()[0]
            last_free_day = ns.get_last_free_day(tracing_results_dict, i)
            most_recent_event = ns.get_most_recent_event(tracing_results_dict, i)
            scheduled_event = ns.get_scheduled_event(tracing_results_dict, i)
            tracing_result = ns.get_formatted_tracing_results(most_recent_event, scheduled_event)

            if eta:
                db.update_container_eta(container, eta, 'rail')
            if last_free_day:
                db.update_container_lfd(container, last_free_day)
            else:
                db.update_container_tracing(container, tracing_result, 'rail')

'''
CSX RAIL
'''                           
csx = csx.CSX()
csx_containers_dict = csx.get_containers_dict()
if csx_containers_dict:
    tracing_results_list = csx.get_tracing_results_list()

    for result in tracing_results_list:
        container_key = result['equipment']['equipmentID']['equipmentInitial'] + \
                        result['equipment']['equipmentID']['equipmentNumber']
        container = csx_containers_dict[container_key]
        try:
            if result['tripPlan']:
                try:
                    eta = result['tripPlan']['updatedEtn'].split('T')[0]
                except KeyError:
                    eta = result['tripPlan']['originalEtn'].split('T')[0]
                db.update_container_eta(container, eta, 'rail')
        except KeyError:
            db.update_container_eta(container, '12/31/2019', 'rail')

        if 'NOTIFIED' in result['shipmentStatus']:
            last_free_day = result['premise']['paidThruDate']
            db.update_container_lfd(container, last_free_day)

'''
UP RAIL TRACING
'''
up_container_list = db.get_containers_by_rail()['UP']

if up_container_list:
    up = uprr.UnionPacific()
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

'''
CP RAIL TRACKING
'''
cp_containers_list = db.get_containers_by_rail()['CP']

if cp_containers_list:
    driver = start_headless_driver()
    cp = cp.CanadianPacific(driver, cp_containers_list)

    with contextlib.closing(driver) as driver:
        tracing_results_list = cp.get_tracing_results_list()
        
        for result in tracing_results_list:
            tracing_result = cp.get_formatted_tracing_results(result)
            eta = result['final_destination_eta']

            if result['last_free_day']:
                db.update_container_lfd(result['container_number'], result['last_free_day'])
            if eta:
                db.update_container_eta(result['container_number'], eta)
                db.update_container_tracing(result['container_number'], tracing_result, 'rail')
            else:
                db.update_container_eta(result['container_number'], '12/31/2019')
                db.update_container_tracing(result['container_number'], result['current_status'], 'rail')
