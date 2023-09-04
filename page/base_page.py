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

        self.browser.implicitly_wait(5)
        button = self.browser.find_element(*BasePageLocators.BUTTON_ELEMENTS)
        assert button, "button is not presented"
        button.click()

    def open_checkbox(self):

        self.browser.implicitly_wait(5)
        checkbutton = self.browser.find_element(*BasePageLocators.CHECKBOX)
        assert checkbutton, "button is not presented"
        checkbutton.click()

    def open_home(self):

        self.browser.implicitly_wait(5)
        home_button = self.browser.find_element(*BasePageLocators.HOME)
        assert home_button, "button is not presented"
        home_button.click()

    def open_downloads(self):

        self.browser.implicitly_wait(5)
        download_button = self.browser.find_element(*BasePageLocators.DOWNLOADS)
        assert download_button, "button is not presented"
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", download_button)
        time.sleep(2)
        download_button.click()

    def chose_word_file(self):

        try:
            word_file_button = self.browser.find_element(*BasePageLocators.CHECKBOX_WORD_FILE)
        except NoSuchElementException:
            self.browser.find_element(*BasePageLocators.DOWNLOADS).click()
            self.browser.implicitly_wait(5)
            word_file_button = self.browser.find_element(*BasePageLocators.CHECKBOX_WORD_FILE)
            assert word_file_button, "button is not presented"
            word_file_button.click()
            print('You have selected:wordFile')
