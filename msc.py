from datetime import datetime

from bs4 import BeautifulSoup

from constants import msc_url

class MSC:
    def __init__(self, session):
        self.session = session

    def get_tracing_results_html(self, container):
        print('Scraping {}'.format(container))
        response = self.session.get(msc_url.format(container))
        return BeautifulSoup(response.content, 'lxml')

    def get_vessel_eta(self, html):
        vessel_eta_div = html.find('div', {'id': 'containerETA'})
        vessel_eta_str = vessel_eta_div.find('abbr').attrs['title']
        vessel_eta_datetime = datetime.strptime(vessel_eta_str[:-12], '%A, %B %d, %Y')
        vessel_eta = datetime.strftime(vessel_eta_datetime, '%m/%d/%Y')
        return vessel_eta

    def get_most_recent_event(self, html_table):
        return (html_table.find('tr', {'class': 'current'})).text.replace('\n', ' ')

    def get_scheduled_events(self, html_table):
        html_table_rows = html_table.find_all('tr')
        scheduled_events_list = []
        for i, row in enumerate(html_table_rows):
            if not html_table_rows[i].attrs:
                scheduled_events_list.append(row.text.replace('\n', ' '))
            else:
                break

        scheduled_events_list.reverse()
        return '\n\t\t\t\t\t'.join(scheduled_events_list)

    def get_all_events(self, html):
        tracing_results_html_table = html.find('tbody', {'class': 'results-content'})
        scheduled_events = self.get_scheduled_events(tracing_results_html_table)
        most_recent_events = self.get_most_recent_event(tracing_results_html_table)
        return 'Most Recent Event:\t{}\nScheduled Events:\t\t{}'.format(most_recent_events, scheduled_events)
