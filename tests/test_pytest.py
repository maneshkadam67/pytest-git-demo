import time

import selenium
import webdriver_manager
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.service import Service as ChromeService


class TestClass:
    def test_ebayFlow(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        wait = WebDriverWait(driver, 10)
        url = 'https://www.ebay.com/'
        driver.get(url)  # "https//:www.rcvacademy.com")
        driver.maximize_window()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="gh-ac"]').send_keys('Mobile')
        driver.find_element(By.XPATH, '//*[@id="gh-btn"]').click()
        time.sleep(5)
        price = driver.find_element(By.XPATH, '//*[@id="item2b4e543087"]/div/div[2]/div[2]/div[1]/span').text
        price_without_dollar = price.replace("$", "")
        print("price_without_dollar", price_without_dollar)
        parent_handle = driver.current_window_handle
        print("outside handle", driver.current_window_handle)
        driver.find_element(By.XPATH, '//*[@id="item2b4e543087"]/div/div[2]/a').click()
        time.sleep(5)
        driver.close()

