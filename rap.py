import time
import pronouncing
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

topic = input("pls give a topic: ")
x = random.choice(pronouncing.rhymes(topic))

print(x)




browser = webdriver.Firefox()

browser.get('https://www.oxfordlearnersdictionaries.com/us/')

search_box = browser.find_element("name", "q")

search_box.send_keys(topic)

search_box.submit()
print("loading....")
time.sleep(10)
print("done")
l=browser.find_elements("class name", "x")

for i in l:
   pls_work = random.choice(l).text
   pls_work0 = pls_work.splitlines()
   pls_work1 = random.choices(pls_work0, k=1) #trying to grab a random list from the pls_work0 list but doesnt work 
   print(pls_work1)

browser.quit()
