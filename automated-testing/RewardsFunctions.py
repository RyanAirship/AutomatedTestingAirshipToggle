#Imports
import pytest
from selenium import webdriver
from base import driver
import sys

def WindowReset():
    driver.execute_script("window.resizeTo(800, 600);")
    driver.minimize_window()
    driver.get("https://large-type.com/#Don't%20close%20this%20window%2C%20it%20is%20the%20rewards%20parent%20tab")

def CreateURL():
    return "https://pages-local-dev.airship.co.uk/rewards/"+sys.argv[1]

def CreateURLByHash(sys_contacthash):
    return "https://pages-local-dev.airship.co.uk/rewards/"+sys_contacthash

def OpenWallet():
    driver.get(CreateURL())
    driver.maximize_window()

def OpenWalletByHash(sys_contacthash):
    driver.get(CreateURLByHash(sys_contacthash))
    driver.maximize_window()