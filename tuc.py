#NaruIge
from gettext import find
import time
import requests
import schedule
from selenium import webdriver
from time import sleep

# import datetime as dt
# import calendar

from webdriver_manager.chrome import ChromeDriverManager

#01 定期実行する関数を準備
def task():
  # フォームを送信する 
  driver = webdriver.Chrome(ChromeDriverManager().install())

  url = 'https://docs.google.com/forms/d/e/1FAIpQLScH-cTd8LzNcV-lPZZFuEWX3kAcoI5I35ZZRgdc6EmDj69CvA/viewform'
  driver.get(url)

  menu = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div/div[2]/div/span')
  print(menu.text)

  info_url = (url + '?usp=pp_url'
          + '&entry.506827147=' + '鈴木貴久' 
          + '&entry.1957735619=' + '12時〜12時20分'
          + '&entry.2091709137=' + menu.text
          + '&entry.2095748066=' + 'takahisa@tsuda.ac.jp'
          + '&entry.2127889036=' + '教員'
          + '&entry.2129216433=' + '普通')

  driver.get(info_url)

  next_btn = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div'
  driver.find_element_by_xpath(next_btn).click()

  submit = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]'
  driver.find_element_by_xpath(submit).click()
  time.sleep(5)

  driver.close()
  driver.quit()

  print("タスク実行済み")

#02 スケジュール登録
schedule.every().tuesday.at("01:38").do(task)

#03 イベント実行
while True:
    schedule.run_pending()
    sleep(1)