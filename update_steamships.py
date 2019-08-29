from database import get_containers_by_steamship, update_container_eta, update_container_tracing

import apl

apl = apl.APL()

tracing_results_list = []
container_list = get_containers_by_steamship()['APLU'] + get_containers_by_steamship()['CMDU']

for container in container_list:
    apl.get_tracing_results_dict(container, tracing_results_list)

for result in tracing_results_list:
    formatted_tracing_results = apl.format_tracing_results(result)
    update_container_eta(result['container'], result['vessel_eta'])
    update_container_tracing(result['container'], formatted_tracing_results, 'ssl')
