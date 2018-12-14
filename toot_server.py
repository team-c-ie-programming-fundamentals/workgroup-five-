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
           "agata": ["pepe", "octavio"],
           "octavio":["agata"]}

@server.route("/home")
def home_page(): 
    return "Welcome to Tooter"


@server.route("/users")
def users_page(): 
    return jsonify()



toots = {"octavio": ["hello", "Me encanta esto"],
         "pepe":["hello", "I love Python <3 "], 
         "agata":["I like singing", "kjkstels"]}


@server.route("/create-toot/<user>/<toot>")

def create_toot(user, toot): 
     
    if user in toots: 
         toots[user].append(toot)
    
         return jsonify(toots[user])
     
    else: 
        return jsonify("there's no user with that name")
    
@server.route("/user-toots/<user>")

def print_toots(user):
    user_all_toots = []
    for toot in toots[user]:
        user_all_toots.append(toot)
    return jsonify(user_all_toots)


@server.route("/follow-user/<user>/<user_to_follow>")
def follow_user(user, user_to_follow):
    if user in toots: 
        
        if user_to_follow in toots: 
                
            follows[user].append(user_to_follow)
            return jsonify(user + " is following " + user_to_follow)
        else: 
            return jsonify("the user you are trying to follow doesn't exist")
            
    else: 
        return jsonify("this user doesn't exist")

@server.route("/follows/<user>")
def get_all_follows(user): 
    if len(follows[user]) > 0: 
        
        user_all_follows = []
        for follow in follows[user]:
            user_all_follows.append(follow)
        return jsonify(user_all_follows)
    else: 
        return user + "!! you don't follow anyone :( Stop playing videogames and sociallize!"
    
@server.route("/unfollow-user/<user>/<user_to_unfollow>")
def unfollow_user(user, user_to_unfollow):
    if user_to_unfollow in follows[user]: 
            
        follows[user].remove(user_to_unfollow)
        return jsonify(user + " has stopped following " + user_to_unfollow)
    
    else: 
        return jsonify(user + " does not follow " + user_to_unfollow)
        
@server.route("/timeline/<user>")
def get_timeline(user): 
    timeline_user = []
    for toot in toots[user]:
        timeline_user.append(user + " wrote: " + toot)
        
    timeline_follower = []
    for follower in follows[user]: 
        for toot in toots[follower]:

            timeline_follower.append(follower + " wrote: " + toot) 
            
    timeline_follower = timeline_follower[::-1]
    timeline_user = timeline_user[::-1]
#    
        
    return jsonify(timeline_follower, timeline_user)
    

server.run()
