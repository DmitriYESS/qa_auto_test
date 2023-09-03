from selenium.webdriver.common.by import By


class BasePageLocators:
    BUTTON_ELEMENTS = (By.XPATH, "//h5[normalize-space()='Elements']")
    CHECKBOX = (By.XPATH, "(//li[@id='item-1'])[1]")
    HOME = (By.XPATH, "//button[@title='Expand all']")
    DOWNLOADS = (By.XPATH, "//li[3]//span[1]//button[1]")
    CHECKBOX_WORD_FILE = (By.CSS_SELECTOR, "label[for='tree-node-wordFile']")
