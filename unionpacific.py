import base64
from datetime import datetime, timedelta

import requests

from constants import uprr_request_token_url, uprr_scrape_url, uprr_data_dict, uprr_headers_dict


class UnionPacific:

    def __get_request_token(self):
        response = requests.post(uprr_request_token_url, headers=uprr_headers_dict, data=uprr_data_dict)
        token_dict = response.json()
        return token_dict['access_token']

    def get_tracking_dict(self, container_list):
        request_token = self.__get_request_token()
        headers = {'Authorization': 'Bearer {}'.format(request_token)}

        response = requests.get(uprr_scrape_url.format(','.join(container_list)), headers=headers)
        response_list = response.json()
        traced_containers_list = []
        for container in response_list:
            traced_containers_list.append({
                    'fields': {
                        'storage_details': container['storageCharges'],
                        'scheduled_events': container['scheduledEvents'],
                        'accomplished_events': container['accomplishedEvents'],
                        'billed_status': container['billedStatus'],
                    }
                }
            )
        traced_containers_dict = dict(zip(container_list, traced_containers_list))
        return traced_containers_dict

    def get_last_free_day(self, _dict):
        storage_charge_date_str = _dict['fields']['storage_details']['storageChargeBegins'].split('T')[0]
        storage_charge_datetime = datetime.strptime(storage_charge_date_str, '%Y-%m-%d')
        last_free_date = storage_charge_datetime - timedelta(days=1)
        return str(datetime.strftime(last_free_date, '20%y-%m-%d'))

    def get_outgate_date(self, _dict):
        if 'Delivered to Truck Line' in _dict['fields']['accomplished_events'][0]['name']:
            outgate_date_str = _dict['fields']['accomplished_events'][0]['dateTime'].split('T')[0]
            outgate_date_object = datetime.strptime(outgate_date_str, '%Y-%m-%d')
            return datetime.strftime(outgate_date_object, '%m/%d/%y')

    def check_container_validity(self, container_num, _dict):
        if _dict['fields']['storage_details'] is None:
            print('{} not on BNSF, check other rails.'.format(container_num))
        else:
            print('{} is in BNSF inventory'.format(container_num))

    def get_container_eta(self, _dict):
        arrival_eta_str = _dict['fields']['scheduled_events'][0]['dateTime'].split('T')[0]
        arrival_eta_datetime = datetime.strptime(arrival_eta_str, '%Y-%m-%d')
        return datetime.strftime(arrival_eta_datetime, '%Y-%m-%d')


def get_uprr_event(_dict, event):
    event_dict = {
        'past': 'accomplished_events',
        'scheduled': 'scheduled_events',
    }
    try:
        return '{}, {}\t{} {}'.format(
            _dict['fields'][event_dict[event]][0]['location']['city'],
            _dict['fields'][event_dict[event]][0]['location']['state'],
            _dict['fields'][event_dict[event]][0]['name'],
            _dict['fields'][event_dict[event]][0]['dateTime'])
    except (IndexError, KeyError):
        pass
