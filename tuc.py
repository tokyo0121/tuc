#NaruIge
from gettext import find
import time
import requests
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
 
driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://docs.google.com/forms/d/e/1FAIpQLScH-cTd8LzNcV-lPZZFuEWX3kAcoI5I35ZZRgdc6EmDj69CvA/viewform?usp=pp_url'
driver.get(url)

menu = find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div/div[2]/div/span')
print(menu)

info_url = (url 
        + '&entry.506827147=' + '鈴木貴久' 
        + '&entry.1957735619=' + '12時〜12時20分'
        + '&entry.2091709137=' + menu
        + '&entry.2095748066=' + 'takahisa@tsuda.ac.jp'
        + '&entry.2127889036=' + '教員'
        + '&entry.2129216433=' + '普通')

driver.get(info_url)

print(info_url)

def click(x):
  driver.find_element_by_xpath(x).click()

next_btn = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div'
click(next_btn)

submit = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]'
click(submit)

print('DONE!')

time.sleep(5)

driver.close()
driver.quit()