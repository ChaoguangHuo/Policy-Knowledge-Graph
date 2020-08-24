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
#cur.execute("SELECT data_local.`地区`,data_local.`全文` FROM data_local WHERE `发布日期`<'2020.01.21'")
#cur.execute("SELECT data_local.`地区`,data_local.`全文` FROM data_local WHERE `发布日期`<'2020.03.18' AND `发布日期`>'2020.01.20'")
cur.execute("SELECT data_local.`地区`,data_local.`全文` FROM data_local WHERE `发布日期`<'2020.04.29' AND `发布日期`>'2020.03.17'")
#cur.execute("SELECT data_local.`地区`,data_local.`全文` FROM data_local WHERE `发布日期`>'2020.04.28'")

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

#####导入停用词
print('导入停用词')
file=codecs.open('stopwords_huo.txt','r',encoding='utf-8')
stopword=[]
for word in file:
   stopword.append(clean(word))
"""
#####添加用户自定义字典
dictionary=codecs.open('dictionary_huo.txt','r',encoding='utf-8')
for word in dictionary:
   jieba.add_word(clean(word))
"""
print('导入字典')
#####只使用用户自定义字典
jieba.load_userdict('dictionary_huo.txt')

#####分词-去停用词
def cut_stopword(line):
    text_seg=[]
    seg=jieba.cut(line)
    for i in seg:
        if i not in stopword:
            text_seg.append(i)
    return ' '.join(text_seg)
corpus={}
for x in text:
    corpus.update({x:cut_stopword(text.get(x))})
######输出文件
csvfile=open('province_topic_tfidf_3.csv','w',newline='')
writer=csv.writer(csvfile)
writer.writerow(['province','topic','weight'])

print('开始抽取关键词')
for location in corpus:
    keywords=jieba.analyse.extract_tags(corpus.get(location),topK=25,withWeight=True,allowPOS=())
    for item in keywords:
        writer.writerow([location,item[0],item[1]*1000])

csvfile.close()
"""
# TfidfVectorizer()将文本中的词语转换为文档-词数矩阵
vectorizer = CountVectorizer()  
X = vectorizer.fit_transform(corpus)
word = vectorizer.get_feature_names()
#####计算TF-IDF
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(X)
print('IF-IDF结果：')
print(X.toarray())
"""
"""
#####textrank抽取关键词
textrank=analyse.textrank
for text in corpus:
    keywords=textrank(text, topK=5, withWeight=False, allowPOS=())
    print(keywords)
"""
