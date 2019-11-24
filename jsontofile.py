# Libs
import json

# Files
import jsonManipulations
import teste 

with open('output.json') as json_file:
    matchJSON = json.load(json_file)


class Teams:
    def __init__(self,teamJSON):
        self.Id = teamJSON["teamId"] # int
        self.win = teamJSON["win"]   # Fail/Win
        self.firstBllod = teamJSON["firstBlood"] # false/true
        self.firstTower = teamJSON["firstTower"] # false/true 
        self.firstInhibitor = teamJSON["firstInhibitor"] # false/true 
        self.firstBaron = teamJSON["firstBaron"] # false/true 
        self.firstDragon = teamJSON["firstDragon"] # false/true 
        self.firstRiftHerald = teamJSON["firstRiftHerald"] # false/true 
        self.towerKills = teamJSON["towerKills"] # int
        self.inhibitorKills = teamJSON["inhibitorKills"] # int
        self.baronKills = teamJSON["baronKills"]  # int
        self.dragonKills = teamJSON["dragonKills"] # int
        self.riftHeraldKills = teamJSON["riftHeraldKills"] # int
        self.bans = getBans(teamJSON) # Lista coms o campeos banidos


class Player:
    def __init__(self, playerJSON):
        summoner = getSummoner(match,8) # Pega um summoner aleatorio da partida

class Match:
    def __init__(self,matchJSON):
        self.gameId = matchJSON["gameId"]
        self.gameDuration = matchJSON["gameDuration"]
        self.teamB = (Teams(matchJSON["teams"][0]))
        self.teamR = (Teams(matchJSON["teams"][1]))

def getBans(teamsJSON):
    banList = []
    for ban in teamJSON["bans"]:
        banList = banList.append(ban["championId"])

match1 = Match(matchJSON)
print(match1.gameId,match1.gameDuration)
print(match1.teamB.Id)

