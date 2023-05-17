#Imports
from base import *

def AirshipLogin(username_input,password_input,login_url):
    driver.get(login_url)
    driver.maximize_window()
    
    fields = driver.find_elements(By.CLASS_NAME, "toggle-input")
    if (len(fields) == 2):
        fields[0].send_keys(username_input)
        fields[1].send_keys(password_input)
        fields[1].send_keys(Keys.RETURN)
    else:
        print("Wrong number of input fields")
    
    # Wait until 2FA button loads and then click it
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"app\"]/div[2]/div/div/div/div/p[4]"))).click()
