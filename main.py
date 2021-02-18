from utili import GetRecentlyPlayedGames, returnPlayTime, GetPlayerSummaries
import numpy as np
import pandas as pd

def main():

    gameCount = []
    recentlyPlayed = []
    playTime = []
    location = []

    with open('./data/realFinalFinal.txt', "r") as f:
        userIdList = f.readlines()

    counter = 0
    for userId in userIdList:
        counter +=1
        if counter == 5000:
            break
        try:
            result = GetRecentlyPlayedGames(int(userId))
            gameCount.append(result[0])
            recentlyPlayed.append(result[1])
            playTime.append(returnPlayTime(int(userId)))
            location.append(GetPlayerSummaries(userId))
        except:
            gameCount.append(np.nan)
            recentlyPlayed.append(np.nan)
            playTime.append(np.nan)
            location.append(np.nan)

    
    d = {"SteamID" : pd.Series(userId), "Game_Count" : pd.Series(gameCount), "Game_List" : pd.Series(recentlyPlayed),
    
        "TotalPlayTime" : playTime, "Location" : location}

    df = pd.DataFrame(d)

    df.to_csv("./output1.txt")
        
if __name__ == "__main__":
    main()
    


    