import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import  Options



executable_path = "/Users/grow09/Desktop/parser/parser/chromedriver" 
os.environ["webdriver.chrome.driver"] = executable_path 
chrome_options = Options()
# chrome_options.add_extension('/Users/grow09/Desktop/djangoprojects/shopenv/parser/parser/extension_1_17_21_0.crx') 
chrome_options.add_extension('/Users/grow09/Desktop/parser/parser/extension_2_2_1_0.crx') 
driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options) 


def logining():
    driver.get("https://steamcommunity.com/login")
    login = driver.find_element_by_id("steamAccountName")
    login.send_keys("log")
    password = driver.find_element_by_id("steamPassword")
    password.send_keys("pass")
    steamlogin = driver.find_element_by_id("SteamLogin")
    steamlogin.click()
    time.sleep(15)

def steambuy():
    try:
        time.sleep(12)
        driver.get("") 
        time.sleep(3)
    # code for SIH querys
        # WebElement = driver.find_element_by_id("allfloatbutton")
        # WebElement.click()
        # time.sleep(25)
        # def scan_items(self):
    # Taking floats from all weapons in page
        float_list = []
        floatlist = driver.find_elements_by_class_name("csgofloat-itemfloat")
        for elem in floatlist:
            float_list.append(elem.text)
        print(float_list)
    # Change list to row
        A = ' '.join(float_list) 
        A = A.split()
        print(A)
    # Concatinating floatlist 
        if len(A) == 20:
            good_list = [A[1], A[3], A[5], A[7], A[9], A[11], A[13], A[15], A[17], A[19]]
        else:
            steambuy()
        for i, item in enumerate(good_list):
            good_list[i] = float(item)
        print(good_list)
        D = []
        x = 0
        print(len(good_list))
    # looking for float higher 75
        for i, j in enumerate(good_list):
            if j > x:
                x = j
                D = i
        if x > 0.75:
            print(x)
        else:
            steambuy()
        print(D)
        print(type(D))
    # looking for list of buttons buttons
        buy_list = []
        buylist = driver.find_elements_by_class_name("item_market_action_button")
        for elem in buylist:
            buy_list.append(elem.get_attribute('href'))
    # # if len(buy_list) == 10:
    # #     G = D
    # # else:
    # #     G = D-1
    # print(G)
    # print(buy_list)
    # print(buy_list[G])
        driver.execute_script(buy_list[D])
        time.sleep(1)
    # taking correct JS button script
        steamlogin = driver.find_element_by_id("market_buynow_dialog_accept_ssa")
        steamlogin.click()
        steamlogin = driver.find_element_by_id("market_buynow_dialog_purchase")
        steamlogin.click()
        time.sleep(45)
        while True:
                steambuy()
    except:
        steambuy()

if __name__ == '__main__':
    try:
        logining()
        steambuy()
    except:
        pass