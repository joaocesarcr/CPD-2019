import json
from jsonManipulations import *

with open('output.json') as json_file:
    matchJSON = json.load(json_file)

class Match:
    def __init__(self,matchJSON):
        self.gameId = matchJSON["gameId"]
        self.gameDuration = matchJSON["gameDuration"]
        self.teamB = (Teams(matchJSON["teams"][0]))
        self.teamR = (Teams(matchJSON["teams"][1]))

class Teams:
    def __init__(self,teamJSON):
        # PRIMEIRO BYTE
        self.Id = teamJSON["teamId"] # int
        self.win = teamJSON["win"]   # Fail/Win
        self.firstBlood = teamJSON["firstBlood"] # false/true
        self.firstTower = teamJSON["firstTower"] # false/true 
        self.firstInhibitor = teamJSON["firstInhibitor"] # false/true 
        self.firstBaron = teamJSON["firstBaron"] # false/true 
        self.firstDragon = teamJSON["firstDragon"] # false/true 
        self.firstRiftHerald = teamJSON["firstRiftHerald"] # false/true 

        # SEGUNDO BYTE
        self.towerKills = teamJSON["towerKills"] # int
        self.inhibitorKills = teamJSON["inhibitorKills"] # int
        self.baronKills = teamJSON["baronKills"]  # int
        self.dragonKills = teamJSON["dragonKills"] # int
        self.riftHeraldKills = teamJSON["riftHeraldKills"] # int

        self.bans = getBans(teamJSON) # Lista coms o campeoes banidos

        self.participants = (Participants(matchJSON))

class Participants:
    def __init__(self,matchJSON):
        self.championId = matchJSON["participants"][1]

class Player:
    def __init__(self, playerJSON):
        summoner = getSummoner(match,8) # Pega um summoner aleatorio da partida


