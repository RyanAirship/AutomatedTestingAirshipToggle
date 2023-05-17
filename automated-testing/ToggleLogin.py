#Imports
import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base import driver

def MenuText():
    print("Select the user you'd like to login as")
    print()
    print("[1] lionel.schumm@yahoo.com - 68 - Local")
    print("[2] TestNewAccount@qa.com - 949 - Local")
    print("[0] Exit Toggle Login Tool")
    print()

def ToggleMenu():
    option = int(input("Enter your choice:  "))
    print()

    while option != 0:
        if option == 1:
             ToggleLogin("lionel.schumm@yahoo.com","hTvdfn74g^","https://dashboard-local-dev.mytoggle.io:8090/login")
             option = 0
        elif option == 2:
             ToggleLogin("test2@qa.com","P@ssword1!","https://dashboard-local-dev.mytoggle.io:8090/login")
             option = 0
        else:
            print("Invalid option")

def ToggleLogin(email_input,password_input,login_url_input):
    # Logs a user in skipping the 2FA section
    driver.get(login_url_input)
    driver.maximize_window()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME,"email")))

    emailfield = driver.find_element(By.NAME,"email")
    emailfield.click()
    emailfield.send_keys(email_input)
    
    passwordfield = driver.find_element(By.NAME,"password")
    passwordfield.click()
    passwordfield.send_keys(password_input)

    loginbutton = driver.find_element(By.CLASS_NAME,"toggle-login-button")
    loginbutton.click()

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"app\"]/div/div[3]/div[2]/div/p[5]"))).click()