# Libs
import json

# Files
# import jsonManipulations
# import teste 

# TODO = uma funcao que recebe a quantidade de bytes necessarios para serem alocados e a informacao a ser alocada
# TODO = nao vai valer a pena usar classe!

def isTrue(value):
    if (value == "True"): return 1
    else: return 0

with open('output.json') as json_file:
    matchJSON = json.load(json_file)

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

class Player:
    def __init__(self, playerJSON):
        summoner = getSummoner(match,8) # Pega um summoner aleatorio da partida

class Match:
    def __init__(self,matchJSON):
        self.gameId = matchJSON["gameId"]
        self.gameDuration = matchJSON["gameDuration"]
        self.teamB = (Teams(matchJSON["teams"][0]))
        self.teamR = (Teams(matchJSON["teams"][1]))

def getBans(teamJSON):
    banList = []
    for ban in teamJSON["bans"]:
        banList.append(ban["championId"])
    return banList
    
def Byte1TeamJSON(teamJSON):
    firstByte = 0
    # Considera como o primeiro bit o mais a esquerda de um byte 
    # TeamId(0/1), Win(0/1), firstBlood(0/1), firstTower(0/1)
    # FirstInib(0/1), firstBaron(0/1), firstDragon(0/1), firstRift(0/1)

    if (teamJSON["teamId"] == 200): 
        firstByte = firstByte | 1 
    # Segundo informa se o time ganhou(1) ou perdeu (0)
    firstByte = firstByte << 1 
    if (teamJSON["win"] == "Win"): 
        firstByte = firstByte | 1
    # Terceiro informa se o time causou o first blood
    firstByte = firstByte << 1 
    if (teamJSON["firstBlood"]): 
        firstByte = firstByte << 1 
        firstByte = firstByte | 1 
    # Quarto informa se o time levou a primeira torre
    firstByte = firstByte << 1 
    if (teamJSON["firstTower"]):
        firstByte = firstByte | 1
    # Quinto informa se o time levou o primeiro inibidor
    firstByte = firstByte << 1 
    if (teamJSON["firstInhibitor"]): 
        firstByte = firstByte | 1
    # Sexto informa se o time levou o primeiro barao
    firstByte = firstByte << 1 
    if (teamJSON["firstBaron"]):
        firstByte = firstByte | 1
    # Setimo informa se o time levou o primeiro dragao
    firstByte = firstByte << 1 
    if (teamJSON["firstDragon"]):
        firstByte = firstByte | 1

    # Oitavo bit informa se o time levou o
    firstByte = firstByte << 1 
    if (teamJSON["firstRiftHerald"]):
        firstByte = firstByte | 1
    return firstByte

match1 = Match(matchJSON)
firstByte = Byte1TeamJSON(matchJSON["teams"][0])
firstByte = ('{0:08b}'.format(firstByte))
print(json.dumps(matchJSON["teams"][0], indent=4, sort_keys=False))
print(firstByte)

f= open("match1.txt","w+")
f.write(firstByte)
f.close()
# print(match1.gameId,match1.gameDuration)
# print(match1.teamB.Id)
# print(match1.teamB.bans)
