# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 09:04:28 2018

@author: User
"""

import scrapy
import re
import bleach
import cleaner

class civilforfeiture2015(scrapy.Spider):
    
    civilTextfile = open("civil2015.txt", "r")
    civilFiletext = civilTextfile.read()
    civilTextfile.close()
    #civilDates = re.findall(r"(\d+\-JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC-\d+)\s", civilFiletext)
    civilDates = []
    civilJANDates = re.findall(r"(\d+-JAN-\d+)", civilFiletext)
    civilFEBDates = re.findall(r"(\d+-FEB-\d+)", civilFiletext)
    civilMARDates = re.findall(r"(\d+-MAR-\d+)", civilFiletext)
    civilAPRDates = re.findall(r"(\d+-APR-\d+)", civilFiletext)
    civilMAYDates = re.findall(r"(\d+-MAY-\d+)", civilFiletext)
    civilJUNDates = re.findall(r"(\d+-JUN-\d+)", civilFiletext)
    civilJULDates = re.findall(r"(\d+-JUL-\d+)", civilFiletext)
    civilAUGDates = re.findall(r"(\d+-AUG-\d+)", civilFiletext)
    civilSEPDates = re.findall(r"(\d+-SEP-\d+)", civilFiletext)
    civilOCTDates = re.findall(r"(\d+-OCT-\d+)", civilFiletext)
    civilNOVDates = re.findall(r"(\d+-NOV-\d+)", civilFiletext)
    civilDECDates = re.findall(r"(\d+-DEC-\d+)", civilFiletext)
    
    for i in civilJANDates:
        civilDates.append(i)
    for i in civilFEBDates:
        civilDates.append(i)
    for i in civilMARDates:
        civilDates.append(i)
    for i in civilAPRDates:
        civilDates.append(i)
    for i in civilMAYDates:
        civilDates.append(i)
    for i in civilJUNDates:
        civilDates.append(i)
    for i in civilJULDates:
        civilDates.append(i)
    for i in civilAUGDates:
        civilDates.append(i)
    for i in civilSEPDates:
        civilDates.append(i)
    for i in civilOCTDates:
        civilDates.append(i)
    for i in civilNOVDates:
        civilDates.append(i)
    for i in civilDECDates:
        civilDates.append(i)
    

    civilCaseNum = re.findall(r"\s(\d+[A-Z]*CV-\d+-\d+)\s", civilFiletext)
    
    #civilTuple = list(zip(civilDates, civilCaseNum))# for i in range(len(civilCaseNum))]
    
    
    

    custom_settings = {'AUTOTHROTTLE_ENABLED' : 'True',
                       'AUTOTHROTTLE_START_DELAY' : '5.0',
                       'AUTOTHROTTLE_TARGET_CONCURRENCY': '0.5',
                       'HTTPCACHE_ENABLED': 'True',
                       'HTTPCACHE_EXPIRATION_SECS': '0',
                       'HTTPCACHE_DIR': 'httpcache',
                       'HTTPCACHE_STORAGE': 'scrapy.extensions.httpcache.FilesystemCacheStorage',                       
                       'USER_AGENT':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                       'COOKIES_ENABLED':'False',
                       'FEED_EXPORT_ENCODING' : 'utf-8',
                       'CONCURRENT_REQUESTS':'1'}
    name = "civilforfeiture2015 spider"
    start_urls = []
    i=0
    while i < len(civilCaseNum):
        start_urls.append('https://caseinfo.arcourts.gov/cconnect/PROD/public/ck_public_qry_doct.cp_dktrpt_docket_report?backto=P&case_id='+ civilCaseNum[i] +'&citation_no=&begin_date=&end_date=')#("https://caseinfo.arcourts.gov/cconnect/PROD/public/ck_public_qry_doct.cp_dktrpt_frames?backto=P&case_id="+ civilCaseNum[i] +"&begin_date=&end_date=" )
        i+= 1
        
    def parse(self, response):
        
        caseInfo = response.css('body > font').extract_first() #response.css('table').extract_first() xpath('//a[@name="description"]').
        if caseInfo:
            caseInfo = caseInfo.split('<a name=')
            civil_case = {}
            
            
            #if caseInfo.find('<table>')
            caseDescriptionDict = {}
            caseDescription = bleach.clean(caseInfo[2], tags=[], attributes={}, styles=[], strip=True)
            caseDescription = caseDescription.replace('\n','')
            caseDescription = caseDescription.replace('\xa0','')

            
            caseDescription = caseDescription.split(':')
            caseDescription = caseDescription[1::]
            caseDescription[0] = caseDescription[0].replace('Filing Date','')
            caseDescription[1] = caseDescription[1].replace('Court','')
            caseDescription[2] = caseDescription[2].replace('Location','')
            caseDescription[3] = caseDescription[3].replace('Type','')
            caseDescription[4] = caseDescription[4].replace('Status','')
            caseDescription[5] = caseDescription[5].replace('Images','')
            caseDescriptionDict['Case ID'] = caseDescription[0]
            caseDescriptionDict['Filing Date'] = caseDescription[1]
            caseDescriptionDict['Court'] = caseDescription[2]
            caseDescriptionDict['Location'] = caseDescription[3]
            caseDescriptionDict['Type'] = caseDescription[4]
            caseDescriptionDict['Status'] = caseDescription[5]
            caseDescriptionDict['Images'] = caseDescription[6]

            
            
            caseEventSchedule = bleach.clean(caseInfo[3], tags=[], attributes={}, styles=[], strip=True)
            caseEventSchedule = caseEventSchedule.replace('\n','')
            caseEventSchedule = caseEventSchedule.replace('\xa0','')
            caseEventSchedule = caseEventSchedule.split('Event Schedule')
            caseEventSchedule = caseEventSchedule[-1]
            
            
            casePartiesInvolved = caseInfo[4]
            casePartiesInvolved = casePartiesInvolved.replace('\n','')
            casePartiesInvolved = casePartiesInvolved.replace('\xa0','')
            casePartiesInvolved = casePartiesInvolved.split('</tr>')
            partyTitles = casePartiesInvolved[0]
            partyTitles = partyTitles.split('</th>')
            partyTitles = [bleach.clean(x, tags=[], attributes={}, styles=[], strip=True) for x in partyTitles]
            partyTitles[0] = 'Seq #'
            #print('first ' + str(len(casePartiesInvolved)))
            #casePartiesInvolved = [casePartiesInvolved[0], casePartiesInvolved[-1]]
            casePartiesInvolved = casePartiesInvolved[1:-1]
            #del casePartiesInvolved[2::3]
            #print('thrird ' + str(len(casePartiesInvolved)))

            
            
            count = 1
            parties = {}
            list_of_parties = []
            
            while count <= len(casePartiesInvolved):
                
                if count%3 == 1:
                    seperateParties = casePartiesInvolved[count-1]
                    seperateParties_list = seperateParties.split('</td>')
                    
                    
                    
                    
                    parties[partyTitles[0]] = bleach.clean(seperateParties_list[0], tags=[], attributes={}, styles=[], strip=True)
                    parties[partyTitles[1]] = bleach.clean(seperateParties_list[1], tags=[], attributes={}, styles=[], strip=True)
                    parties[partyTitles[2]] = bleach.clean(seperateParties_list[2], tags=[], attributes={}, styles=[], strip=True)
                    parties[partyTitles[3]] = bleach.clean(seperateParties_list[3], tags=[], attributes={}, styles=[], strip=True)
                    parties[partyTitles[4]] = bleach.clean(seperateParties_list[4], tags=[], attributes={}, styles=[], strip=True)
                    parties[partyTitles[5]] = bleach.clean(seperateParties_list[5], tags=[], attributes={}, styles=[], strip=True)
                    
                    
                    
                elif count%3 == 2:
                    seperateParties = casePartiesInvolved[count-1]
                    seperateParties_list = seperateParties.split('</td>')
                    alias = seperateParties_list[-2]
                    alias = bleach.clean(alias, tags=[], attributes={}, styles=[], strip=True)
                    parties['Alias'] = alias
                    
                
                else:
                    list_of_parties.append(parties)
                    parties = {}
                    
                
                
                count = count + 1

            
            
            #casePartiesInvolved = bleach.clean(caseInfo[4], tags=[], attributes={}, styles=[], strip=True)

#            caseDescription = [x.replace('\n','') for x in caseDescription]
#            caseEventSchedule = [x.replace('\n','') for x in caseEventSchedule]
#            
#            caseDescription = [x.replace('\xa0','') for x in caseDescription]         
#            caseEventSchedule = [x.replace('\xa0','') for x in caseEventSchedule]
             #•
            
            civil_case['URL Address'] = response.url
            civil_case['Description'] = caseDescriptionDict            
            civil_case['Event Schedule'] = caseEventSchedule
            civil_case['Parties Involved'] = list_of_parties

            
            
            yield civil_case