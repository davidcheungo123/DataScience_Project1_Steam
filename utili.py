import requests
import json
import numpy as np

def GetRecentlyPlayedGames(steamid):
    #steamid	uint64	✔	The player we're asking about
    url = "http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v1/?key=<key>&format=json"

    params={
    'steamid':steamid,

    }
    response = requests.get(url,params=params)
    d = json.loads(response.text)
    RecentlyPlayedGame_Dict = {}

    try: 
        count_of_game = d["response"]["total_count"]
    except:
        count_of_game = 0

    try:
        if bool(d["response"]):
            for i in range(len(d["response"]["games"])):
                gameID = d["response"]["games"][i]["appid"]
                game_name = d["response"]["games"][i]["name"]
                playtime_2w = d["response"]["games"][i]["playtime_2weeks"]

                RecentlyPlayedGame_Dict[gameID] = [game_name,playtime_2w]
    except:
        RecentlyPlayedGame_Dict = {}

    return (count_of_game,RecentlyPlayedGame_Dict)


def returnPlayTime(steamId):
    #steamid	uint64	
    #include_appinfo	bool
    #include_played_free_games	bool
    #32196D5A386BD32E48454D8C69AC2C43
    params = {
        "steamid" : int(steamId),
        "key" : "<key>",
        "include_appinfo" : True,
        "include_played_free_games" : True
    }
    try:
        url = requests.get("https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v1/", params=params)
        D = json.loads(url.text)
        print(D)
        # bool(D["response"]) : if this is not an empty dict => return True , otherwise False
        if bool(D["response"]):
            DList = D["response"]["games"]
            getTimeList = []
            for app in DList:
                if app["playtime_forever"] is not None:
                    getTimeList.append(app["playtime_forever"])
                else:
                    getTimeList.append(0)
            return sum(getTimeList)
        else:
            return np.nan
    except:
        return np.nan

def GetPlayerSummaries(steamId):
    #steamids    string
    try:
        steamId = str(steamId)
        params = {
            "steamids" : steamId,
            "key" : "<key>"
        }
        url = requests.get("https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/" ,params=params)
        data = json.loads(url.text)
        return data["response"]["players"][0]["loccountrycode"]
    except:
        return np.nan