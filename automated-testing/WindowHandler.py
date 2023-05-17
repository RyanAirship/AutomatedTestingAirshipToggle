from base import *

def ResetToTestPage():
    driver.get("https://large-type.com/#TEST")

def IfOneTabOpen():
    windows = driver.window_handles
    if len(windows) == 1:
        return True
    else: 
        return False
    
def SwitchToParentTab():
    if IfOneTabOpen():
        print("Error: Attempted to switch to most parent tab when on parent tab")
    else:
        windows = driver.window_handles
        driver.switch_to.window(windows[0])

def SwitchToMostRecentTab():
    if IfOneTabOpen():
        print("Error: Attempted to switch to most recent tab with only one tab open")
    else:
        windows = driver.window_handles
        window_length = len(windows)
        driver.switch_to.window(windows[(window_length-1)])