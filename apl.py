from datetime import datetime
from collections import defaultdict
import itertools

import requests
from bs4 import BeautifulSoup

from database import airtable_containers_sheet


def get_containers_by_steamship():
    containers_by_steamship_dict = defaultdict(list)
    airtable_records = airtable_containers_sheet.get_all(
        fields=['Container', 'MBL'],
        view='Pending ANs'
    )

    for record in airtable_records:
        hi = containers_by_steamship_dict[record['fields']['MBL'][0]]

    for k, v in containers_by_steamship_dict.items():
        containers_by_steamship_dict[k] = list(itertools.chain.from_iterable(v)) # combines lists from values of dict key

    return containers_by_steamship_dict

scrape_url = 'https://www.apl.com/ebusiness/tracking/search?SearchBy=Container&Reference={}&search=Search'
container_list= ['CNIU1150508', 'TRHU3865199']

def get_tracing_results_html(container):
    r = requests.get(scrape_url.format(container))
    html = BeautifulSoup(r.content, 'lxml')
    return html.find('tbody')

def get_vessel_eta(html_table):
    tracing_results_table_rows = html_table.find_all('tr')
    for row in tracing_results_table_rows:
        tracing_results_columns = row.find_all('td')
        event_description = tracing_results_columns[2].text.strip()
        event_datetime_str = ' '.join(tracing_results_columns[0].text.split()[1:4])
        if 'Arrival final port of discharge' in event_description:
            vessel_eta_datetime = datetime.strptime(event_datetime_str, '%d %b %Y')
            vessel_eta = datetime.strftime(vessel_eta_datetime, '%m/%d/%Y')
            return vessel_eta

def get_most_recent_event(html_table):
    current_container_status = [text.strip() for text in (html_table.find('tr', {'class': "is-current is-open"})).text.split('\r')]
    return dict(datetime=current_container_status[1], event_description=current_container_status[3],
                location=current_container_status[5],)

def get_scheduled_events(html_table):
    tracing_results_table_rows = html_table.find_all('tr')
    scheduled_events_list = []

    for row in tracing_results_table_rows:
        if not (row.find('td', {'class': "is-icon"})).text:
            tracing_results_columns = row.find_all('td')
            row_update_list = [column.text.strip() for column in tracing_results_columns]
            scheduled_events_list.append(
                dict(
                    datetime=row_update_list[0],
                    event_description=row_update_list[2],
                    location=row_update_list[3],
                )
            )

    return scheduled_events_list

tracing_results_list = []

for container in container_list:
    tracing_results_table = get_tracing_results_html(container)
    most_recent_event_dict = get_most_recent_event(tracing_results_table)
    scheduled_events = get_scheduled_events(tracing_results_table)
    vessel_eta = get_vessel_eta(tracing_results_table)
    tracing_results_list.append(
        dict(
            container=container,
            vessel_eta=vessel_eta,
            most_recent_event=most_recent_event_dict,
            scheduled_events=scheduled_events
        )
    )

for result in tracing_results_list:
    print(result)
