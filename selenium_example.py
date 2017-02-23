# use selenium to scrape site with infinite scroll bar

#!usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

member = []
PAGEDOWN = 10  # the number of pagedown needed to exhaust the page
# let's use a member list of us senators on twitter as an example
URL = 'https://twitter.com/cspan/lists/senators/members'
# don't forget to set up the chrome driver for selenium
browser = webdriver.Chrome(os.getenv('CHROMEDRIVER') + 'chromedriver')
os.environ['webdriver.chrome.driver'] = os.getenv('CHROMEDRIVER'
                                                  + 'chromedriver')
browser.get(URL)
elem = browser.find_element_by_tag_name('body')
no_of_pagedowns = PAGEDOWN
while no_of_pagedowns:
    elem.send_keys(Keys.PAGEDOWN)
    time.sleep(1)  # sleep for one second
    no_of_pagedowns -= 1

post_elems = browser.find_element_by_class_name('username')
for post in post_elems:
    if post.text:  # check if it's an empty string
        member.append(str(post.text))  # append all the text to the list
# do whatever you want with the list
