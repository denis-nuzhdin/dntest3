from selenium.webdriver.firefox.webdriver import WebDriver

class Application:

    def __init__(self):
        self.wd = WebDriver()

    def is_valid(self):
        try:
            self.wd.current_url()
            return True
        except:
            return False

    def open_site(self):
        # open site
        wd = self.wd
        wd.get("http://demo07.i-sys.ru:3003")

    def destroy(self):
        self.wd.quit()