from datetime import datetime

from bs4 import BeautifulSoup

from constants import apl_scrape_url


class APL:
    def __init__(self, session):
        self.session = session

    def get_tracing_results_html(self, container):
        print('Scraping {}'.format(container))
        r = self.session.get(apl_scrape_url.format(container))
        html = BeautifulSoup(r.content, 'lxml')
        return html.find('tbody')

    def get_vessel_eta(self, html_table):
        tracing_results_table_rows = html_table.find_all('tr')
        for row in tracing_results_table_rows:
            tracing_results_columns = row.find_all('td')
            event_description = tracing_results_columns[2].text.strip()
            event_datetime_str = ' '.join(tracing_results_columns[0].text.split()[1:4])
            if 'Arrival final port of discharge' in event_description:
                vessel_eta_datetime = datetime.strptime(event_datetime_str, '%d %b %Y')
                vessel_eta = datetime.strftime(vessel_eta_datetime, '%m/%d/%Y')
                return vessel_eta

    def get_most_recent_event(self, html_table):
        current_container_status = [text.strip() for text in (html_table.find('tr', {'class': "is-current is-open"})).text.split('\r')]
        return dict(datetime=current_container_status[1], event_description=current_container_status[3],
                    location=current_container_status[5],)

    def get_scheduled_events(self, html_table):
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

    def get_tracing_results_dict(self, container):
        tracing_results_table = self.get_tracing_results_html(container)
        most_recent_event_dict = self.get_most_recent_event(tracing_results_table)
        scheduled_events = self.get_scheduled_events(tracing_results_table)
        vessel_eta = self.get_vessel_eta(tracing_results_table)
        return (
            dict(
                container=container,
                vessel_eta=vessel_eta,
                most_recent_event=most_recent_event_dict,
                scheduled_events=scheduled_events
            )
        )

    def format_tracing_results(self, _dict):
        all_scheduled_events_str = ''
        for i, items in enumerate(_dict['scheduled_events']):
            event_str = '{} {} {}\n\t\t\t\t\t'.format(
                _dict['scheduled_events'][i]['event_description'],
                _dict['scheduled_events'][i]['location'],
                _dict['scheduled_events'][i]['datetime'],
            )
            all_scheduled_events_str = all_scheduled_events_str + event_str

        return 'Most Recent Event:\t{} {} {}\nScheduled Events:\t\t{}'.format(
            _dict['most_recent_event']['event_description'],
            _dict['most_recent_event']['location'],
            _dict['most_recent_event']['datetime'],
            all_scheduled_events_str,
        )
