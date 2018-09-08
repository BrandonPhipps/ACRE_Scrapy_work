# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 10:11:10 2018

@author: User
"""
import re
import scrapy

class testing(scrapy.Spider):
    custom_settings = {'AUTOTHROTTLE_ENABLED' : 'True',
                       'DOWNLOAD_DELAY' : '.25',
                       'AUTOTHROTTLE_TARGET_CONCURRENCY':'1.0',
                       'HTTPCACHE_ENABLED': 'True',
                       'HTTPCACHE_EXPIRATION_SECS': '0',
                       'HTTPCACHE_DIR': 'httpcache',
                       'HTTPCACHE_STORAGE': 'scrapy.extensions.httpcache.FilesystemCacheStorage',                       
                       'USER_AGENT':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                       'COOKIES_ENABLED':'False',
                       'FEED_EXPORT_ENCODING' : 'utf-8',
                       'CONCURRENT_REQUESTS':'1'}
    
    name = "namesearch spider"
    start_url =['view-source:https://caseinfo.arcourts.gov/cconnect/PROD/public/ck_public_qry_cpty.cp_personcase_srch_details?backto=P&soundex_ind=&aka_ind=&partial_ind=&last_name=VASQUEZ&first_name=STEPHANIE&middle_name=&dl_number=&dob=&begin_date=&end_date=&judge_id=&judge_status=&case_type=ALL&person_type=ALL&county_code=&locn_code=ALL&id_code=&PageNo=1']
    
    def parse(self, response):
        html = response.css('HTML').extract_first()
        if html:
            new_html = html[0]
            info_needed = new_html.split('</HEAD>')
            tables = info_needed[1]
            case_list = tables.split('<TR ALIGN')
            case_list = case_list[1:-1]
            
            
        