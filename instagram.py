from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.common.action_chains import ActionChains
import os
from bs4 import BeautifulSoup
import pandas as pd


try:
    searchInput = input("Enter the hastag : ")
    followersNum = input("Enter number of followers : ")
    followersNum = int(followersNum)
    print(type(searchInput))
    print(type(followersNum))

except Exception as e:
    print(e)

try:
    # driver = webdriver.Chrome()
    # WINDOW_SIZE = "1366,768"
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    # options.add_argument("--window-size=%s" % WINDOW_SIZE)
    options.add_argument('--disable-gpu')
    # caps = DesiredCapabilities().CHROME
    # caps["pageLoadStrategy"] = "eager"
    # driver = webdriver.Chrome()

    driver = uc.Chrome(use_subprocess=True)
    driver.maximize_window()
    driver.set_page_load_timeout(300)

    driver.get("https://www.instagram.com")
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name = 'username']")))
    element.send_keys("berserk0334")
    driver.find_element(
        By.XPATH, "//input[@name = 'password']").send_keys("berserkingdgaf")
    driver.find_element(By.XPATH, "//div[contains(text(), 'Log in')]").click()


except WebDriverException as e:
    print(e)

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Search')]")))
    element.click()
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@aria-label = 'Search input']")))
    element.send_keys("#"+searchInput)
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class = '_ab8w  _ab94 _ab97 _ab9f _ab9k _ab9p  _aba0 _aba8 _abcm']")))
    element.click()
    elements = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@class = '_aagu']")))
    link = driver.current_url
    for element in range(len(elements)):
        elements = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class = '_aagu']")))
        actions = ActionChains(driver)
        actions.move_to_element(elements[element]).click().perform()
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@class = 'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _acan _acao _acat _acaw _aj1- _a6hd']")))
        element.click()
        followers = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a/div/span/span")))
        fol = followers.get_attribute("innerText")
        if fol.find("K") > -1:
            fol = fol.replace("K", "")
            fol = float(fol)
            fol = int(fol)
            fol = fol * 1000
        elif fol.find("M") > -1:
            fol = fol.replace("M", "")
            fol = float(fol)
            fol = int(fol)
            fol = fol * 1000000
        else:
            fol = int(fol)
        if fol < followersNum:
            print("less")
        else:
            print("more")
            driver.get(link)
    time.sleep(32423423)


except Exception as e:
    print(e)
