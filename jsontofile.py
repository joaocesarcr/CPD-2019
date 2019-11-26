# Libs
import pickle
import sys
import json
import struct

# Files
from matchClasses import *
from jsonManipulations import *
from jsontofile import *

# import teste 

# TODO = uma funcao que recebe a quantidade de bytes necessarios para serem alocados e a informacao a ser alocada

with open('output.json') as json_file:
    matchJSON = json.load(json_file)
    
# Recebe struct Match match
# int + int -> pacote
# gameId gameDuration -> pacote
def matchInfToBytes(match):
    b = struct.pack('I I',match.gameId,match.gameDuration)
    return b
    
# arquivo do tipo struct Match = entrada
# Como todos valores são booleanos, é possível armazenar todas as informações em um byte
# class Match -> binario
def teamBoolsByte(match):
    # Considera como o primeiro bit o mais a esquerda de um byte 
    # 1 BIT DEVE SER IGNORADO NAS BUSCAS
    firstByte = 1
    # Segundo informa se o time ganhou(1) ou perdeu (0)
    firstByte = firstByte << 1 
    if (match.win == "Win"): 
        firstByte = firstByte | 1
    # Terceiro informa se o time causou o first blood
    firstByte = firstByte << 1 
    if (match.firstBlood): 
        firstByte = firstByte | 1 
    # Quarto informa se o time levou a primeira torre
    firstByte = firstByte << 1 
    if (match.firstTower):
        firstByte = firstByte | 1
    # Quinto informa se o time levou o primeiro inibidor
    firstByte = firstByte << 1 
    if (match.firstInhibitor): 
        firstByte = firstByte | 1
    # Sexto informa se o time levou o primeiro barao
    firstByte = firstByte << 1 
    if (match.firstBaron):
        firstByte = firstByte | 1
    # Setimo informa se o time levou o primeiro dragao
    firstByte = firstByte << 1 
    if (match.firstDragon):
        firstByte = firstByte | 1

    # Oitavo bit informa se o time levou o
    firstByte = firstByte << 1 
    if (match.firstRiftHerald):
        firstByte = firstByte | 1
    return struct.pack('I',firstByte)

################### ETC
match1 = Match(matchJSON)
matchBool = (teamBoolsByte(match1))
matchInfo = matchInfToBytes(match1)

################### ESCREVE ARQUIVO 
f = open('bin.bin', 'wb')
f.write(matchInfo) # Game ID,gameDuration
f.write(matchBool) # Byte com informacoes booleanas
f.close()
    
sys.exit()
# print(match1.gameId,match1.gameDuration)
# print(match1.teamB.Id)
# print(match1.teamB.bans)
# print(match1.teamB.participants.championId)
# print(json.dumps(match1.teamB.participant1.championId, indent=4, sort_keys=False))
# print(json.dumps(match1.teamB.participant2.championId, indent=4, sort_keys=False))
# print(match1.gameId,match1.gameDuration)
# firstByte = ('{0:8}'.format(firstByte))
