import requests
import json


"""
Helper function 1
GetPlayerSummaries is an API, We use the API to check if the steamids are public or not,
This function will return boolean value given the ["response"]["players"][0]["loccountrycode"] exists or not.
[make sure valid steam API key]
"""

def GetPlayerSummaries(steamId):
    steamId = str(steamId)
    params = {
        "steamids" : steamId
    }
    try:
        url = requests.get("https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key=<key>&format=json" ,params=params)
        data = json.loads(url.text)
        if data["response"]["players"][0]["loccountrycode"] is not None:
            return True
        else:
            return False
    except:
        return False

"""
Helper function 2
change the format of steamid to 64bits format.
"""

def steamid_to_64bit(steamid):
    steam64id = 76561197960265728

    id_split = steamid.split(":")
    steam64id += int(id_split[2]) * 2
    if id_split[1] == "1":
        steam64id += 1
    return steam64id

"""
main()
SteamIDs follow a fairly simple format when represented textually: "STEAM_X:Y:Z"
We can make use of that format and pattern to change the format to 64bits and check 
if the steamid is valid.
"""

def main():

    initialSteamIDList = []
    """
    8digits, We can control the range so that to control the number of steamID
    e.g. for i in range(40100000, 40100500) to test 500 values and append valid ids into finalList 
    """
    for i in range(40100000, 40100500):
        x = "STEAM_1:1:" + str(i)
        initialSteamIDList.append(x)

    finalList = []

    for steamID in initialSteamIDList:
        x = steamid_to_64bit(steamID)
        if GetPlayerSummaries(x):
            finalList.append(x)
        else:
            continue

    #txt file name 
    with open("./data/realFinalFinalv2.txt", "w") as f:
        for item in finalList:
            f.write("%s\n"  % str(item))

if __name__ == "__main__":
    main()