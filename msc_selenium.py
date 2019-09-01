from datetime import datetime
from bs4 import BeautifulSoup
import selenium.webdriver.support.ui as ui

class MSC:
    def __init__(self, driver):
        self.driver = driver

    def get_tracing_results_html(self):
        return BeautifulSoup(self.driver.page_source, 'lxml')

    def search_for_container(self, container):
        search_input_box = self.driver.find_element_by_id('ctl00_ctl00_plcMain_plcMain_TrackSearch_txtBolSearch_TextField')
        search_input_box.send_keys(container)
        search_button = self.driver.find_element_by_id('ctl00_ctl00_plcMain_plcMain_TrackSearch_hlkSearch')
        search_button.click()

    def get_vessel_eta(self, html):
        tag_id = 'ctl00_ctl00_plcMain_plcMain_rptBOL_ctl00_rptContainers_ctl01_TrackingContainer_tdEtaResultField'
        vessel_eta_str = (html.find('td', {'id': tag_id})).text.strip()
        vessel_eta_datetime = datetime.strptime(vessel_eta_str, '%d/%m/%Y')
        vessel_eta = datetime.strftime(vessel_eta_datetime, '%m/%d/%Y')
        return vessel_eta

    def get_all_events_dict(self, url, container):
        self.driver.get(url)
        self.search_for_container(container)

        wait = ui.WebDriverWait(self.driver, 10)

        wait.until(lambda driver: driver.title.lower().startswith('shipping'))

        html = self.get_tracing_results_html()
        vessel_eta = self.get_vessel_eta(html)
        tracing_results_html_table = html.find('table', {'class': 'resultTable'})
        tracing_results_rows = tracing_results_html_table.find_all('tr')
        events_dict = dict(scheduled_events=[], vessel_eta=vessel_eta)

        for row in tracing_results_rows[1:]:
            if 'future' in row.attrs['class'][0]:
                columns = row.find_all('span', {'class': 'responsiveTd'})
                scheduled_event = ' '.join([column.text for column in columns])
                events_dict['scheduled_events'].append(' '.join(scheduled_event.split()))
            else:
                most_recent_event = ' '.join(row.text.split())
                events_dict.update(dict(most_recent_event=most_recent_event))
                break

        return events_dict

    def get_formatted_tracing_results(self, _dict):
        most_recent_event = _dict['most_recent_event']
        scheduled_events_list = _dict['scheduled_events']
        formatted_scheduled_events = '\n\t\t\t\t\t'.join(scheduled_events_list)
        return 'Most Recent Event:\t{}\nScheduled Events:\t{}'.format(most_recent_event,
                                                                      formatted_scheduled_events)