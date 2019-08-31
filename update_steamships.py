import multiprocessing

import requests

import apl
import hpl
import msc
from database import get_containers_by_steamship, update_container_eta, update_container_tracing

session = requests.Session()

apl = apl.APL(session)
tracing_results_list = []
apl_containers_list = get_containers_by_steamship()['APLU'] + get_containers_by_steamship()['CMDU']

pool = multiprocessing.Pool(processes=len(apl_containers_list))
with pool as p:
    tracing_results = p.map(apl.get_tracing_results_dict, apl_containers_list)
    for result in tracing_results:
        tracing_results_list.append(result)

for result in tracing_results_list:
    formatted_tracing_results = apl.format_tracing_results(result)
    update_container_eta(result['container'], result['vessel_eta'])
    update_container_tracing(result['container'], formatted_tracing_results, 'ssl')


msc = msc.MSC(session)
msc_containers_list = get_containers_by_steamship()['MEDU']

for container in msc_containers_list:
    html = msc.get_tracing_results_html(container)
    update_container_tracing(container, msc.get_all_events(html), 'ssl')
    update_container_eta(container, msc.get_vessel_eta(html))

hpl = hpl.HPL(session)
hapag_containers_list = get_containers_by_steamship()['HLCU']

for container in hapag_containers_list:
    try:
        html = hpl.get_tracing_results_html(container)
        update_container_tracing(container, hpl.get_all_events(html), 'ssl')
        update_container_eta(container, hpl.get_vessel_eta(html))
    except AttributeError:
        pass