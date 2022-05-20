#NaruIge
import time
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
 
url = 'https://docs.google.com/forms/d/e/1FAIpQLScH-cTd8LzNcV-lPZZFuEWX3kAcoI5I35ZZRgdc6EmDj69CvA/viewform?usp=pp_url'

info_url = (url 
        + '&entry.506827147=' + '鈴木貴久' 
        + '&entry.1957735619=' + '12時〜12時20分'
        + '&entry.2091709137=' + 'A'
        + '&entry.2095748066=' + 'takahisa@tsuda.ac.jp'
        + '&entry.2127889036=' + '教員')

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(info_url)

print(info_url)

next_btn = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div'

def click(x):
  driver.find_element_by_xpath(x).click()

click(next_btn)

result_url = (info_url + '&entry.2129216433=' + '普通')

driver.get(result_url)
print(result_url)

submit = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]'

click(submit)

print('DONE!')


# driver.close()
# driver.quit()
