from urllib.request import urlopen
import json, textwrap


import urllib.request,urllib.error
import json
from keys import rito

def requestUrl(url):
    try:
        #attempt to parse the url to return data in json format
        response = urllib.request.urlopen(url)
        string = response.read().decode('utf-8')
        return json.loads(string)
    except urllib.error.HTTPError as e:
        return e

def getChallenger():
    url = "https://na1.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key=" + rito
    dirtData = requestUrl(url)
    
    #403 is an error code due to the most common issue, API key needs regen


    if type(dirtData) == urllib.error.HTTPError:
        return False
    
    players = dirtData["entries"]

    cleanData = {}

    for i in range(1, len(players)):
        #creates dict pairing players with their points 
        cleanData[players[i]["summonerName"]] = players[i]["leaguePoints"]
    topFive = sortDict(cleanData)

    return topFive



def sortDict(roster):
    #sorts aggregated leaderboard data and organizes it ascending 
    leaderboard=dict(sorted(roster.items(),key= lambda x:x[-1]))
    topFive = {}
    #reverse ascending list to descending, grabs top five 
    for x in list(reversed(list(leaderboard)))[0:5]:
        topFive[x] = leaderboard[x]


