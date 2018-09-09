# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 10:11:10 2018

@author: User
"""
import re
import scrapy
import bleach
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
    start_urls =['https://caseinfo.arcourts.gov/cconnect/PROD/public/ck_public_qry_cpty.cp_personcase_srch_details?backto=P&soundex_ind=&aka_ind=&partial_ind=&last_name=VASQUEZ&first_name=STEPHANIE&middle_name=&dl_number=&dob=&begin_date=&end_date=&judge_id=&judge_status=&case_type=ALL&person_type=ALL&county_code=&locn_code=ALL&id_code=&PageNo=1']
    caseNumCV = '43CV-15-469'
    caseNumCR = ''
    def parse(self, response):
        html = response.css('body > font').extract_first()
        
        if html:
            search = {}
            tables = html
#            info_needed = tables.split('</HEAD>')
#            tables = info_needed[1]
            case_list = tables.split('</tr>')
            case_list = case_list[2:-2]
            
            #string = '****DELIMITER****'.join(case_list)
            case_counter = 0
            tester = False
            subOfCV = -2
            while case_counter < len(case_list):
                new_case = case_list[case_counter].split('<td>')
                count = 0
                while count < len(new_case):
                    matchCR = re.search(r">(\d+[A-Z]*CR-\d+-\d+)<", new_case[count])
                    matchCV = re.search(r">(\d+[A-Z]*CV-\d+-\d+)<", new_case[count])
                    if matchCV:               
                        if self.caseNumCV == matchCV.group(1):
                            tester = True
                            subOfCV = case_counter
                            count += 1
                            break
                    
                    if (tester == True) and (case_counter == (subOfCV+1)):
                        if matchCR:
                            self.caseNumCR = matchCR.group(1)
                            search['Civil'] = self.caseNumCV
                            search['Criminal'] = self.caseNumCR
                            yield(search)
                    
            
                    
                    
                    
                    
                    count += 1
                case_counter += 1
                    
                    
#            case_list = [bleach.clean(x, tags=[], attributes={}, styles=[], strip=True) for x in case_list]
#                
#            search['string'] = case_list
            yield search
            
        