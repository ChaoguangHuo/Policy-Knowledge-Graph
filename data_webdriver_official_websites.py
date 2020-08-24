#coding=utf-8
import time
import csv
import codecs
import os
import re
import urllib
from selenium import webdriver
driver=webdriver.Chrome('C:\Python36\webdriver\chromedriver_win32.exe')
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException



def find_website(web):
    driver.get(web)
    
def nextpage():
    try: driver.find_element_by_link_text('下一页').click()
    except NoSuchElementException:
        try:driver.find_element_by_class_name('btn_page').click()
        except NoSuchElementException:
            try:driver.find_element_by_class_name('jumpBtn').click()
            except NoSuchElementException:
                print('no_next_page')
def clean(string):
    return re.sub(r'\s+','',string)
def has_href_no_class(tag):
    return tag.has_attr('href') and not tag.has_attr('class')

driver.get('')
###################
fopen=open('D:/HUO/data_policy/official_web.csv','r') ######change according your computer
reader=csv.reader(fopen)
for line in reader:
    if len(line)>0:

try:

    
except NoSuchElementException:
    


"""
vpn_login()
i=1
href={}
for page in range(1,sumpage+1):
    if i%5==0:
        time.sleep(60)
        vpn_login()
        contin(page)
    listwrap=driver.find_element_by_class_name('list-wrap').get_attribute('innerHTML')
    soup=BeautifulSoup(listwrap,'html5lib')
    for h4 in soup.find_all('h4'):
        for hhref in h4.find_all(has_href_no_class):
            href.update({i-1:str(homepage)+str(hhref.attrs['href'])})
            i+=1
    driver.find_element_by_link_text('下一页').click()
    time.sleep(60)
    if i%30==0:
        print (i)

print (len(href))
fweb=open('D:/HUO/data_policy/central_policy_ncov_web.csv','w',encoding='utf-8-sig') ######change according your computer
writer=csv.writer(fweb)
for x in href.values():
    writer.writerow([x])
fweb.close()


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
j=0
vpn_login()
for web in href.values():
    j+=1
    if j%100==0:
        print(j)
        vpn_login()
        time.sleep(120)
        if "void" in web:
            error+=1
        else:
            driver.get(web)
            time.sleep(30)
            title=str(driver.title).replace("-","")
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
    else:
        if "void" in web:
            error+=1
        else:
            driver.get(web)
            time.sleep(30)
            title=str(driver.title).replace("-","")
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
"""
"""
    title=driver.find_element_by_id('divFullText').text

    print(title)
        
    drive.back()
    time.sleep(10)
    soup=BeautifulSoup(listwrap,'html5lib')
    for h4 in soup.find_all('h4'):
     
        for hhref in h4.find_all(has_href_no_class):
            href.update({i:str(hhref.attrs['href'])})
            i+=1
            
            driver.back()         
    driver.find_element_by_link_text('下一页').click()
print(len(href))
for web in href.values():
    driver.get(web)
    time.sleep(25)

driver.quit()    
listwrap=driver.find_element_by_class_name('list-wrap').get_attribute('innerHTML')


"""
