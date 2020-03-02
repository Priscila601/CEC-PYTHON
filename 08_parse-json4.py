# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 20:04:21 2020

@author: CEC
"""


import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "Tznt11GJzT0W3awGbRvrGPutNBN7Ns0z"
while True:
    orig = input("Starting location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")    
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))
