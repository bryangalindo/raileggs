from constants import bnsf_data, bnsf_scrape_url
import requests
from bs4 import BeautifulSoup


class BNSF:
    def __init__(self, containers_list):
        self.containers_list = containers_list

    def format_containers(self):
        formatted_containers_list = []
        for container in self.containers_list:
            if '0' in container[4]:
                formatted_container_str = container[:4] + container[5:-1]
                formatted_containers_list.append(formatted_container_str)
            else:
                formatted_containers_list.append(container[:-1])
        return formatted_containers_list

    def get_tracing_results_html(self):
        formatted_containers_list = self.format_containers()
        bnsf_data['equipment'] = ','.join(formatted_containers_list)
        response = requests.post(bnsf_scrape_url, data=bnsf_data)
        html = BeautifulSoup(response.content, 'html.parser')
        container_tags = html.find_all('tr', {'id': 'dllRowStyle'})
        return container_tags

    def get_tracing_results_dict(self):
        tracing_results_list = []
        container_tags = self.get_tracing_results_html()
        for tag in container_tags:
            tracing_results_list.append(dict(
                container_number='{}{}'.format((tag.find('td', {'id': 'UnitInit'})).text,
                                               (tag.find('td', {'id': 'UnitNumber'})).text),
                last_location=(tag.find('td', {'id': 'LastHub'})).text,
                final_destination=(tag.find('td', {'id': 'DestHub'})).text,
                last_free_day=(tag.find('td', {'id': 'LastFreeDay'})).text,
                eta='{} {}'.format((tag.find('td', {'id': 'EstDRMPDate'})).text,
                                   (tag.find('td', {'id': 'EstDRMPTime'})).text),
                rail_billed=(tag.find('td', {'id': 'BillYN'})).text,
            )
            )

        return tracing_results_list
