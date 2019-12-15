import json
from jsonManipulations import *
class Match:
    def __init__(self,matchJSON):
        self.gameId = matchJSON["gameId"]
        self.gameDuration = matchJSON["gameDuration"]
        
        # A SER INTERPRETADA DO PONTO DE VISTA DO TIME AZUL(teamB)
        self.win = matchJSON["teams"][0]["win"]   # Fail/Win
        self.firstBlood = matchJSON["teams"][0]["firstBlood"] # false/true self.firstTower = matchJSON["teams"][0]["firstTower"] # false/true 
        self.firstInhibitor = matchJSON["teams"][0]["firstInhibitor"] # false/true 
        self.firstBaron = matchJSON["teams"][0]["firstBaron"] # false/true 
        self.firstDragon = matchJSON["teams"][0]["firstDragon"] # false/true 
        self.firstRiftHerald = matchJSON["teams"][0]["firstRiftHerald"] # false/true 
        self.firstTower = matchJSON["teams"][0]["firstTower"]

        self.teamB = (Teams(matchJSON["teams"][0]))
        self.teamR = (Teams(matchJSON["teams"][1]))

class Teams:
    def __init__(self,teamJSON):

        # NAO TEM IMPORTANCIA POIS A ORDEM DO BYTE INDICARA QUAL TIME
        # BOOLSBYTETEAMS
        self.towerKills = teamJSON["towerKills"] # int
        self.inhibitorKills = teamJSON["inhibitorKills"] # int
        self.baronKills = teamJSON["baronKills"]  # int
        self.dragonKills = teamJSON["dragonKills"] # int
        self.riftHeraldKills = teamJSON["riftHeraldKills"] # int

        self.bans = getBans(teamJSON) # Lista coms o campeoes banidos


        if (teamJSON["teamId"] == 100):
            self.participant1 = (Participants(matchJSON["participants"][0]))
            self.participant2 = (Participants(matchJSON["participants"][1]))
            self.participant3 = (Participants(matchJSON["participants"][2]))
            self.participant4 = (Participants(matchJSON["participants"][3]))
            self.participant5 = (Participants(matchJSON["participants"][4]))
        else:
            self.participant1 = (Participants(matchJSON["participants"][5]))
            self.participant2 = (Participants(matchJSON["participants"][6]))
            self.participant3 = (Participants(matchJSON["participants"][7]))
            self.participant4 = (Participants(matchJSON["participants"][8]))
            self.participant5 = (Participants(matchJSON["participants"][9]))


class Participants:
    def __init__(self,prtcJSON):
        # ACCOUNT INFO

        # IN GAME STATS
        # ints
        self.championId = prtcJSON["championId"] 
        self.kills = prtcJSON["stats"]["kills"] 
        self.deaths = prtcJSON["stats"]["deaths"] 
        self.assists = prtcJSON["stats"]["assists"] 
        self.largestKS = prtcJSON["stats"]["largestKillingSpree"]
        self.largestMK = prtcJSON["stats"]["largestMultiKill"]
        self.longTSL = prtcJSON["stats"]["longestTimeSpentLiving"]
        self.doubleKills = prtcJSON["stats"]["doubleKills"]
        self.tripleKills = prtcJSON["stats"]["tripleKills"]
        self.quadraKills = prtcJSON["stats"]["quadraKills"]
        self.pentaKills = prtcJSON["stats"]["pentaKills"]
        self.totalddtc = prtcJSON["stats"]["totalDamageDealtToChampions"]
        self.mddtc = prtcJSON["stats"]["magicDamageDealtToChampions"]
        self.pddtc = prtcJSON["stats"]["physicalDamageDealtToChampions"]
        self.trueddtc = prtcJSON["stats"]["trueDamageDealtToChampions"]
        self.dmgObj = prtcJSON["stats"]["damageDealtToObjectives"]
        self.dmgTur = prtcJSON["stats"]["damageDealtToTurrets"]
        self.visionscore = prtcJSON["stats"]["visionScore"]
        self.timeCCO = prtcJSON["stats"]["timeCCingOthers"]
        self.totalGold = prtcJSON["stats"]["goldEarned"]
        self.turretKills = prtcJSON["stats"]["turretKills"]
        self.inhibKills = prtcJSON["stats"]["inhibitorKills"]
        self.totalMinionsK = prtcJSON["stats"]["totalMinionsKilled"]
        self.neutralMinionsK = prtcJSON["stats"]["neutralMinionsKilled"]
        self.neutralMinionsKTJ = prtcJSON["stats"]["neutralMinionsKilledTeamJungle"]
        self.neutralMinionsKEJ = prtcJSON["stats"]["neutralMinionsKilledEnemyJungle"]
        self.champLevel = prtcJSON["stats"]["champLevel"]
        self.vwb = prtcJSON["stats"]["visionWardsBoughtInGame"]
        # bool
        self.fb = prtcJSON["stats"]["firstBloodKill"]
        self.fba = prtcJSON["stats"]["firstBloodAssist"]

class Player:
    def __init__(self, playerJSON):
        summoner = getSummoner(match,8) # Pega um summoner aleatorio da partida

