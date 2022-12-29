#!/usr/bin/env python
import requests
from urllib import request, error
import socket
import time
import math
import os

socket.setdefaulttimeout(60)
mirror = 'http://speedtest.tele2.net/1MB.zip'
filename = '1.zip'


allproxies = [
    "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
    "https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
    
]
def proxies():
    for i in allproxies:
        #proxies(i)
        print(i)
    #url = "https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/http.txt"#"https://www.proxyscan.io/download?type=http"
        url =  i#"https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt"
        proxis = requests.get(url).text
        proxis = proxis.splitlines()
        for proxy in proxis:
            prox,port = proxy.split(':')
            #print(f'checking {proxy}...')
            response = requests.post(f"http://ip-api.com/json/{prox}").json()
            try:
                res = response['isp']
                country = response['country']
                city = response['city']
                #print(res)
                if res == 'Google LLC':
                    #print(proxy)
                    r = requests.get("https://google.com/",proxies= {'http': proxy,'https': proxy}, timeout=5)
                    #print(r.status_code)
                    stat = r.status_code
                    if stat == 200:
                        
                        proxycheck = request.ProxyHandler({'http': proxy})
                        opener = request.build_opener(proxycheck)
                        request.install_opener(opener)
                        start = time.time()
                        request.urlretrieve(mirror, filename)
                        delta = time.time() - start
                        filesize = os.path.getsize(filename)
                        ratio = filesize/(delta*1024)
                        print('GProxy {} - Download speed:{} KB/s - Country: {} - City: {}'.format(proxy, math.floor(ratio), country, city))
                        if os.path.isfile(filename):
                            os.remove(filename)
                        
                    else:
                        pass

                else:
                    pass

            except:
                pass


proxies() 

print("finished")
