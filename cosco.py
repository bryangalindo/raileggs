from constants import cosco_recent_event_url, cosco_vessel_eta_url


class COSCO:
    def __init__(self, containers_list, session, timestamp):
        self.containers_list = containers_list
        self.session = session
        self.timestamp = timestamp

    def format_containers_list(self):
        return ','.join(self.containers_list)

    def get_vessel_eta(self, container):
        r = self.session.get(url=cosco_vessel_eta_url.format(container, self.timestamp))
        return r.json()['data']['content'].split()[0]

    def get_most_recent_event_list(self):
        most_recent_event_list = []
        formatted_containers_list = self.format_containers_list()
        r = self.session.get(url=cosco_recent_event_url.format(formatted_containers_list, self.timestamp))
        recent_events_list = r.json()['data']['content']['containers']
        for event in recent_events_list:
            recent_event_dict = dict(
                container_number=event['container']['containerNumber'],
                date=event['container']['locationDateTime'].split()[0],
                event_description=event['container']['label'],
                location=event['container']['location'],
            )
            most_recent_event_list.append(recent_event_dict)

        return most_recent_event_list

    def format_most_recent_event(self, _dict):
        return 'Most Recent Event:\t{} {} {}'.format(
            _dict['date'],
            _dict['event_description'],
            _dict['location'],
        )
