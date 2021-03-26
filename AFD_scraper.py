from twitter import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

login("VishiC1","WVuKgDGhzpq3S99",driver)
driver.maximize_window()
time.sleep(3)
search("Alternative für Deutschland")
#xpath for AFD link on search page
select_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div[3]/div/div/div/div[2]/div[1]/div[1]/a')


time.sleep(10)

#mach eine Liste von den tweets auf der Seite!
tweets = driver.find_elements_by_css_selector("[data-testid=\"tweet\"]")


for tweet in tweets:
    print(tweet.text)

print("")
print("")

index = 1
for tweet in tweets:
    print("tweet " + str(index))
    print(" ")
    extract_numbers(tweet)
    print(" ")
    index += 1





