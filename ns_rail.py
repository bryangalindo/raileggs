from ns_event_codes import event_codes
from constants import headers, ns_login_dict, ns_login_url, ns_tracing_url
from datetime import datetime


class NorfolkSouthern:
    def __init__(self, session):
        self.session = session

    def login(self):
        self.session.headers.update(headers)
        self.session.headers.update({'Content-Type': 'application/json'})
        return self.session.post(ns_login_url, json=ns_login_dict)

    def get_token(self):
        login_response = self.login()
        login_results_dict = login_response.json()
        return login_results_dict['result']['token']

    def get_tracing_results_dict(self, container, session):
        token = self.get_token()
        self.session.headers.update({'CSRFTOKEN': token})
        search_response = session.post(ns_tracing_url, json={"searchList": container})
        return search_response.json()

    def get_most_recent_event(self, _dict, index):
        event_code_key = _dict['result']['validEquipmentDataList'][index]['lastAAREventCode']
        event_description = event_codes[event_code_key]
        location = _dict['result']['validEquipmentDataList'][index]['currentTerminalLocation']
        event_date_time = _dict['result']['validEquipmentDataList'][index]['eventTime']
        return '{} {} {}'.format(event_description, location, event_date_time)

    def get_eta(self, _dict, index):
        return _dict['result']['validEquipmentDataList'][index]['etg']

    def get_last_free_day(self, _dict, index):
        return _dict['result']['validEquipmentDataList'][index]['lastFreeDateTime']

    def get_scheduled_event(self, _dict, index):
        eta = self.get_eta(_dict, index)
        location = _dict['result']['validEquipmentDataList'][index]['onlineDestination']
        return 'On route to {} ETA: {}'.format(location, eta)

    def get_formatted_tracing_results(self, recent_event, scheduled_event):
        return 'Most Recent Event: {}\nScheduled Event: {}\nLast Checked On: {}'.format(
            recent_event,
            scheduled_event,
            datetime.now(),
        )
