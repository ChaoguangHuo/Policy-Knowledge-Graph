#coding=utf-8
import time
import csv
import codecs
import os
import re
import urllib

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
driver=webdriver.Chrome('C:\Python36\webdriver\chromedriver_win32.exe')

sumpage=35#define the total page number
homepage=str('http://www-pkulaw-com-s.vpn.ruc.edu.cn')# homepage
fweb=open('D:/HUO/data_policy/central_policy_ncov_web.csv','w',encoding='utf-8-sig') ######change according your computer
writer=csv.writer(fweb)
##########vpn_login
def vpn_login()
    driver.get('https://vpn.ruc.edu.cn/por/login_psw.csp?redirect_uri=http%3A%2F%2Fwww-pkulaw-com-s.vpn.ruc.edu.cn%2F&rnd=0.7024457470738152#https%3A%2F%2Fvpn.ruc.edu.cn%2F%3Fredirect_uri%3Dhttp%253A%252F%252Fwww-pkulaw-com-s.vpn.ruc.edu.cn%252F')
    time.sleep(30)
    driver.find_element_by_id('svpn_name').send_keys('')#account
    driver.find_element_by_id('svpn_password').send_keys('')#password
    driver.find_element_by_id('logButton').click()
    time.sleep(30)
##########
i=1
def first(a):
    driver.get(a)
    time.sleep(40)
def contin(page):
    driver.find_element_by_name('jumpToNum').send_keys(page)
    driver.find_element_by_class_name('jumpBtn').click()
def clean(string):
    return re.sub(r'\s+','',string)
def has_href_no_class(tag):
    return tag.has_attr('href') and not tag.has_attr('class')
def search():
    listwrap=driver.find_element_by_class_name('list-wrap').get_attribute('innerHTML')
    soup=BeautifulSoup(listwrap,'html5lib')
    for h4 in soup.find_all('h4'):
        for hhref in h4.find_all(has_href_no_class):
            x=str(homepage)+str(hhref.attrs['href'])
            writer.writerow([x])
def nextpage():
    driver.find_element_by_link_text('下一页').click()
def refresh():
    driver.refresh()

p1='https://www.pkulaw.com/law/condition/chl?recordId=51b0a989-f510-4ac6-a59b-ed2e03bdc1a6'
first(p1)
for xx in range(0,sumpage):
    try:
        search()
        nextpage()
        time.sleep(30)
        i+=1
    except NoSuchElementException:
        driver.refresh()
        contin(i)
    if i%50==0:
        print(i)
    
fweb.close()
driver.quit()

