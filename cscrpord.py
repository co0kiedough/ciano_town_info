import pandas as pd
import requests
import glob
import re
import csv
from bs4 import BeautifulSoup as bsm
from googlesearch import search
class gsearch:
    
    def __init__(self):
        self.csvf = glob.glob('njto*.csv')
        self.urllist = []
        self.csvd = {}
        self.ocsv = open(self.csvf[0], 'r', newline='', encoding='utf8')
        self.rcsv = csv.DictReader(self.ocsv)
        i = 0
        for row in self.rcsv:
            self.csvd[i] = row
            i+=1
        
        
        
    def urlq(self):
        tlist = []
        csvd = self.csvd
        for row in csvd:
            # print(csvd[row])
            # print(csvd[row]['Township'])
            tlist.append((csvd[row]['City'], 'https://www.google.com/search?q=filetype:pdf ' +'Township of '+ str(csvd[row]['City']) + ' New Jersey recreational marijuana ordinance'))
        return tlist
    
    def resplinks(self, list_of_towns):
        townlinks = {}
        glinks = {}
        glist = []
        curlist=[]
        li = list_of_towns
        for town in li:
            q = str(town[1])
            glist=[]
            
            for l in search(q, num=1, stop=1,pause=2):
                print(q)
                
                if l not in curlist:
                    if 'http' in str(l):
                        print(l)
                        glist.append(l)
                else:
                    if l == 'https://www.nj.gov/dca/divisions/lps/gps/pl_zoning.html':
                        return glinks
                    foo='bar'
                curlist.append(l)
            glinks[town[0]] = {'town':town[0], 'links':glist}
        return glinks
                
        # for town in li:
        #     
        #     
        #     resp = requests.get(town[1])
        #     soup = bsm(resp.content, features='lxml')
        #     for link in  soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
        #         lr = re.split(":(?=http)",link["href"].replace("/url?q=",""))
        #         lr = lr[0].split('&sa=')[0]
        #         print(lr)
        #         # curlist.append(re.split(":(?=http)",link["href"].replace("/url?q=","")))
        #         if not lr in curlist:
        #             curlist.append(lr)
        #     townlinks[town[0]] = {'town':town[0], 'links':curlist}
        #     curlist = []
        # return townlinks
    
    def scrapepage(self, towndict):
        emails = {}
        for t in towndict:
            # link = towndict[t]['links'][0]
            link = towndict[t]['links'][0]
            # for link in towndict[t]['links']:
            print(link)
            
            try:
                #code
                page = requests.get(link)
                print(page.text)
                # print(page.text)
                # psoup = bsm(page.content)
                # new_emails = re.search(r"((mailto\:)?\w{1,}\@\w{1,}\.\w{1,})+", page.text, re.I)
                # emails[t] = {'emails':new_emails}
            except Exception:
                emails[t] = {'emails':''}

        # return emails
            
    def saveemails(self, emaild):
        # print(emaild)
        for town in emaild:
            
            em = emaild[town]['emails']
            # print(em)
            if em == None or em=='None' or em =='':
                emaild[town]['email_address'] = ''
            else:
                print(em)
                if 'href' in str(em.group(0)):
                    emg = str(em.group(0)).split('href="')[1]
                    emg = emg.split('">')[0]
                    if 'mailto' in emg:
                        emg = emg.split('to:')[1]
                        
                    emaild[town]['email_address'] = emg
                else:
                    ema = em.group(0)
                    if 'mailto:' in ema:
                        ema = ema.split('to:')[1]
                    emaild[town]['email_address'] = ema
        outd = emaild
        return outd
                
            
        
        # df = pd.DataFrame(emailset, columns=['Email'])
        # f = open('email.csv', 'r', newline='')
        # df.to_csv(f, index=False)
        # fclose()
        
    



        
    #code

# class request_info:
#     
#     def __init__(self):
#         self.reqcity= 'https://data.nj.gov/resource/k9xb-zgh4.json'
#         
#     def mrequest(self, reqcity=self.reqcity):
#         r = requests.get(reqcity)
#     
#     
#     #code
# import pandas as pd
# from sodapy import Socrata
# 
# api_key_id = 'esmxq0m7lzx9a9i62fv4dsxv3'
# api_secret = '2isigm4cqtwqzfrmnyushedtz1wt2tztno25x60a874jv5eimn'
# 
# 
# # Unauthenticated client only works with public data sets. Note 'None'
# # in place of application token, and no username or password:
# client = Socrata("data.nj.gov", None)
# 
# # Example authenticated client (needed for non-public datasets):
# # client = Socrata(data.nj.gov,
# #                  MyAppToken,
# #                  userame="user@example.com",
# #                  password="AFakePassword")
# 
# # First 2000 results, returned as JSON from API / converted to Python list of
# # dictionaries by sodapy.
# results = client.get("k9xb-zgh4", limit=2000)
# 
# # Convert to pandas DataFrame
# results_df = pd.DataFrame.from_records(results)
# 
# Testing coding with my voice
# Testing tab space space space space space bar 