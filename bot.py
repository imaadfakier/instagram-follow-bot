import config
import os
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time


def wait(secs):
    time.sleep(secs)


class InstaFollower:
    """
    ...
    """

    # class attributes
    # ...

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=os.environ.get(key='CHROME_DRIVER_PATH'))

    def login(self):
        self.driver.get(url='https://www.instagram.com/accounts/login/')
        self.driver.maximize_window()
        wait(secs=1)
        username_input_field = self.driver.find_element_by_name(name='username')
        username_input_field.send_keys(os.environ.get(key='INSTAGRAM_USERNAME'))
        username_input_field = self.driver.find_element_by_name(name='password')
        username_input_field.send_keys(os.environ.get(key='INSTAGRAM_PASSWORD'))
        log_in_button = self.driver.find_element_by_xpath(xpath='//*[@id="loginForm"]/div/div[3]/button')
        log_in_button.click()

    def find_followers(self):
        # wait(secs=2)
        wait(secs=4)
        self.driver.get(url='https://www.instagram.com/streetwearmoods/')
        wait(secs=3)
        account_followers_link = self.driver.find_element_by_css_selector(css_selector='a.-nal3')
        account_followers_link.click()
        wait(secs=4)
        # followers_container_div = self.driver.find_element_by_class_name(name='isgrP')
        # self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', followers_container_div)
        # wait(secs=3)

    def follow(self):
        # start = 0
        followers_follow_button = self.driver.find_elements_by_class_name(name='sqdOP  ')  # spaces don't matter
        while True:
            for follower_follow_button in followers_follow_button:
                try:
                    follower_follow_button.click()
                except ElementClickInterceptedException as e:
                    cancel_unfollow_button = self.driver.find_element_by_css_selector(css_selector='.aOOlW.HoLwm')
                    cancel_unfollow_button.click()
                    # wait(secs=3)
                    # wait(secs=6)
                    wait(secs=2)
                    follower_follow_button.click()
                finally:
                    wait(secs=1)
            # self.find_followers()
            followers_container_div = self.driver.find_element_by_class_name(name='isgrP')
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', followers_container_div)
            # wait(secs=6)
            wait(secs=3)
            followers_follow_button = self.driver.find_elements_by_css_selector(
                css_selector='button.sqdOP  '
            )[len(followers_follow_button)::]
