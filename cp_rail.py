from bs4 import BeautifulSoup
import selenium.webdriver.support.ui as ui
from constants import cp_login_url, cp_tracing_url


class CanadianPacific:
    def __init__(self, driver, containers_list):
        self.driver = driver
        self.containers_list = containers_list

    def format_containers_list(self):
        return '\n'.join(self.containers_list)

    def login(self):
        self.driver.get(cp_login_url)
        username_box = self.driver.find_element_by_id('username')
        password_box = self.driver.find_element_by_id('password')
        username_box.send_keys('CentransBryan')
        password_box.send_keys('6161Savoy')
        login_button = self.driver.find_element_by_class_name('login_button')
        login_button.click()

    def search_for_tracing(self, containers_list):
        self.driver.get(cp_tracing_url)
        search_box_element = self.driver.find_element_by_name('paramValue3470')
        search_box_element.send_keys(containers_list)
        lfd_button_element = self.driver.find_element_by_name('paramValue3478')
        lfd_button_element.click()
        tracing_submit_button = self.driver.find_element_by_xpath(
            '/html/body/table[2]/tbody/tr/td[2]/form/table/tbody/tr[15]/td/input[3]')
        tracing_submit_button.click()

    def get_tracing_results_hmtl(self):
        formatted_containers_list = self.format_containers_list()
        self.login()
        self.search_for_tracing(formatted_containers_list)

        wait = ui.WebDriverWait(self.driver, 10)
        wait.until(lambda driver: driver.find_element_by_id('rowTable'))
        return BeautifulSoup(self.driver.page_source, 'html.parser')

    def get_tracing_results_list(self):
        html = self.get_tracing_results_hmtl()
        tracing_results_table = html.find('table', {'id': 'rowTable'})
        tracing_results_rows = tracing_results_table.find_all('tr')
        tracing_results_list = []

        for i, row in enumerate(tracing_results_rows[1:]):
            tracing_results_columns = row.find_all('td')
            current_status = tracing_results_columns[3].text.strip()
            most_recent_event = tracing_results_columns[4].text.strip()
            if tracing_results_columns[7].text.strip():
                final_destination_eta = tracing_results_columns[7].text.strip()[1:11]
            else:
                final_destination_eta = ''
            if tracing_results_columns[-2].text.strip():
                last_free_day = tracing_results_columns[-2].text.strip().split()[0]
            else:
                last_free_day = ''
            tracing_results_list.append(
                dict(
                    container_number=self.containers_list[i],
                    current_status=current_status,
                    most_recent_event=most_recent_event,
                    final_destination_eta=final_destination_eta,
                    last_free_day=last_free_day
                )
            )

        return tracing_results_list

    def get_formatted_tracing_results(self, _dict):
        return 'Most Recent Event:\t{}\nCurrent Status:\t\t{} ETA: {}'.format(_dict['most_recent_event'],
                                                                              _dict['current_status'],
                                                                              _dict['final_destination_eta']
                                                                              )