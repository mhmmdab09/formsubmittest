from webbrowser import get
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import random
import string

SITEURL = ""
ELEMENTID = ""

br = webdriver.Chrome('/usr/bin/chromedriver')

br.get(SITEURL)


while( True ):
    phone = br.find_element(By.ID, ELEMENTID)
    phone.send_keys(random.randrange(11111111111, 99999999999, 11))
    phone.submit()
    sleep(3)