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
driver.get('https://vpn.ruc.edu.cn/por/login_psw.csp?redirect_uri=http%3A%2F%2Fwww-pkulaw-com-s.vpn.ruc.edu.cn%2F&rnd=0.7024457470738152#https%3A%2F%2Fvpn.ruc.edu.cn%2F%3Fredirect_uri%3Dhttp%253A%252F%252Fwww-pkulaw-com-s.vpn.ruc.edu.cn%252F')
time.sleep(40)
driver.find_element_by_id('svpn_name').send_keys('')#account
driver.find_element_by_id('svpn_password').send_keys('')#password
driver.find_element_by_id('logButton').click()
time.sleep(60)
def contin(page):
    driver.find_element_by_name('oninput').send_keys(page)
    driver.find_element_by_class_name('jumpBtn').click()
def clean(string):
    return re.sub(r'\s+','',string)
def has_href_no_class(tag):
    return tag.has_attr('href') and not tag.has_attr('class')
###################

##############
href={}
i=1
fopen=open('D:/HUO/data_policy/central_policy_ncov_web.csv','r') ######change according your computer
reader=csv.reader(fopen)
for line in reader:
    if len(line)>0:
        y=str(line).replace("/n",'').replace("/r","").replace("[","").replace("]","").replace("'","")
        if "锘縣" in y:
            y=y.replace("锘縣","h")
            href.update({i:y})
        else:
            href.update({i:y})
        i+=1
print (len(href))
###############

f=open('D:/HUO/data_policy/central_policy_ncov.csv','w',encoding='utf-8-sig') ######change according your computer
writer=csv.writer(f)
writer.writerow(["title","department","number","fabudate","shishidate","shixiao","level","leibie","fulltext"])

error=0
for web in href.values():
    if "void" in web:
        error+=1
    else:
        driver.get(web)
        time.sleep(60)
        title=str(driver.title).replace("-北大法宝V6官网","")
        content=driver.find_element_by_class_name('content').get_attribute('innerHTML')
        soup=BeautifulSoup(content,'html5lib')
        for ul in soup.find_all('ul'):
            lilist=ul.find_all('li')
            department=[]
            number=''
            fabudate=''
            shishidate=''
            shixiao=''
            level=''
            leibie=[]
            for li in lilist:
                if "发布部门" in str(li):
                    dspan=li.find_all('span')
                    for span in dspan:
                        department.append(str(span.attrs['title']).replace("  "," "))
                if "发文字号" in str(li):
                    number=str(li.attrs['title'])
                if "发布日期" in str(li):
                    fabudate=str(li.attrs['title'])
                if "实施日期" in str(li):
                    shishidate=str(li.attrs['title'])
                if "时效性" in str(li):
                    dspan=li.find_all('span')
                    for span in dspan:
                        shixiao=str(span.attrs['title'])
                if "效力级别" in str(li):
                    dspan=li.find_all('span')
                    for span in dspan:
                        level=str(span.attrs['title'])
                if "法规类别" in str(li):
                    dspan=li.find_all('span')
                    for span in dspan:
                        leibie.append(str(span.attrs['title']))
        fulltext=driver.find_element_by_id('divFullText').text
        writer.writerow([title,department,number,fabudate,shishidate,shixiao,level,leibie,clean(fulltext)])
f.close()  
driver.quit()
print (error)
