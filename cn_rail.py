from datetime import datetime

import requests
from bs4 import BeautifulSoup

from constants import load_status_dict, cn_rail_events_dict


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
