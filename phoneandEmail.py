# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 21:16:51 2018

@author: chand
"""

#! python3
#phoneAndEmail.py -find phonenumbers and emailaddresses on clip board.
#step1: creating a Regex for phonenumbers.
import pyperclip
import re

phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?  #area code
        (\s|-|\.)?           #seperator
        (\d{3})              #first 3 digits
        (\s|-|\.)            #seperator
        (\d{4})              #last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))? #extension
        )''',re.VERBOSE)
# step2:Creating regex for email address
# Will not be able to match all possible email addresses 
#will be able to match any typical email address
emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+                 #username
         @                                # @ symbol
          [a-zA-Z0-9.-]+                  # domain name
          (\.[a-zA-Z]{2,4})               # dot something
          )''',re.VERBOSE)
#step 3: Finding all the matches in the clip board.
text = str(pyperclip.paste())
matches = []
phoneNum=''
for groups in phoneRegex.findall(text):
    phoneNum += '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phoneNum += ' x' +groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])
#step 4: joining the matches into a string for copying it to a clip board.
    if len(matches) >0:
        pyperclip.copy('\n'.join(matches))
        print('copied to the clipboard:')
        print('\n'.join(matches))
    else:
        print('no phonenumbers or email address found')
        