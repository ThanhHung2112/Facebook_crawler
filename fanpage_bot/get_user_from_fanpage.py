from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.chrome.service import Service

from time import sleep
import random

from login_fb import Login


class GET_USER_FFANPAGE():
    def __init__(self):

        self.username = "yelan482@gmail.com"
        self.password = "Linhcute542002"
        # Options

        service = Service(executable_path='fanpage_bot/chromedriver.exe')
        options = ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--disable-extensions")
        # options.add_argument("--headless")
        options.add_argument("--incognito")
        options.add_argument("--window-size=1920x1080")

        self.browser = Chrome(service=service, options=options)
        # self.browser = Login().login()

    def login(self):

        self.browser.get("https://www.facebook.com/")
        assert "Facebook" in self.browser.title
        elem = self.browser.find_element(By.ID, "email")
        elem.send_keys(self.username)
        elem = self.browser.find_element(By.ID, "pass")
        elem.send_keys(self.password)

        self.browser.find_element(By.NAME, "login").click()
        sleep(random.randint(3,5))
       

        return
    
    def get_user_link(self):

        return self.browser.get("https://www.facebook.com/DoantruongQuocHoc")

        
    

G = GET_USER_FFANPAGE()
G.login()
G.get_user_link()
# G.runs()

