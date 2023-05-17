from base import *

def RetrieveMenuObject():
    MenuObject = driver.find_elements(By.CLASS_NAME,"toggle-multi-tier-sidenav-ul")
    return MenuObject

def GoToEmailBuilder():
    # Wait for element to load and then define it
    WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.XPATH,"//a[@class='nuxt-link-exact-active nuxt-link-active']")))
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,"//a[normalize-space()='Email builder']")))
    EmailButton = driver.find_element(By.XPATH,"//a[normalize-space()='Email builder']")
    
    # Email button element is not clickable off the cuff - Not 100% why
    HoverBeforeClicking(EmailButton)
