# Contains functions relating to products in Toggle
from base import *
import datetime


#Functions to create any kind of product with dummy data
def CheckProducts():
    #Since adding a new product is a repetative action, I have copied the steps to get to the products screen into here
    #click the shop icon 
    driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[3]/div/div/div/ul/li[3]/a/span").click()
    sleep(1)
    #click the products option
    driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[3]/div/div/div/ul/li[3]/ul/li[1]/a").click()
    sleep(1)

def AddNew():
    #click Add
    CheckProducts()
    driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[4]/div[1]/button").click()
    sleep(1)

############################################################################################################################################################
def CreateGiftCard():
    AddNew()
    #click Gift Card
    driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[4]/div[2]/div/div/div/div[2]/div[1]/div/div/a").click()
    sleep(3)

    #Retrieve all the fields within classes
    fulfillments = driver.find_elements(By.CLASS_NAME,"toggle-input-checkbox-check-element")
    TextInputs = driver.find_elements(By.CLASS_NAME,"toggle-input")

    #Enter information into all the text fields
    TextInputs[0].click()
    TextInputs[0].send_keys("Test Gift "+datetime.datetime.now().strftime("%I:%M%p, %B %d, %Y"))
    TextInputs[1].click()
    TextInputs[1].send_keys("Automated Product Description")
    TextInputs[2].click()
    TextInputs[2].send_keys("Automated Long Description")

    #Check the "Pre-set value" tick box and set price as £1
    fulfillments[1].click()
    PriceInput = driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[4]/div/div[2]/div[2]/div[4]/div/div/div[2]/div[2]/div[1]/div/input")
    PriceInput.click()
    PriceInput.send_keys("1")

    #Select digital fulfillment ([2] would be physical) and allow scheduled delivery
    fulfillments[3].click()
    
    #Set as active and leave webshop as private
    driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[4]/div/div[2]/div[3]/div[3]/div/div/div/div/div/label[1]/div/span[2]").click()
    sleep(0.5)

    
    #Set to expire after 12 months
    driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[4]/div/div[3]/div/div/div[2]/div/div/div/select").click()
    sleep(0.5)
    driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div/div/select/option[4]").click()
    sleep(0.5)

    #Save the product
    driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[4]/div/div[4]/div/button").click()
    

############################################################################################################################################################
def CreateExperience():
    AddNew()
    #click Experience
    driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[4]/div[2]/div/div/div/div[2]/div[2]/div/div/a").click()
    sleep(3)

    #Retrieve all the fields within classes
    fulfillments = driver.find_elements(By.CLASS_NAME,"toggle-input-checkbox-check-element")
    #print("The length of fulfillments for experiences is " + str(len(fulfillments)))
    TextInputs = driver.find_elements(By.CLASS_NAME,"toggle-input")

    #Enter information into all the text fields
    TextInputs[0].click()
    TextInputs[0].send_keys("Experience "+datetime.datetime.now().strftime("%I:%M%p, %B %d, %Y"))
    TextInputs[1].click()
    TextInputs[1].send_keys("Automated Product Description")
    TextInputs[2].click()
    TextInputs[2].send_keys("Automated Long Description")

    #Check the "Pre-set value" tick box and set price as £1
    fulfillments[1].click()
    PriceInput = driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[4]/div/div[2]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/input")
    PriceInput.click()
    PriceInput.send_keys("1")

    #Select digital fulfillment and allow scheduled delivery - for some reason this needs clicking twice
    driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[4]/div/div[2]/div[3]/div[1]/div/div/label[2]/div/span[2]").click()
    sleep(0.5)
    driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[4]/div/div[2]/div[3]/div[1]/div/div/label[2]/div/span[1]").click()
   

    #Set as active and leave webshop as private
    sleep(0.5)
    driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[4]/div/div[2]/div[3]/div[3]/div/div/div/div/div/label[1]").click()
    
    #Set expiry after 12 months
    driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[4]/div/div[3]/div/div/div[2]/div/div/div/select").click()
    sleep(0.5)
    driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[4]/div/div[3]/div/div/div[2]/div/div/div/select/option[4]").click()
    sleep(0.5)
   
    #Set as active
    driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[4]/div/div[2]/div[3]/div[3]/div/div/div/div/div/label[1]/div/span[2]").click()
    sleep(0.5)

    #Save the product
    driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[4]/div/div[4]/div/button").click()

############################################################################################################################################################
def CreatePayItForward():
    AddNew()
    #Click Pay It Forward
    driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[4]/div[2]/div/div/div/div[2]/div[3]/div/div/a").click()
    sleep(3)
    TextInputs = driver.find_elements(By.CLASS_NAME,"toggle-input")

    #Enter information into all the text fields
    TextInputs[0].click()
    TextInputs[0].send_keys("Pay It Forward "+datetime.datetime.now().strftime("%I:%M%p, %B %d, %Y"))
    TextInputs[1].click()
    TextInputs[1].send_keys("Automated Pay It Forward Description")
    TextInputs[2].click()
    TextInputs[2].send_keys("Automated Pay It Forward Long Description")

    #Set as active
    driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[4]/div/div[2]/div[3]/div/div/div/div/div/div/label[1]/div/span[2]").click()
    sleep(0.5)

    # Set a webshop value option of £1
    PriceInput = driver.find_element(By.NAME,"ToggleInputCurrency")
    PriceInput.send_keys("1")
    
    # Save the product
    driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[4]/div/div[3]/div/button").click()
    

############################################################################################################################################################
def CreateRetailProduct():
    AddNew()
    #Click Retail Product
    driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[4]/div[2]/div/div/div/div[2]/div[4]/div/div/a").click()
    sleep(3)

############################################################################################################################################################
def CreateBundle():
    AddNew()
    #Click Bundle
    driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[4]/div[2]/div/div/div/div[2]/div[5]/div/div/a").click()
    sleep(5)

#//*[@id=\"app\"]/div/div[4]/div[2]/div/div/div/div[2]/div[2]/div/div/a

    #driver.find_element(By.XPATH,"   ").click()
