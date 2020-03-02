# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 19:15:17 2020

@author: CEC
"""

import urllib.parse
import requests

main_api="https://www.mapquestapi.com/directions/v2/route?"
orig="Galapagos"
dest="Quito"
key="sAECPl4GMxASY0pK8EtJ3PqUHfyOoqfZ"
url= main_api + urllib.parse.urlencode({"key": key, "from":orig, "to": dest})

json_data= requests.get(url).json()
print(json_data)