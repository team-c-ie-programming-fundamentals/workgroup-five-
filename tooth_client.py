#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 09:03:50 2018

@author: yotroz
"""

#%%
import requests
#from flask import Flask, jsonify

    


def create_toot(user, toot): 
    
    data = { user, toot}
    
    return requests.post(url='http://127.0.0.1:5000/create-toot/' + user + '/' + toot, data=data)

#    return requests.get('http://127.0.0.1:5000/create-toot/' + user + "/" + toot


    
#%%

import requests
def get_toots(user): 
    request = requests.get('http://127.0.0.1:5000/user-toots/' + user)
    return request.json()


def followers_list(user):
    request = requests.get('http://127.0.0.1:5000/follows/' + user)
    
    return request.json()

response = requests.get("http://127.0.0.1:5000/users")

data = response.json()

print(data)