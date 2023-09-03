import time

from .page.base_page import WorkPage


link = "https://demoqa.com/"

def test_main_page(browser):
    page = WorkPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.open_element_page() # открываем элементы
    page.open_checkbox() # кликаем на Check Box
    page.open_home() # открываем директорию Home
    #page.open_downloads() # раскрываем директроию downloads
    page.chose_word_file() # Выбираем checkbox Word file
    time.sleep(5) # ждем 5 секунд перед выходом браузера для наглядности, что все действия были выполнены


