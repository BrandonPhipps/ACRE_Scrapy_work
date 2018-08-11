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
        start_urls.append("https://caseinfo.arcourts.gov/cconnect/PROD/public/ck_public_qry_doct.cp_dktrpt_frames?backto=P&case_id="+ civilCaseNum[i] +"&begin_date=&end_date=" )
        i+= 1
        
    def parse(self, response):
        
        caseDescription = response.xpath('//a[@name="description"]').extract_first()
        if caseDescription:
            civil_case = {}
            case_Description = bleach.clean(caseDescription, tags=[], attributes={}, styles=[], strip=True)
            civil_case['description'] = case_Description
            yield civil_case