#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 08:40:24 2018

@author: yotroz
"""

#%%




from flask import Flask, jsonify


server = Flask("Toot server")


follows = {"pepe": ["octavio"],
           "agata": ["pepe", "octavio"]}


@server.route("/home")
def home_page(): 
    return "Welcome to Tooter"


@server.route("/users")
def users_page(): 
    return jsonify()




toots = {"octavio": ["hello", "Me encanta esto"],
         "pepe":["hello", "I love Python <3 "]}


@server.route("/create-toot")

def create_toot(user, toot): 
#    return user + " wrote: " + \n + toot
#    user = jsonify(user)
#    toot = jsonify(toot)    
      
#    return toots[user].append(toot)
    
#    return toots[user].append(toot)
#    toots = toots + toot
    print(toots)
    return user + "  wrote: test " + toot
    
#
    



#def print_toots(toots):
#    for toot in toots:
#        return toot
    
#     users[user].toots.append(message)

#    return toots[user].append(toot)







server.run()
