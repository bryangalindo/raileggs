from datetime import datetime

import requests
from bs4 import BeautifulSoup
import lxml


class CanadianRail:
    def __init__(self, scrape_url, containers_list):
        self.scrape_url = scrape_url
        self.containers_list = containers_list

    def __format_containers_list(self):
        return ''.join([container[:-1] for container in self.containers_list])

    def __get_html_dict(self):
        formatted_containers_list = self.__format_containers_list()
        location_response = requests.get(self.scrape_url.format('HL', formatted_containers_list))
        eta_response = requests.get(self.scrape_url.format('HH', formatted_containers_list))
        location_html = BeautifulSoup(location_response.content, 'lxml')
        eta_html = BeautifulSoup(eta_response.content, 'lxml')
        return dict(location_html=location_html, eta_html=eta_html)

    def extract_containers_from_html(self):
        containers_html_dict = self.__get_html_dict()
        extracted_containers_dict = {'location_html': [], 'eta_html': []}
        for k, v in containers_html_dict.items():
            extracted_containers_dict[k] = v.text.split('\n')[5:5 + len(self.containers_list)]
        return extracted_containers_dict

    def get_load_status(self, index, _dict):
        load_status_key = _dict['location_html'][index].split()[6]
        return load_status_dict[load_status_key]

    def get_current_event(self, index, _dict):
        now = datetime.now()
        rail_status_key = _dict['location_html'][index].split()[7]
        event_datetime_str = self.remove_at(4, (''.join(_dict['location_html'][index].split()[4:6])))
        raw_event_datetime = datetime.strptime(event_datetime_str, '%m%d%H%M')
        event_datetime = datetime.strftime(raw_event_datetime, '%m/%d/{} %H:%M'.format(now.year))
        return dict(most_recent_event=cn_rail_events_dict[rail_status_key], datetime=event_datetime)

    def get_current_location(self, index, _dict):
        location_list = _dict['location_html'][index].split()[2:4]
        current_location = ', '.join(location_list)
        return dict(current_location=current_location)

    def get_next_destination(self, index, _dict):
        location_list = _dict['location_html'][index].split()[9:11]
        destination = ', '.join(location_list)
        return dict(destination=destination)

    def get_final_eta(self, index, _dict):
        try:
            now = datetime.now()
            final_eta_str = _dict['eta_html'][index].split()[-1]
            final_eta_datetime = datetime.strptime(final_eta_str[:4], '%m%d')
            final_eta = datetime.strftime(final_eta_datetime, '%m/%d/{}'.format(now.year))
            return dict(final_eta=final_eta)
        except ValueError:  # catches strptime trying to turn letters into datetime object
            pass

    def remove_at(self, index, s):
        return s[:index] + s[index + 1:]


cn_rail_events_dict = {
    'A': 'Arrived at location',
    'B': 'Bad order (needs repair)',
    'C': 'Came in the gate of an intermodal terminal',
    'D': 'Arrived at final destination yard or terminal',
    'E': 'Exit the gate of an intermodal terminal',
    'F': 'Flat Car has been reported in bad order (needs repair)',
    'G': 'Released from bad order (repair) and returned to service',
    'H': 'Hold status',
    'J': 'Junction delivery (interchange to another railroad)',
    'K': 'Intermodal Interchange',
    'L': 'Loaded',
    'M': 'Motor carrier move',
    'P': 'Passed a station on a train (departure)',
    'Q': 'Flat Car released from bad order (repair)',
    'R': 'Received at junction interchange from another railroad',
    'S': 'Stored',
    'U': 'Ramped, intermodal unit loaded onto a flatcar',
    'V': 'Deramped, intermodal unit removed from a flatcar',
    'W': 'Release by shipper (OK to move)',
    'X': 'Departed shipper, pickup or pull',
    'Y': 'Notification or constructive placement',
    'Z': 'Placement or delivery to consignee ',
}
#
load_status_dict = {
    'L': 'Loaded',
    'E': 'Empty'
}

scrape_url = 'https://automate.cn.ca/ecomsrvc/velocity/Tracing/english/TracingDirect_DirectAccess?&Function=STI&UserID=CENTRANSCN&Password=CENTRANSCN&Format={}&EquipmentID={}'
containers_list = ['CEOU2018957', 'HLXU6217417', 'DRYU9110697', 'TRLU6915028']

cn = CanadianRail(scrape_url, containers_list)

container_html = cn.extract_containers_from_html()
for i, container in enumerate(container_html):
    print(
        '{}: {} {} {} {} {}'.format(
            containers_list[i],
            cn.get_load_status(i, container_html),
            cn.get_current_location(i, container_html),
            cn.get_current_event(i, container_html),
            cn.get_next_destination(i, container_html),
            cn.get_final_eta(i, container_html),
        )
    )

