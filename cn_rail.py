from datetime import datetime
import re

import requests
from bs4 import BeautifulSoup

from constants import load_status_dict, cn_rail_events_dict


class CanadianRail:
    def __init__(self, scrape_url, containers_list):
        self.scrape_url = scrape_url
        self.containers_list = containers_list

    def __format_containers_list(self):
        return ''.join([container[:-1] for container in self.containers_list])

    def __extract_eta(self, eta_str, starting_index):
        now = datetime.now()
        last_index = starting_index + 4
        final_eta_datetime = datetime.strptime(eta_str[starting_index:last_index], '%m%d')
        return datetime.strftime(final_eta_datetime, '%m/%d/{}'.format(now.year))

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

    def get_recent_event(self, index, _dict):
        now = datetime.now()
        rail_status_key = _dict['location_html'][index].split()[7]
        event_datetime_str = self.remove_at(4, (''.join(_dict['location_html'][index].split()[4:6])))
        raw_event_datetime = datetime.strptime(event_datetime_str, '%m%d%H%M')
        event_datetime = datetime.strftime(raw_event_datetime, '%m/%d/{} %H:%M'.format(now.year))
        return dict(most_recent_event=cn_rail_events_dict[rail_status_key], datetime=event_datetime)

    def get_recent_location(self, index, _dict):
        location_list = _dict['location_html'][index].split()[2:4]
        current_location = ', '.join(location_list)
        return dict(most_recent_location=current_location)

    def get_next_destination(self, index, _dict):
        location_list = _dict['location_html'][index].split()[9:11]
        destination = ', '.join(location_list)
        return dict(destination=destination)

    def get_final_eta(self, index, _dict):
        global final_eta
        tracing_result_list = _dict['eta_html'][index].split()
        first_int_index = re.search("\d", tracing_result_list[-1])
        if first_int_index and tracing_result_list[-1].isdigit():
            final_eta = self.__extract_eta(tracing_result_list[-1], first_int_index.start())
        elif not first_int_index:
            final_eta = '12/31/2019'
        elif first_int_index and not tracing_result_list[-1].isdigit():
            pass
        else:
            first_int_index = re.search("\d", tracing_result_list[-2])
            final_eta = self.__extract_eta(tracing_result_list[-2], first_int_index.start())

        return dict(final_eta=final_eta)

    def remove_at(self, index, s):
        return s[:index] + s[index + 1:]

    def get_all_tracing_results(self, index, _dict):
        return {
            self.get_recent_location(index, _dict),
            self.get_next_destination(index, _dict),
            self.get_final_eta(index, _dict),
            self.get_recent_event(index, _dict),
        }
