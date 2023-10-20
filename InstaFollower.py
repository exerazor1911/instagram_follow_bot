import os
import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

SIMILAR_ACCOUNT = 'rockstargames'
INSTAGRAM_URL = 'https://www.instagram.com/accounts/login/'

INSTAGRAM_LOGIN = os.environ.get("INSTAGRAM_LOGIN")
INSTAGRAM_PASSWD = os.environ.get("INSTAGRAM_PASSWD")


class InstaFollower:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.maximize_window()

    def login(self):
        self.driver.get(INSTAGRAM_URL)
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(
            INSTAGRAM_LOGIN
        )
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(
            INSTAGRAM_PASSWD
        )
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, '.x1i10hfl').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
        time.sleep(2)

    def find_followers(self):
        self.driver.find_element(By.LINK_TEXT, 'Search').click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, 'input').send_keys(
            SIMILAR_ACCOUNT
        )
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]').click()
        time.sleep(4)
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(2)
        # first_popup_item = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]')
        # first_popup_item.send_keys(Keys.END)
        self.scr1 = self.driver.find_element(By.CSS_SELECTOR, 'div ._aano')
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", self.scr1)

    def follow(self):
        all_buttons = self.scr1.find_elements(By.CSS_SELECTOR, "button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.scr1.find_element(By.CSS_SELECTOR, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


