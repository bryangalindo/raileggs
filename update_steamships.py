import multiprocessing
import time
import contextlib

import requests
import selenium.webdriver as webdriver

import apl
from constants import driver_path, hapag_url
import cosco
from database import get_containers_by_steamship, update_container_eta, update_container_tracing
import hpl
import msc
import one_line


session = requests.Session()

'''
APL TRACKING
'''
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

'''
MSC TRACKING
'''
msc = msc.MSC(session)
msc_containers_list = get_containers_by_steamship()['MEDU']

for container in msc_containers_list:
    try:
        html = msc.get_tracing_results_html(container)
        update_container_tracing(container, msc.get_all_events(html), 'ssl')
        update_container_eta(container, msc.get_vessel_eta(html))
    except AttributeError:
        pass

'''
HAPAG TRACKING
'''
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)

with contextlib.closing(driver) as driver:
    hpl = hpl.HPL(driver)
    hpl_containers_list = get_containers_by_steamship()['HLCU']

    for container in hpl_containers_list:
        events_dict = hpl.get_all_events_dict(hapag_url, container)
        tracing_results = hpl.get_formatted_tracing_results(events_dict)
        vessel_eta = hpl.get_vessel_eta(events_dict['scheduled_events'])
        update_container_tracing(container, tracing_results, 'ssl')
        update_container_eta(container, vessel_eta)

'''
COSCO TRACKING
'''
timestamp = int(time.time())
cosco_containers_list = get_containers_by_steamship()['COSU']

cosco = cosco.COSCO(containers_list=cosco_containers_list, session=session, timestamp=timestamp)
cosco_containers_list = get_containers_by_steamship()['COSU']

most_recent_events_list = cosco.get_most_recent_event_list()

for event in most_recent_events_list:
    container_number = event['container_number']
    vessel_eta = cosco.get_vessel_eta(container_number)
    update_container_eta(container_number, vessel_eta)
    update_container_tracing(container_number, cosco.format_most_recent_event(event), 'ssl')

'''
ONE LINE TRACKING
'''
one = one_line.ONE(session)
one_containers_list = get_containers_by_steamship()['ONEY']

for container in one_containers_list:
    events_dict = one.get_events_dict(container)
    tracing_results = one.get_formatted_events(events_dict)
    vessel_eta = one.get_vessel_eta(container)
    update_container_eta(container, vessel_eta)
    update_container_tracing(container, tracing_results, 'ssl')
