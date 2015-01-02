# -*- coding: utf-8 -*-
import json
import requests
from pandas import DataFrame, Series

'''
API Key: d0a219271900223e7dcced8bf644ca1f
Secret: is 6d7b8c744b855f9528c6071d37304759
http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=d0a219271900223e7dcced8bf644ca1f&format=json
'''

def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain.
    #
    # Once you've done this, return the name of the number 1 top artist in Spain.
    data = requests.get(url).text
    data = json.loads(data)
    
    
    topartists = data['topartists']
    artists = topartists['artist']

    #df = DataFrame[artist]
    for artist in artists:
        attr = artist['@attr']
        rank =  attr['rank']
        
        if rank == "1":
            return artist['name']            
            
    
    #print artist
    return 'unknown'
        
url = "http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=d0a219271900223e7dcced8bf644ca1f&format=json"

print api_get_request(url)