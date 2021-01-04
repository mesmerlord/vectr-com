import cloudscraper
import bs4
import requests
from bs4 import BeautifulSoup
from requests import adapters
import ssl
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
import json

class MyAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       ssl_version=ssl.PROTOCOL_TLSv1)
username= input("Username:")
password = input("Password:")
payload = {
    'password': password,
    'username': username

}

def downloadsvg(height, width):
    name=adapters.HTTPAdapter
    s=requests.Session()
    s.mount('https://vectr.com/api/login', MyAdapter())

    # Login with post and Request source code from main page.
    log=s.post('https://vectr.com/api/login', data=payload)
    new=cloudscraper.create_scraper(sess=s)

    soup=json.loads(new.get(f"https://vectr.com/{username}/designs/.index.json").content)
    todl=[]

    for item in soup['data']:
        todl.append(item['name'])
    x=1
    for item in todl:
        with open(f"file{x}.svg", 'wb') as newfile:
            file=new.get(f"https://vectr.com/{item}.svg?width={width}&height={height}").content
            newfile.write(file)
            x+=1


proportions = input("Use specific proportions, height first then width, ex. 640x640. Type no for default : ")
if len(proportions.split("x")) <1:
    x1 = proportions.split("x")


else:
    x1= [640,640]

downloadsvg(int(x1[0]),int(x1[1]))

