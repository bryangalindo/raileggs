from constants import form_data_payload, vessel_eta_payload, events_payload, one_line_url



class ONE:
    def __init__(self, session):
        self.session = session

    def __get_form_data(self, container):
        form_data_payload['cntr_no'] = container
        r = self.session.post(url=one_line_url, data=form_data_payload, verify=False)
        response_dict = r.json()
        return dict(cop_number=response_dict['list'][0]['copNo'],
                    short_mbl=response_dict['list'][0]['bkgNo'],
                    )

    def get_vessel_eta(self, container):
        vessel_eta_payload['bkg_no'] = self.__get_form_data(container)['short_mbl']
        r = self.session.post(url=one_line_url, data=vessel_eta_payload, verify=False)
        response_dict = r.json()
        return response_dict['list'][1]['eta'].split()[0]

    def get_tracing_results_list(self, container):
        form_data_dict = self.__get_form_data(container)
        events_payload['cntr_no'] = container
        events_payload['bkg_no'] = form_data_dict['short_mbl']
        events_payload['cop_no'] = form_data_dict['cop_number']
        r = self.session.post(url=one_line_url, data=events_payload, verify=False)
        response_dict = r.json()
        return response_dict['list']

    def get_events_dict(self, container):
        events_dict = dict(scheduled_events=[])
        tracing_results_list = self.get_tracing_results_list(container)
        tracing_results_list.reverse()
        for result in tracing_results_list:
            event_description = result['statusNm']
            date = result['eventDt'].split()[0]
            location = result['placeNm']
            formatted_event_str = '{} {} {}'.format(date, event_description, location)
            if 'A' in result['actTpCd']:
                events_dict.update(dict(most_recent_event=formatted_event_str))
                break
            else:
                events_dict['scheduled_events'].append(formatted_event_str)

        return events_dict

    def get_formatted_events(self, _dict):
        most_recent_event = _dict['most_recent_event']
        scheduled_events_list = _dict['scheduled_events']
        scheduled_events_list.reverse()
        scheduled_events = '\n\t\t\t\t\t'.join(scheduled_events_list)
        return 'Most Recent Event:\t{}\nScheduled Events:\t\t{}'.format(most_recent_event, scheduled_events)
