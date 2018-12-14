#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 09:03:50 2018

@author: yotroz
"""

#%%
import requests
from flask import Flask, jsonify

        


#%%

import requests

def create_toot(user, toot): 
    
    request = requests.get('http://127.0.0.1:5000/create-toot/{}/{}'.format(user, toot))
    return request.json()
    

def get_toots(user): 
    
    request = requests.get('http://127.0.0.1:5000/user-toots/' + user)
    return request.json()


def followers_list(user):
    
    request = requests.get('http://127.0.0.1:5000/follows/' + user)
    return request.json()

def follow_someone(user, user_to_follow):
    
    request = requests.get('http://127.0.0.1:5000/follow-user/{}/{}'.format(user, user_to_follow))
    return request.json()
    

def unfollow_user(user, user_to_unfollow): 
    
    request = requests.get('http://127.0.0.1:5000/unfollow-user/{}/{}'.format(user, user_to_unfollow))
    return request.json()

def get_timeline(user): 
    request = requests.get('http://127.0.0.1:5000/timeline/{}'.format(user))
    return request.json()


response = requests.get("http://127.0.0.1:5000/users")

data = response.json()

print(data)