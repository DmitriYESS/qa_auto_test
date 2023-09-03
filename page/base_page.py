import time
from .lokators import BasePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class WorkPage:
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def open_element_page(self):

        button = self.browser.find_element(*BasePageLocators.BUTTON_ELEMENTS)
        self.browser.implicitly_wait(5)
        assert button, "button is not presented"
        button.click()

    def open_checkbox(self):

        checkbutton = self.browser.find_element(*BasePageLocators.CHECKBOX)
        self.browser.implicitly_wait(5)
        assert checkbutton, "button is not presented"
        checkbutton.click()

    def open_home(self):

        home_button = self.browser.find_element(*BasePageLocators.HOME)
        self.browser.implicitly_wait(5)
        assert home_button, "button is not presented"
        home_button.click()

    def open_downloads(self):

        download_button = self.browser.find_element(*BasePageLocators.DOWNLOADS)
        self.browser.implicitly_wait(5)
        assert download_button, "button is not presented"
        download_button.click()

    def chose_word_file(self):

        word_file_button = self.browser.find_element(*BasePageLocators.CHECKBOX_WORD_FILE)
        self.browser.implicitly_wait(5)
        assert word_file_button, "button is not presented"
        word_file_button.click()

