import re
from bs4 import BeautifulSoup
import selenium.webdriver.support.ui as ui


class HPL:
    def __init__(self, driver):
        self.driver = driver

    def get_tracing_results_html(self):
        return BeautifulSoup(self.driver.page_source, 'lxml')

    def get_most_recent_event(self, html):
        most_recent_event_tag = html.find('table', {'id': 'tracing_by_container_f:hl56'})
        return most_recent_event_tag.text.split('Last Movement ')[1]

    def get_scheduled_events_list(self, html):
        scheduled_events_list = []
        tracing_results_html_table = html.find('table', {'id': 'tracing_by_container_f:hl66'})
        tracing_results_rows = tracing_results_html_table.find_all('tr')
        tracing_results_rows.reverse()

        for row in tracing_results_rows:
            if row.find('td', {'class': 'strong'}):
                break
            else:
                scheduled_event = ' '.join([column.text for column in row.find_all('td')])
                scheduled_events_list.insert(0, scheduled_event)

        return scheduled_events_list

    def get_vessel_eta(self, _list):
        vessel_arrivals_list = []
        for item in _list:
            if 'Vessel arrival' in item:
                vessel_arrivals_list.append(item)

        vessel_eta = (re.search('\d+-\d+-\d+', vessel_arrivals_list[-1])).group()
        return vessel_eta

    def get_all_events_dict(self, url, container):
        self.driver.get(url.format(container))
        wait = ui.WebDriverWait(self.driver, 10)

        wait.until(lambda driver: driver.title.lower().startswith('tracing'))
        wait.until(lambda driver: driver.find_element_by_id('tracing_by_container_f:hl56'))

        html = self.get_tracing_results_html()
        most_recent_event = self.get_most_recent_event(html)
        scheduled_events_list = self.get_scheduled_events_list(html)

        return dict(most_recent_event=most_recent_event,
                    scheduled_events=scheduled_events_list)

    def get_formatted_tracing_results(self, _dict):
        most_recent_event = _dict['most_recent_event']
        scheduled_events_list = _dict['scheduled_events']
        formatted_scheduled_events = '\n\t\t\t\t\t'.join(scheduled_events_list)
        return 'Most Recent Event:\t{}\nScheduled Events:\t{}'.format(most_recent_event,
                                                                      formatted_scheduled_events)
