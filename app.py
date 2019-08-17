import unionpacific as uprr
import bnsf
import database as db

# bnsf = bnsf.BNSF()
# bnsf_container_list = db.get_containers_by_rail()['BNSF']
# bnsf_tracing_results_dict = bnsf.get_tracing_results_dict(bnsf_container_list)

print('hello')

up = uprr.UnionPacific()
up_container_list = db.get_containers_by_rail()['UP']
uprr_tracing_results_dict = up.get_tracking_dict(up_container_list)
updated_containers_list = []

for k, v in uprr_tracing_results_dict.items():
    scheduled_event = uprr.get_scheduled_event(v)
    past_event = uprr.get_past_event(v)
    try:
        if 'Van Notification' in past_event:
            last_free_day = up.get_last_free_day(v)
            db.update_container_lfd(k, last_free_day)
    except TypeError:
        pass
    eta_keywords = ['Estimated', 'Arrival']
    try:
        if any(keyword in scheduled_event for keyword in eta_keywords):
            container_eta = up.get_container_eta(v)
            db.update_container_eta(k, container_eta)
    except TypeError:
        pass
    tracing_results = '{}\n{}\n\n'.format(past_event, scheduled_event)
    db.update_container_tracing(k, tracing_results)
    updated_containers_list.append(k)


print('{} have been updated'.format(' '.join(updated_containers_list)))
