import pandas as pd
import requests
import glob
import re
import csv
from bs4 import BeautifulSoup as bsm
from googlesearch import search
class gsearch:
    
    def __init__(self):
        self.csvf = glob.glob('njtow*.csv')
        self.urllist = []
        self.csvd = {}
        self.ocsv = open(self.csvf[0], 'r', newline='', encoding='utf8')
        self.rcsv = csv.DictReader(self.ocsv)
        i = 0
        for row in self.rcsv:
            self.csvd[i] = row
            i+=1
        self.fdict = {}
        
        
    def urlq(self):
        tlist = []
        csvd = self.csvd
        for row in csvd:
            # print(csvd[row])
            # print(csvd[row]['Township'])
            city = str(csvd[row]['City'])
            
            cityurl = 'filetype:pdf Township of '+ city + ' New Jersey zone map'
            capp = {city:{'city':cityurl}}
            tlist.append(capp)
            # print(capp)
            capp = {}
            
            
        return tlist
    
    def resplinks(self, list_of_towns):
        townlinks = {}
        linklist = []
        glinks = {}
        glist = []
        curlist=[]
        li = list_of_towns
        i=0
        for town in li:
            
            tname = str(list(town)[0])
            turl = town[tname]['city']
            print(i, tname, turl)
            # print(tname, turl)
            gfile = self.gglesearch(turl, tname)
            linklist.append(gfile)
            townlinks[tname] = gfile
            gfile = ''
            i+=1
        
        
        
        return townlinks
            

    def dlpdfs(self, fileurls):
        foo = 'bar'
    
    def dlfile(self, townlist):
        for t in townlist:
            
            town = townlist[t]['town']
            link = townlist[t]['link']
            fname = '''\\zoning\\''' + str(town) + '_ordinance.pdf'
            f = open(fname, 'wb')
            r = requests.get(link)
            for chunk in r.iter_content(2048):
                f.write(chunk)
            f.close()
        
    
    
    def gglesearch(self, searchurl, town):
        lcount = 0
        rdict = {}
        t = town
        
        result = search(searchurl, num=1, stop=1,pause=2)
        for r in result:
            if lcount > 0:
                rdict = {'error':'link'}
            else:
                lcount+=1
                try:
                    rdict  = {'town':town, 'link':str(r)}
                    
                except Exception as e:
                    rdict =  {'error':e}
        
        return rdict
        
        # print(result)
        # try:
        #     # print(dir(result))
        #     fname = str(result).split('/')[-1]
        #     f = requests.get(result)
        #     # print(fname)
        #     # fout = open(fname, 'wb')
        #     tdict = {'town':town, 'fileurl':str(result)}
        #     fd[town] = {'town':town, 'fileurl':str(result)}
        #     # for c in f.iter_content(1024):
        #     #     fout.write(c)
        #     # fout.close()
        #     
        # except Exception as e:
        #     tdict = {'town':'error', 'fileurl':e}
            
        
        
        
    
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