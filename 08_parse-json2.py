# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 19:51:36 2020

@author: CEC
"""

import urllib.parse
import requests

main_api="https://www.mapquestapi.com/directions/v2/route?"
orig="Guayaquil"
dest="Quito"
key="sAECPl4GMxASY0pK8EtJ3PqUHfyOoqfZ"
url= main_api + urllib.parse.urlencode({"key": key, "from":orig, "to": dest})

json_data= requests.get(url).json()

print("URL:" + (url))

  
json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")
