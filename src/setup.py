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
        gosite(self)


if __name__ == '__main__':
    buy = Buy(keys)
    buy.site()
