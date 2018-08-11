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
    
    civilHash = {}
    

#        
    
#    for x in civilDates:
#        civilHash[x] = civilCaseNum
#        
#    for k,v in civilHash.items():
#        print (k,v)
    