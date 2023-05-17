# This is the base file that will define the driver
import pytest
from selenium import webdriver
import sys
from time import sleep
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

ChromeOptions = Options()
ChromeOptions.add_argument("start-maximized")

driver = webdriver.Chrome(chrome_options = ChromeOptions ,service=Service(ChromeDriverManager().install()))

def HoverBeforeClicking(Element):
    ActionChains(driver).move_to_element(Element).perform()
    Element.click()
