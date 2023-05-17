from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from base import driver
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from StripeCardDetails import CardMap

def BootStore():
    driver.get("https://ryan-s-qa-testing-company.mytoggle.io/")
    driver.maximize_window()

def BackToHome():
    driver.get("https://ryan-s-qa-testing-company.mytoggle.io")

def BuyTestItem(Email,PaymentMethod):
    
    #Locate all the products on the store and select the first
    options = driver.find_elements(By.CLASS_NAME,"button") # The products begin at index [4], as the ones before this are the home, check balanace, collection, and register card buttons
    sleep(0.5)
    options[4].click()
    sleep(1)
    
    #Add a reference message
    MessageInput = driver.find_element(By.NAME,"message")
    MessageInput.click()
    MessageInput.send_keys("Automated test buying product message "+datetime.datetime.now().strftime("%I:%M%p, %B %d, %Y"))
    sleep(0.5)
    
    #Click checkout
    driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[2]/div/div/div[2]/div/fieldset/div[3]/div/div/button").click()
    sleep(0.5)
    
    #There will be new buttons now, because we're on the confirmation screen from adding to cart
    options = driver.find_elements(By.CLASS_NAME,"button")

    #Go to basket
    options[3].click()
    sleep(0.5)

    #Click choose delivery
    # The button element is not locatable so instead the program will just url jump to the delivery options
    driver.get("https://ryan-s-qa-testing-company.mytoggle.io/delivery")
    sleep(0.5)
    
    #Enter the email to send the order to
    EmailField = driver.find_element(By.XPATH,"//*[@id=\"basket\"]/div[2]/div/div/div/div/input")
    EmailField.click()
    EmailField.send_keys(Email)
    sleep(0.5)

    #Proceed to the payment screen
    driver.get("https://ryan-s-qa-testing-company.mytoggle.io/payment")
    timeout = 30
    try:
        element_present = EC.presence_of_element_located((By.XPATH,"//*[@id=\"payment-form\"]/div[4]/div/button"))
        WebDriverWait(driver, timeout).until(element_present)
        sleep(10)
        
        #Fill in all the payment fields
        driver.find_element(By.XPATH,"//*[@id=\"payment-form\"]/div[1]/div[1]/div/input").click()
        driver.find_element(By.XPATH,"//*[@id=\"payment-form\"]/div[1]/div[1]/div/input").send_keys(PaymentMethod)
        driver.find_element(By.XPATH,"//*[@id=\"payment-form\"]/div[1]/div[2]/div/input").click()
        driver.find_element(By.XPATH,"//*[@id=\"payment-form\"]/div[1]/div[2]/div/input").send_keys("Test")
        driver.find_element(By.XPATH,"//*[@id=\"payment-form\"]/div[1]/div[3]/div/input").click()
        driver.find_element(By.XPATH,"//*[@id=\"payment-form\"]/div[1]/div[3]/div/input").send_keys(Email)
        driver.find_element(By.XPATH,"//*[@id=\"payment-form\"]/div[1]/div[4]/div[2]/div/input").click()
        driver.find_element(By.XPATH,"//*[@id=\"payment-form\"]/div[1]/div[4]/div[2]/div/input").send_keys("Test Address")
        driver.find_element(By.XPATH,"//*[@id=\"payment-form\"]/div[1]/div[4]/div[3]/div/input").click()
        driver.find_element(By.XPATH,"//*[@id=\"payment-form\"]/div[1]/div[4]/div[3]/div/input").send_keys("Test City")
        driver.find_element(By.XPATH,"//*[@id=\"payment-form\"]/div[1]/div[4]/div[3]/div/input").click()
        driver.find_element(By.XPATH,"//*[@id=\"payment-form\"]/div[1]/div[4]/div[4]/div/input").send_keys("S1A 1AA")
        
        #The card details are inside an iframe for security purposes (Have to switch to that frame)
        # When you arrive at the iframes for the card number, exp. date, CVC, and zip:
        driver.switch_to.frame(frame_reference=driver.find_element(By.XPATH, '//*[@id="card-number"]/div/iframe'))
        driver.find_element(By.NAME,'cardnumber').send_keys(CardMap[PaymentMethod])
        #Exit the iFrame once we are done
        driver.switch_to.default_content()

        driver.switch_to.frame(frame_reference=driver.find_element(By.XPATH, '//*[@id="card-expiry"]/div/iframe'))
        driver.find_element(By.NAME,'exp-date').send_keys('0125')
        #Exit the iFrame once we are done
        driver.switch_to.default_content()

        driver.switch_to.frame(frame_reference=driver.find_element(By.XPATH, '//*[@id="card-cvc"]/div/iframe'))
        driver.find_element(By.NAME,'cvc').send_keys('123')
        #Exit the iFrame once we are done
        driver.switch_to.default_content()

        #Click the Pay button to finish the order
        sleep(0.5)
        driver.find_element(By.XPATH,"//*[@id=\"payment-form\"]/div[4]/div/button").click()

        print("Completed the test for "+str(PaymentMethod)+" please wait 10 seconds before returning to the store")
        sleep(10)
        BackToHome()

    except TimeoutException:
        print("Timed out waiting for payment screen to load")
