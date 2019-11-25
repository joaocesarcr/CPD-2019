# Libs
import pickle
import sys
import json

# Files
from matchClasses import *
from jsonManipulations import *

# import teste 

# TODO = uma funcao que recebe a quantidade de bytes necessarios para serem alocados e a informacao a ser alocada
# TODO = nao vai valer a pena usar classe!

with open('output.json') as json_file:
    matchJSON = json.load(json_file)
    
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
# firstByte = Byte1TeamJSON(matchJSON["teams"][0])
# print(match1.teamB.participants.championId)
print(json.dumps(match1.teamB.participants.championId, indent=4, sort_keys=False))
# print(match1.gameId,match1.gameDuration)
# firstByte = ('{0:8}'.format(firstByte))
# with open("match.xxd", "wb") as mypicklefile:
        # pickle.dump(firstByte, mypicklefile)
sys.exit()
# print(match1.gameId,match1.gameDuration)
# print(match1.teamB.Id)
# print(match1.teamB.bans)
