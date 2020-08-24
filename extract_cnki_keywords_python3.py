import os
import re
import codecs
import jieba
import random
import glob
import codecs
import csv

rootpath='D:\HUO\paper_policy_covid19\data\ciki_data'
os.chdir(rootpath)
filelist=os.listdir(rootpath)

csvfile=open('D:\HUO\paper_policy_covid19\data\cnki_dictionary.txt','w')
#writer=csv.writer(csvfile)
#writer.writerow(['KEYWORD'])

for filename in filelist:
    print(filename)
    with codecs.open(filename,"r",encoding='utf-8') as file:
        for line in file:
            if str(line).startswith("Keyword-关键词:"):
                aa=str(line).replace("Keyword-关键词:","").replace(" ","").replace('\n','')
                list=aa.split(';;')
                print (list)
                for x in list:
                    csvfile.write(str(x)+'\n')
                    #writer.writerow([x])
csvfile.close()
                
"""
            if str(line).startswith("UT WOS:"):
                i+=1
                b=str(line).replace("UT WOS:","").replace("\n","")
                if len(list):
                    for y in range(0,number):
                        writer.writerow([b,list[y]])
                list=[]
print i
"""
#a=re.sub('\\(.*?\\)', '', aa)
