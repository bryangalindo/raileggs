from collections import defaultdict
import itertools

from airtable import Airtable

from constants import BASE_KEY, SHEET, API_KEY

airtable_tracking_sheet = Airtable(BASE_KEY, SHEET, API_KEY)
airtable_containers_sheet = Airtable(BASE_KEY, 'Containers', API_KEY)


def get_containers_by_rail():
    containers_by_rail_dict = defaultdict(list)
    airtable_records = airtable_tracking_sheet.get_all(
        fields=['CI Reference', 'Container List', 'Container Yard'],
        view='Inland Moves'
    )

    for record in airtable_records:
        container_list = record['fields']['Container List'].split(', ')
        containers_by_rail_dict[record['fields']['Container Yard']].append(container_list)

    for k, v in containers_by_rail_dict.items():
        containers_by_rail_dict[k] = list(itertools.chain.from_iterable(v)) # combines lists from values of dict key

    return containers_by_rail_dict


def update_container_tracing(container_number, tracing_results):
    record = airtable_containers_sheet.search('Container', container_number)
    fields = {'Tracing': tracing_results}
    airtable_containers_sheet.update(record[0]['id'], fields)


def update_container_lfd(container_number, lfd):
    record = airtable_containers_sheet.search('Container', container_number)
    fields = {'LFD': lfd}
    airtable_containers_sheet.update(record[0]['id'], fields)


def update_container_eta(container_number, eta):
    record = airtable_containers_sheet.search('Container', container_number)
    fields = {'ETA': eta}
    airtable_containers_sheet.update(record[0]['id'], fields)


