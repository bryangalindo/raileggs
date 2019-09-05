import selenium.webdriver as webdriver
from constants import driver_path


def has_digits(input_str):
    return any(char.isdigit() for char in input_str)


def start_headless_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    return webdriver.Chrome(executable_path=driver_path)
