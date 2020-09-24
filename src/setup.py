from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from config import keys
from time import sleep

class Buy:
    def __init__(self,K):
        self.fname      = K['firstname']
        self.lname      = K['lastname']
        self.street     = K['streetad']
        self.zip        = K['zip']
        self.state      = K['state']
        self.email      = K['email']
        self.phone      = K['cell']
        self.url        = K['productURL']
        self.driver     = webdriver.Chrome(executable_path='/Users/ljuboslav/git/buy/driver/chromedriver') # path to chromedriver

    def gosite(self):
        driver = self.driver
        driver.get(self.url)
        sleep(1)

    def addcart(self):
        driver = self.driver
        gosite = self.gosite()
        sleep(2)
        try:
            driver.find_element_by_id("landingpage-cart")
            print("Found Add to Cart.")
            try:
                driver.find_element_by_css_selector("#landingpage-cart > div > div.nav-col.call-to-action.call-to-action-main-product").click()
                print("Clicked Add to Cart.")
                sleep(0.2)
                if driver.find_elements_by_class_name("centerPopup-body") is not None:
                    driver.find_element_by_css_selector("#custom > div > div.centerPopup-bottom > div > div > div > button.btn.button-decline.btn-cancel").click()
                    sleep(5)
                    try:
                        driver.find_element_by_css_selector("#captcha > div > div.geetest_btn > div.geetest_radar_btn > div.geetest_radar_tip").click()
                        print("clicked: Human")
                    except:
                        print("HERE")
                        driver.find_element_by_id("recaptcha-anchor").click()
                        print("clicked: Verify")
                else:
                    print("error 1")
            except:
                print("error 2")
        except:
            print("error 3")
        # Destroy popup
        #driver.find_elements_by_class_name("close").click()





if __name__ == '__main__':
    buy = Buy(keys)
    buy.addcart()
