#Imports
from base import *
from WindowHandler import *

def BlindLogin(if_local):
    # Clicks on blind login and switch to the tab it opens
    if if_local == "local":
        driver.get("https://www-local-dev.airship.co.uk/console/index.php?module=BlindLogIn")
        driver.maximize_window()
        # Enter Y Test Company
        driver.find_element(By.NAME,"4").click()

        # Switch to the window that's just opened
        SwitchToMostRecentTab()
    else:
        driver.get("https://www.airship.co.uk/console/index.php?module=BlindLogIn")
        driver.maximize_window()
        # Enter Test Account - Ryan Testing Company
        driver.find_element(By.NAME,"667").click()

        # Switch to the window that's just opened
        SwitchToMostRecentTab()