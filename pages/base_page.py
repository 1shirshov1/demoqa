class BasePage:   # Класс сохраняет методы для Всех страниц
    def __init__(self, driver, base_url):     # def __init__ метод иницииализации, сюда передается драйвер и URL  страницы
        self.driver = driver    # объект self
        self.base_url = base_url  # 'https://demoqa.com/'

    def visit(self):     # метод входа на страницу (открывает браузер
        return self.driver.get(self.base_url)

    def back(self):   # метод  back шаг назад в браузере
        self.driver.back()

    def forward(self):  # метод  back шаг вперед в браузере
        self.driver.forward()

    def refresh(self):
        self.driver.refresh()

    def get_url(self):      # метод получения URL на которой находится тест
        """ Returns current browser URL. """
        return self.driver.current_url

    def get_title(self):
        return self.driver.title   #

    def equal_url(self):  # метод который сравнивает URL
        if self.get_url() == self.base_url:   # через self обращаюсь к get_url
            return True
        return False