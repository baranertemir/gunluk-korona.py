#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 16:18:10 2020

@author: ayca22
"""

import requests
import json
from bs4 import BeautifulSoup

url = "https://covid19.saglik.gov.tr"
header = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"}

response = requests.get(url,headers=header)

soup = BeautifulSoup(response.content,"html.parser")

script = soup.find_all("script")

x = 0
for i in script:
    x += 1
    if x == 16:
        data = i
        break
data = str(data)

data = data.replace('<script type="text/javascript">',"")
data = data.replace('//<![CDATA[',"")
data = data.replace("var sondurumjson =","")
data = data.replace(";//]]>","")
data = data.replace("</script>","")
data = data.strip()
data = data.strip("[]")
data = json.loads(data)


tarih = data["tarih"]
test = data["gunluk_test"]
vaka = data["gunluk_vaka"]
vefat = data["gunluk_vefat"]
iyilesen = data["gunluk_iyilesen"]
toplam_test = data["toplam_test"]
toplam_vaka = data["toplam_vaka"]
toplam_vefat = data["toplam_vefat"]
toplam_iyilesen = data["toplam_iyilesen"]
toplam_yogun_bakim = data["toplam_yogun_bakim"]
agir = data["agir_hasta_sayisi"]

print("Tarih",tarih,"\nGünlük Test:",test,"\nGünlük Vaka:",vaka,"\nGünlük Vefat:",vefat,"\nGünlük İyileşen:",iyilesen,"\nToplam Test:",test,"\nToplam Vaka:",toplam_vaka,"\nToplam Vefat:",toplam_vefat,"\nToplam İyileşen:",toplam_iyilesen,"\nAğır Hasta Sayısı:",agir)


