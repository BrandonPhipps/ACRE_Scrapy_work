# -*- coding: utf-8 -*-
import re
import bleach

def strip_amp(string):
  return string.replace("&amp;", "&")

def hours_and_mins(string,hr_or_hour):
    hours_search = re.search(r"(\d+)\s*(:?"+ hr_or_hour + ")", string)
    minutes_search = re.search(r"(\d+)\s*(:?min)", string)

    if minutes_search:
        minutes1 = minutes_search.group(1)
        minutes = int(minutes1)

    else:
        minutes = 0
        
    if hours_search:
        hours1 = hours_search.group(1)
        hours = (int(hours1)*60)
    else:
        hours = 0
        
    return (hours+minutes)
                            
def list_to_string(list_of_stuff):
    new_list = []
    new_list = list_of_stuff
    
    if (len(new_list) > 1):        
        
        new_list = [" ".join(x.split()) for x in new_list]#[x.replace("\n", ' ') for x in new_list]
        stripCR_string = "\n".join(new_list)
        stripCR_string =bleach.clean(stripCR_string, tags=[], attributes={}, styles=[], strip=True)                    
        list_of_stuff_string = stripCR_string.replace("&amp;", "&") 
        list_of_stuff_string = list_of_stuff_string.replace("\t", '')
        list_of_stuff_string = list_of_stuff_string.replace(" \n ", '\n')
        list_of_stuff_string = list_of_stuff_string.replace("\n ", '\n')
        list_of_stuff_string = list_of_stuff_string.replace(" \n", '\n')
        list_of_stuff_string = list_of_stuff_string.replace("\n\n", '\n')
        list_of_stuff_string = list_of_stuff_string.strip()  
        return list_of_stuff_string
    elif (len(new_list) == 1):

        list_of_stuff_string = bleach.clean(new_list[0], tags=[], attributes={}, styles=[], strip=True)   
        list_of_stuff_string = list_of_stuff_string.replace("&amp;", "&")
        list_of_stuff_string = " ".join(list_of_stuff_string.split())
        return list_of_stuff_string
    else:
        return None


def title(string):
    name = bleach.clean(string, tags=[], attributes={}, styles=[], strip=True)
    name = strip_amp(name)
    name  = re.sub('\{(.*?)\}', '', name)
    name  = re.sub('\((.*?)\)', '', name)
    name= name.lower()
    name_list = name.split() 
    name_list = [x.capitalize() for x in name_list]
    name  = " ".join(name_list)
    return name.strip()

def tag_list(list_of_tags, name_of_site):
    tags = []
    for x in list_of_tags:
        clean_tag = bleach.clean(x, tags=[], attributes={}, styles=[], strip=True)
        clean_tag = clean_tag.replace("&amp;", '&')
        clean_tag = clean_tag.lower()
        match = re.search("([^.]*recipe[^.]*)", clean_tag)
        match_2 = re.search("([^.]*comment[^.]*)", clean_tag)
        if not match and not match_2:
            tags.append(clean_tag) 
    
    tags.append(name_of_site)        
    unique_tags = []                
    [unique_tags.append(item) for item in tags if item not in unique_tags]
    return ",".join(unique_tags)

def time_list_returns_list(list_of_all_times, hr_or_hour,):
    prep_subzero_cook_subone_total_subtwo = [0,0,0]
    if list_of_all_times:
        all_times_list = []        
        for time in list_of_all_times:  
            time_HTML = time
            time_strip = bleach.clean(time_HTML, tags=[], attributes={}, styles=[], strip=True)
            all_times_list.append(time_strip) 
        

        i = 0
        prep_time = 0
        cook_time = 0
        while (i < len(all_times_list)):                               
        
            
            hours_search = re.search(r"(\d+)\s*(:?" + hr_or_hour +")", all_times_list[i])
            minutes_search = re.search(r"(\d+)\s*(:?min)", all_times_list[i])

            if minutes_search:
                minutes1 = minutes_search.group(1)
                minutes = int(minutes1)

            else:
                minutes = 0
                
            if hours_search:
                hours1 = hours_search.group(1)
                hours = (int(hours1)*60)
            else:
                hours = 0
                
            match = re.search("prep\s*time[:]?\s*(\d+)", all_times_list[i].lower())                    
            if match:
                prep_time = minutes + hours               
                prep_subzero_cook_subone_total_subtwo[0] = prep_time
                
            match = re.search("cook\s*time[:]?\s*(\d+)", all_times_list[i].lower())
            if match:
                cook_time = minutes + hours
                prep_subzero_cook_subone_total_subtwo[1] = cook_time                     

            i+=1
            
        total_time = prep_time + cook_time
        prep_subzero_cook_subone_total_subtwo[2] = total_time
        
    return prep_subzero_cook_subone_total_subtwo

def nutrition_label_return_dict(list_from_table):
    nutrition_HMTL = list_from_table
    nutrition_elements = []  
    nutrition = {}
    nutritionRegEx = "(\d+)"
    for nutrition_in_page in nutrition_HMTL:
        nutrition_Extract = nutrition_in_page
        nutrition_Extract = bleach.clean(nutrition_Extract, tags=[], attributes={}, styles=[], strip=True)
        nutrition_elements.append(nutrition_Extract)
        
    nutrients = "".join(nutrition_elements)
    
                    
        
    match = re.search(r"calories[:]?\s*"+nutritionRegEx, nutrients.lower())
    if match:                      
        nutrition['calories'] = match.group(1)
        
    
    match = re.search(r"total\sfat[:]?\s*"+nutritionRegEx, nutrients.lower())                    
    if match:
        nutrition['totalfat'] = match.group(1)
        
    match = re.search(r"saturated\sfat[:]?\s*"+nutritionRegEx, nutrients.lower())                    
    if match:
        nutrition['satfat'] = match.group(1)
        
    match = re.search(r"cholesterol[:]?\s*"+nutritionRegEx, nutrients.lower())                    
    if match:
        nutrition['cholesterol'] = match.group(1)
        
    match = re.search(r"sodium[:]?\s*"+nutritionRegEx, nutrients.lower())                    
    if match:
        nutrition['sodium'] = match.group(1)
        
    match = re.search(r"potassium[:]?\s*"+nutritionRegEx, nutrients.lower())                    
    if match:
        nutrition['potassium'] = match.group(1)
                            
        
    match = re.search(r"total\scarbohydrates[:]?\s*"+nutritionRegEx, nutrients.lower())
    if match:
        nutrition['carbo'] = match.group(1)
        
    match = re.search(r"fiber[:]?\s*"+nutritionRegEx, nutrients.lower())                    
    if match:
        nutrition['fiber'] = match.group(1)
        
    match = re.search(r"sugar[:]?\s*"+nutritionRegEx, nutrients.lower())                    
    if match:
        nutrition['sugar'] = match.group(1)
        

    match = re.search(r"protein[:]?\s*"+nutritionRegEx, nutrients.lower())
    if match:
        nutrition['protein'] = match.group(1)
    return nutrition


def avatar_using_re(body_list, base_url, image_type_string):
    
    avatar = re.search(base_url + "(.*?)" + image_type_string, body_list)    
    if avatar:
        avatar_url = (base_url + avatar.group(1) + image_type_string)
        return avatar_url
    else:
        return None
    

def html_to_split_returns_list(list_of_html, pattern_to_split):
    string_to_split = "".join(list_of_html)
    new_list = string_to_split.split(pattern_to_split)
    return new_list
    
def split_list_into_sections_return_string(list_of_html, pattern_to_split, pattern2_to_split, replace_this_word, join_list_by):
    new_list = html_to_split_returns_list(list_of_html, pattern_to_split)
    last_list = ''
    if new_list:
        newer_list = []
        newer_list2= []
        i = 0
        
        while (i < len(new_list)):                                  
            newer_list.append(html_to_split_returns_list(new_list[i], pattern2_to_split))                                 
            i+=1
            
        i=0
        while (i < len(newer_list)):                    
            newer_list2.append(list_to_string(newer_list[i]))
            i+=1
            
        if newer_list2:
            last_list = "\n".join(newer_list2)
            string = last_list.replace(replace_this_word,'') 
            return string.strip()
    else:
        return None
    
def clean_single_xpath_element(xpath_element):
    new_string = bleach.clean(xpath_element, tags=[], attributes={}, styles=[], strip=True)
    new_string = strip_amp(new_string)
    new_string = " ".join(str(new_string).split())
    return new_string.strip()
    