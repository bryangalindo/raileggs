import requests
from bs4 import BeautifulSoup

from constants import bnsf_data, bnsf_containers_list, bnsf_post_url


class BNSF:
    def __init__(self, containers_list):
        self.containers_list = containers_list

    def format_containers_list(self):
        return ','.join([container[:-1] for container in self.containers_list])

    def get_tags_list(self):
        bnsf_data['equipment'] = self.format_containers_list()
        response = requests.post(url=bnsf_post_url, data=bnsf_data)
        html = BeautifulSoup(response.content, 'lxml')
        return html.find_all('tr', {'id': 'dllRowStyle'})

    def get_logistics_dict(self, html):
        container_number = '{}{}'.format((html.find('td', {'id': 'UnitInit'})).text,
                                         (html.find('td', {'id': 'UnitNumber'})).text)
        rail_bill_status = (html.find('td', {'id': 'BillYN'})).text
        last_free_day = (html.find('td', {'id': 'LastFreeDay'})).text
        final_destination_eta = (html.find('td', {'id': 'EstDRMPDate'})).text
        return dict(
            container_number=container_number, rail_bill_status=rail_bill_status,
            last_free_day=last_free_day, final_destination_eta=final_destination_eta,
        )

    def get_containers_logistics(self):
        html_tag_list = self.get_tags_list()
        containers_logistics_list = []
        for tag in html_tag_list:
            containers_logistics_list.append(self.get_logistics_dict(tag))

        return containers_logistics_list
