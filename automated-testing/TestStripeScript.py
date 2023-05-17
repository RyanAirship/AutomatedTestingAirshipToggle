from AirshipLogin import AirshipLogin
from ToggleLogin import ToggleLogin
from BootWebstore import BootStore
from CreateProduct import *
from WebshopCommands import *
from time import sleep
from StripeCardDetails import CardNames

BootStore()
sleep(1)
BuyTestItem("ryan.goodall+AutomatedPurchase@airship.co.uk",CardNames[0])
sleep(1)
BuyTestItem("ryan.goodall+AutomatedPurchase@airship.co.uk",CardNames[1])
sleep(1)
BuyTestItem("ryan.goodall+AutomatedPurchase@airship.co.uk",CardNames[2])
sleep(1)
BuyTestItem("ryan.goodall+AutomatedPurchase@airship.co.uk",CardNames[3])
sleep(1)
BuyTestItem("ryan.goodall+AutomatedPurchase@airship.co.uk",CardNames[4])
sleep(1)
BuyTestItem("ryan.goodall+AutomatedPurchase@airship.co.uk",CardNames[5])
sleep(1)
BuyTestItem("ryan.goodall+AutomatedPurchase@airship.co.uk",CardNames[6])
sleep(1)
BuyTestItem("ryan.goodall+AutomatedPurchase@airship.co.uk",CardNames[7])
sleep(1)
BuyTestItem("ryan.goodall+AutomatedPurchase@airship.co.uk",CardNames[8])
sleep(1)
BuyTestItem("ryan.goodall+AutomatedPurchase@airship.co.uk",CardNames[9])
sleep(1)
BuyTestItem("ryan.goodall+AutomatedPurchase@airship.co.uk",CardNames[10])
sleep(1)
BuyTestItem("ryan.goodall+AutomatedPurchase@airship.co.uk",CardNames[11])
sleep(1)
BuyTestItem("ryan.goodall+AutomatedPurchase@airship.co.uk",CardNames[12])
sleep(1)
BuyTestItem("ryan.goodall+AutomatedPurchase@airship.co.uk",CardNames[13])
print("Automated Stripe product pruchasing tests complete")
