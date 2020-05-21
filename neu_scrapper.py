# -*- coding: utf-8 -*-
"""
Created on Wed May 20 15:25:31 2020

@author: HP
"""


import requests
from selenium.webdriver import Chrome
import numpy as np
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import re
import datetime
from bs4 import BeautifulSoup

driver = Chrome()
driver.get('https://web.whatsapp.com/')

#Code to get the list of the contacts in the group :)

driver.find_element_by_xpath('//*[@title="Leaf SongDiscoveryHindi 3"]').click()

sourcer=(driver.page_source).encode('utf-8')
soup=BeautifulSoup(sourcer,features='html.parser')

#CODE FOR GETTING ALL THE CONTACTS IN THE GROUP

p=driver.find_element_by_class_name('_2y17h')
q=p.find_element_by_xpath('div[2]/div[2]/span')

l=q.text
l=l.split(',')
for i in range(len(l)):
    l[i]=l[i].replace(" ","")
    l[i]=l[i][3:]
    
popper=[]
for k,v in names.items():
    if k not in l:
        popper.append(k)
    else:
        pass
for item in popper:
    names.pop(item)    
l[2].replace(" ","")
p=times.get_attribute("title")

# CODE TO COUNTING THE REPLIES(SOMEWHAT COMPLETE)
lol_new=soup.findAll("div",{"class":"Tkt2p"})
for badmsg in lol_new:
    initial_msg=badmsg.get_text()
    print(initial_msg)
    if re.search('identifier',initial_msg,re.IGNORECASE):
        ----------
    else:
        for i in range(len(initial_msg)):
            if initial_msg[i:i+11]=='identifier':
                count+=1
                

#CODE TO GET THE TIME FOR EACH MESSAGE
times=soup.findAll("span",{"class":"_3EFt_"})
for i in range(len(times)):
    print(times[i],lol_new[i])


#CODE FOR GETTING THE MESSAGES
for badmsg in lol_new:
    initial_msg=badmsg.get_text()
    print(initial_msg)

#CODE FOR READING THE MESSAGES INSIDE THE REPLIES
lol_new=soup.findAll("div",{"class":"Tkt2p"})
for badmsg in lol_new:
    initial_msg=badmsg.get_text()
    print(initial_msg)
    if re.search('identifier',initial_msg,re.IGNORECASE):
        ----------
    else:
        for i in range(len(initial_msg)):
            if initial_msg[i:i+11]=='identifier':
                count+=1
                
#CODE FOR CALCULATING THE DAILY ACTIVE USERS
sender_msg_numbers=soup.findAll("span",{"class":"RZ7GO"})
# to find the messages specific to yesterday
start_end=[]
for i in range(len(times)-1):
    if re.search('PM',times[i].get_text()) and re.search('AM',times[i+1].get_text()):
        start_end.append(i)
        print(times[i].get_text(),times[i+1].get_text())
lol_new=lol_new[start_end[0]:start_end[1]]
