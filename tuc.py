#NaruIge
from gettext import install
from selenium import webdriver
import random

#pip install selenium
#import sys


driver = webdriver.Chrome()

driver.get("https://docs.google.com/forms/d/e/1FAIpQLScH-cTd8LzNcV-lPZZFuEWX3kAcoI5I35ZZRgdc6EmDj69CvA/viewform?usp=pp_url&entry.2095748066=p19106tn@gm.tsuda.ac.jp&entry.506827147=堤菜留美&entry.2127889036=学生&entry.2091709137=A&entry.1957735619=11時20分〜11時30分&entry.2129216433=普通")

print("DONE")
#driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div/div/span/span").click()
driver.find_element_by_class_name("lRwqcd").click()

driver.quit()