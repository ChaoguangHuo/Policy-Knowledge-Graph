"""
import sys
stdi,stdo,stde=sys.stdin,sys.stdout,sys.stderr 
reload(sys)
sys.stdin,sys.stdout,sys.stderr=stdi,stdo,stde
sys.setdefaultencoding('utf-8')#gb18030
"""
import re
import pymysql
import pymysql.cursors
import numpy as np
import csv
import string
import os
import re
import codecs
import jieba
from jieba import analyse
from optparse import OptionParser
import random
import glob
import codecs
from sklearn.feature_extraction.text import TfidfTransformer,CountVectorizer
config={
	  'host':'127.0.0.1',
          'port':3306,
          'user':'root',
          'password':'password',
          'db':'policy_covid19',
          'charset':'utf8mb4',}
connection=pymysql.connect(**config)
cur=connection.cursor()

def clean(string):
    return re.sub(r'\s+','',string)

#####从数据库中读取内容
cur.execute("SELECT data_local.`地区`,data_local.`全文` FROM data_local")
results=cur.fetchall()
print('search out:',len(results))
text={}
for x in results:
    location=x[0]
    content=x[1]
    if location in text:
        text.update({location:text.get(location)+content})
    else:
        text.update({location:str(content)})

print('导入停用词')
#####导入停用词
file=codecs.open('stopwords_huo.txt','r',encoding='utf-8')
stopword=[]
for word in file:
   stopword.append(clean(word))

"""
#####添加用户自定义字典
dictionary=codecs.open(r'D://HUO//paper_policy_covid19//data//dictionary_huo.txt','r',encoding='utf-8')
for word in dictionary:
   jieba.add_word(clean(word))
"""
print('导入字典')
#####只使用用户自定义字典
jieba.load_userdict('dictionary_huo.txt')

#####分词-去停用词
def cut_stopword(line):
    text_seg=[]
    seg=jieba.lcut(line)
    for i in seg:
        if clean(i) not in stopword:
            text_seg.append(clean(i))
    return text_seg

def count(wordsls):
    wcdict={}
    for word in wordsls:
        if len(word)==1:
            continue
        else:
            wcdict[word]=wcdict.get(word,0)+1
    wcls=list(wcdict.items())
    wcls.sort(key=lambda x:x[1],reverse=True)
    return wcls

######输出文件
csvfile=open('province_topic20_pinlv.csv','w',newline='')
writer=csv.writer(csvfile)
writer.writerow(['province','topic','weight'])

print('抽取高频词及其频率')
corpus={}
for x in text:
    y=count(cut_stopword(text.get(x)))
    for i in range(0,20):
        writer.writerow([x,y[i][0],y[i][1]])
        
csvfile.close()

