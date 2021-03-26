import csv
from getpass import getpass
from time import sleep
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions

# browser and driver specifications
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://twitter.com/login")


# wait-function
def waiting_func(xpath):
    xpath_username = xpath
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, xpath_username)))


# login funtcion for username and password
def login(username, password, driver):
    xpath_username = '//input[@name="session[username_or_email]"]'
    # WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, xpath_username)))
    waiting_func(xpath_username)
    uid_input = driver.find_element_by_xpath(xpath_username)
    uid_input.send_keys(username)

    pwd_input = driver.find_element_by_xpath('//input[@name="session[password]"]')
    pwd_input.send_keys(password)
    try:
        pwd_input.send_keys(Keys.RETURN)
        url = "https://twitter.com/home"
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(url))
    except exceptions.TimeoutException:
        print("Timeout while waiting for home screen")

    driver.get("https://twitter.com/home")


def search(input):
    xpath_searchBox = '//input[@aria-label="Search query"]'
    waiting_func(xpath_searchBox)
    search_input = driver.find_element_by_xpath(xpath_searchBox)
    search_input.send_keys(input)
    search_input.send_keys(Keys.RETURN)


def select_by_xpath(xpath):
    waiting_func(xpath)
    search_input = driver.find_element_by_xpath(xpath)
    search_input.send_keys(Keys.RETURN)


def select_by_link(link):
    search_input = driver.find_element_by_link_text(link)
    search_input.send_keys(Keys.RETURN)


def tweet_headline_filter(filter_keyword, tweet):
    pretweet_words = tweet.text.split()
    tweet_words = [str(i) for i in pretweet_words]
    if tweet_words[0] == filter_keyword[0]:
        return True
    else:
        return False

def extract_numbers(tweet):
    preword_list = tweet.text.split()
    word_list = [str(i) for i in preword_list]
    likes = word_list[-1]
    retweets = word_list[-2]
    comments = word_list[-3]
    numbers = ["likes: " + str(int(likes)), "retweets: " + str(int(retweets)), "comments: " + str(int(comments))]
    for index in numbers:
        print(index)


