# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 17:49:39 2018

@author: User
"""
import re
import json
#civilTextfile = open("civil2015.txt", "r")
#civilFiletext = civilTextfile.readlines()
#civilTextfile.close()
with open('civil2015.txt') as f:
    content = f.readlines()


count = 0


allCaseInfo ={}
for line in content:
    dateAndCaseNum = []
    names_1 = re.search(r"\s+V\s+(.*?)\s+PROPERTY+", line)
    names_2 = re.search(r"\s+VS\s+(.*?)\s+PROPERTY+", line)
    names_3 = re.search(r"\s+ARKANSAS\s+(.*?)\s+PROPERTY+", line)
    names_4 = re.search(r"\s+AR\s+(.*?)\s+PROPERTY+", line)
    names_5 = re.search(r"\s+STATE\s+(.*?)\s+PROPERTY+", line)
    names_6 = re.search(r"(:?\s\d+[A-Z]*CV-\d+-\d+)+\s+(.*?)\s+PROPERTY+", line)
    
    civilCaseNum = re.search(r"\s(\d+[A-Z]*CV-\d+-\d+)\s", line)
    
    civilJANDates = re.search(r"(\d+-JAN-\d+)", line)
    civilFEBDates = re.search(r"(\d+-FEB-\d+)", line)
    civilMARDates = re.search(r"(\d+-MAR-\d+)", line)
    civilAPRDates = re.search(r"(\d+-APR-\d+)", line)
    civilMAYDates = re.search(r"(\d+-MAY-\d+)", line)
    civilJUNDates = re.search(r"(\d+-JUN-\d+)", line)
    civilJULDates = re.search(r"(\d+-JUL-\d+)", line)
    civilAUGDates = re.search(r"(\d+-AUG-\d+)", line)
    civilSEPDates = re.search(r"(\d+-SEP-\d+)", line)
    civilOCTDates = re.search(r"(\d+-OCT-\d+)", line)
    civilNOVDates = re.search(r"(\d+-NOV-\d+)", line)
    civilDECDates = re.search(r"(\d+-DEC-\d+)", line)
    dateAndCaseNum.append(civilCaseNum.group(1))
    
    
    if civilJANDates:
        dateAndCaseNum.append(civilJANDates.group(1))
        if names_1:
            allCaseInfo[names_1.group(1)] = dateAndCaseNum
            
        elif names_2:
            allCaseInfo[names_2.group(1)] = dateAndCaseNum
            
        elif names_3:
            allCaseInfo[names_3.group(1)] = dateAndCaseNum
            
        elif names_4:
            allCaseInfo[names_4.group(1)] = dateAndCaseNum
            
        elif names_5:
            allCaseInfo[names_5.group(1)] = dateAndCaseNum
            
        elif names_6:
            allCaseInfo[names_6.group(1)] = dateAndCaseNum
            
    elif civilFEBDates:
        dateAndCaseNum.append(civilFEBDates.group(1))
        if names_1:
            allCaseInfo[names_1.group(1)] = dateAndCaseNum
            
        elif names_2:
            allCaseInfo[names_2.group(1)] = dateAndCaseNum
            
        elif names_3:
            allCaseInfo[names_3.group(1)] = dateAndCaseNum
            
        elif names_4:
            allCaseInfo[names_4.group(1)] = dateAndCaseNum
            
        elif names_5:
            allCaseInfo[names_5.group(1)] = dateAndCaseNum
        
        elif names_6:
            allCaseInfo[names_6.group(1)] = dateAndCaseNum
    
    elif civilMARDates:
        dateAndCaseNum.append(civilMARDates.group(1))
        if names_1:
            allCaseInfo[names_1.group(1)] = dateAndCaseNum
            
        elif names_2:
            allCaseInfo[names_2.group(1)] = dateAndCaseNum
            
        elif names_3:
            allCaseInfo[names_3.group(1)] = dateAndCaseNum
            
        elif names_4:
            allCaseInfo[names_4.group(1)] = dateAndCaseNum
            
        elif names_5:
            allCaseInfo[names_5.group(1)] = dateAndCaseNum
            
            
        elif names_6:
            allCaseInfo[names_6.group(1)] = dateAndCaseNum
    elif civilAPRDates:
        dateAndCaseNum.append(civilAPRDates.group(1))
        if names_1:
            allCaseInfo[names_1.group(1)] = dateAndCaseNum
            
        elif names_2:
            allCaseInfo[names_2.group(1)] = dateAndCaseNum
            
        elif names_3:
            allCaseInfo[names_3.group(1)] = dateAndCaseNum
            
        elif names_4:
            allCaseInfo[names_4.group(1)] = dateAndCaseNum
            
        elif names_5:
            allCaseInfo[names_5.group(1)] = dateAndCaseNum
            
        elif names_6:
            allCaseInfo[names_6.group(1)] = dateAndCaseNum
                    
    elif civilMAYDates:
        dateAndCaseNum.append(civilMAYDates.group(1))
        if names_1:
            allCaseInfo[names_1.group(1)] = dateAndCaseNum
            
        elif names_2:
            allCaseInfo[names_2.group(1)] = dateAndCaseNum
            
        elif names_3:
            allCaseInfo[names_3.group(1)] = dateAndCaseNum
            
        elif names_4:
            allCaseInfo[names_4.group(1)] = dateAndCaseNum
            
        elif names_5:
            allCaseInfo[names_5.group(1)] = dateAndCaseNum
            
            
        elif names_6:
            allCaseInfo[names_6.group(1)] = dateAndCaseNum
            
    elif civilJUNDates:
        dateAndCaseNum.append(civilJUNDates.group(1))
        if names_1:
            allCaseInfo[names_1.group(1)] = dateAndCaseNum
            
        elif names_2:
            allCaseInfo[names_2.group(1)] = dateAndCaseNum
            
        elif names_3:
            allCaseInfo[names_3.group(1)] = dateAndCaseNum
            
        elif names_4:
            allCaseInfo[names_4.group(1)] = dateAndCaseNum
            
        elif names_5:
            allCaseInfo[names_5.group(1)] = dateAndCaseNum
            
        elif names_6:
            allCaseInfo[names_6.group(1)] = dateAndCaseNum
                    
    elif civilJULDates:
        dateAndCaseNum.append(civilJULDates.group(1))
        if names_1:
            allCaseInfo[names_1.group(1)] = dateAndCaseNum
            
        elif names_2:
            allCaseInfo[names_2.group(1)] = dateAndCaseNum
            
        elif names_3:
            allCaseInfo[names_3.group(1)] = dateAndCaseNum
            
        elif names_4:
            allCaseInfo[names_4.group(1)] = dateAndCaseNum
            
        elif names_5:
            allCaseInfo[names_5.group(1)] = dateAndCaseNum
            
        elif names_6:
            allCaseInfo[names_6.group(1)] = dateAndCaseNum
                    
    elif civilAUGDates:
        dateAndCaseNum.append(civilAUGDates.group(1))
        if names_1:
            allCaseInfo[names_1.group(1)] = dateAndCaseNum
            
        elif names_2:
            allCaseInfo[names_2.group(1)] = dateAndCaseNum
            
        elif names_3:
            allCaseInfo[names_3.group(1)] = dateAndCaseNum
            
        elif names_4:
            allCaseInfo[names_4.group(1)] = dateAndCaseNum
            
        elif names_5:
            allCaseInfo[names_5.group(1)] = dateAndCaseNum
            
            
        elif names_6:
            allCaseInfo[names_6.group(1)] = dateAndCaseNum
            
    elif civilSEPDates:
        dateAndCaseNum.append(civilSEPDates.group(1))
        if names_1:
            allCaseInfo[names_1.group(1)] = dateAndCaseNum
            
        elif names_2:
            allCaseInfo[names_2.group(1)] = dateAndCaseNum
            
        elif names_3:
            allCaseInfo[names_3.group(1)] = dateAndCaseNum
            
        elif names_4:
            allCaseInfo[names_4.group(1)] = dateAndCaseNum
            
        elif names_5:
            allCaseInfo[names_5.group(1)] = dateAndCaseNum
            
        elif names_6:
            allCaseInfo[names_6.group(1)] = dateAndCaseNum
                    
    elif civilOCTDates:
        dateAndCaseNum.append(civilOCTDates.group(1))
        if names_1:
            allCaseInfo[names_1.group(1)] = dateAndCaseNum
            
        elif names_2:
            allCaseInfo[names_2.group(1)] = dateAndCaseNum
            
        elif names_3:
            allCaseInfo[names_3.group(1)] = dateAndCaseNum
            
        elif names_4:
            allCaseInfo[names_4.group(1)] = dateAndCaseNum
            
        elif names_5:
            allCaseInfo[names_5.group(1)] = dateAndCaseNum
            
        elif names_6:
            allCaseInfo[names_6.group(1)] = dateAndCaseNum
                    
    elif civilNOVDates:
        dateAndCaseNum.append(civilNOVDates.group(1))
        if names_1:
            allCaseInfo[names_1.group(1)] = dateAndCaseNum
            
        elif names_2:
            allCaseInfo[names_2.group(1)] = dateAndCaseNum
            
        elif names_3:
            allCaseInfo[names_3.group(1)] = dateAndCaseNum
            
        elif names_4:
            allCaseInfo[names_4.group(1)] = dateAndCaseNum
            
        elif names_5:
            allCaseInfo[names_5.group(1)] = dateAndCaseNum
            
        elif names_6:
            allCaseInfo[names_6.group(1)] = dateAndCaseNum
                    
    elif civilDECDates:
        dateAndCaseNum.append(civilDECDates.group(1))
        if names_1:
            allCaseInfo[names_1.group(1)] = dateAndCaseNum
            
        elif names_2:
            allCaseInfo[names_2.group(1)] = dateAndCaseNum
            
        elif names_3:
            allCaseInfo[names_3.group(1)] = dateAndCaseNum
            
        elif names_4:
            allCaseInfo[names_4.group(1)] = dateAndCaseNum
            
        elif names_5:
            allCaseInfo[names_5.group(1)] = dateAndCaseNum

        elif names_6:
            allCaseInfo[names_6.group(1)] = dateAndCaseNum
            
    count += 1

            

#for key, value in allCaseInfo.items() :
#    print (key, value)

print('total count = ' + str(len(allCaseInfo)))

with open('RE_tester_text.json', 'w') as file:
     file.write(json.dumps(allCaseInfo))