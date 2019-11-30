# Libs
import sys
import json
import struct

# Files
from matchClasses import *
from jsonManipulations import *
from APIrequests import *

# TODO PLAYER BOOLEANS nao esta sendo utilizado

# with open('output.json') as json_file:
    # matchJSON = json.load(json_file)

def fullPack(match):
    matchP = matchPack(match) # 2I + h 
    teamPB = teamPack(match.teamB) # 10H
    teamPP = teamPlayersPack(match.teamB)
    teamPR = teamPack(match.teamR) # 10H
    teamPPR = teamPlayersPack(match.teamR)
    return matchP + teamPB + teamPP + teamPR + teamPPR

################################### MATCH = 1
def matchPack(match): 
    # 2I + h
    a = matchInfToBytes(match) # 2I
    b = matchBoolsByte(match) # h
    return a + b

# gameId gameDuration -> pacote
def matchInfToBytes(match):
    b = struct.pack('2I',match.gameId,match.gameDuration)
    return b
    
# arquivo do tipo struct Match = entrada
# Como todos valores são booleanos, é possível armazenar todas as informações em um byte
# class Match -> binario
def matchBoolsByte(match):
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
    return struct.pack('h',firstByte)

#################################### TIMES = 2
def teamPack(team):
    # 5H + 5H = 10 H
    a = teamStats(team) 
    b = teamBans(team)
    return a + b

def teamStats(team):
    #towerKills, inhibKills,baronKills,dragonKills,riftHealdKills
    b = struct.pack('5H',
            team.towerKills,
            team.inhibitorKills,
            team.baronKills,
            team.dragonKills,
            team.riftHeraldKills)
    return b

def teamBans(team):
#TODO passar para array
    ban1 = team.bans[0]
    ban2 = team.bans[1]
    ban3 = team.bans[2]
    ban4 = team.bans[3]
    ban5 = team.bans[4]
    b = struct.pack('5H',ban1,ban2,ban3,ban4,ban5)
    return b

##################### PLAYER = 10
def teamPlayersPack(team):
    # Recebe um time e empacota os dados de todos jogadores
    p1 = participantPack(team.participant1) #= 10h 6H 11H
    p2 = participantPack(team.participant2)
    p3 = participantPack(team.participant3) 
    p4 = participantPack(team.participant4)
    p5 = participantPack(team.participant5)
    return p1  + p2 + p3 + p4 + p5

def participantPack(p):
    pStats = participantStats(p) #10h
    pDmg = participantDmgInfo(p) #6H
    pInfo = participantInfo(p) # 11H
    return pStats + pDmg + pInfo
    
def participantStats(p):
    b = struct.pack('10h',
            p.championId,
            p.kills,
            p.deaths,
            # p.assists,
            p.largestKS,
            p.largestMK,
            p.longTSL,
            p.doubleKills,
            p.tripleKills,
            p.quadraKills,
            p.pentaKills)
    return b

def participantDmgInfo(p):
# Ordem = totalddt, mddtc, pddtc, trueddtc, dmgobj, dmgtur
    b = struct.pack('6H',
            p.totalddtc,
            p.mddtc,
            p.pddtc,
            p.trueddtc,
            p.dmgObj,
            p.dmgTur)
    return b

def participantInfo(p):
# Ordem = visionscore,timecco,totalgold,turretKills,inibKills,totalMinionsK,neutralMinionsK, neutraMinionsKTJ,neutralMinionsKEJ,champLevel,vwb
    b = struct.pack('11H',
            p.visionscore,
            p.timeCCO,
            p.totalGold,
            p.turretKills,
            p.inhibKills,
            p.totalMinionsK,
            p.neutralMinionsK,
            p.neutralMinionsKTJ,
            p.neutralMinionsKEJ,
            p.champLevel,
            p.vwb)
    return b

def participantBool(p):
    bit = 0
    if(p.fb | p.fba): bit = 1
    b = struct.pack('h',bit)
    return b


        
################### ETC
# Ordem
# game Id, game duration
# Match bool 
# Dados time azul
    # bans do time azul
    # dados players dos times
match1 = Match(matchJSON)
 
#Match
fullP = fullPack(match1)
# teamP = teamPlayersPack(match1.teamB)
pTst = teamPlayersPack(match1.teamB)

# teamPP = teamPlayersPack(match1.teamB)
################### ESCREVE ARQUIVO 
f = open('bin.bin', 'ab')
f.write(fullP)
f.close()
    
matchPSTR = '2I h'
teamPack = '10H'
player = '10h 17H'
################ LE ARQUIVO
# binaryFILE = open("bin.bin", 'rb')
# binary = binaryFILE.read(590)
# binary_unpack = struct.unpack(matchPSTR + teamPack + (player * 5) + teamPack + (player * 5),binary)

# print(match1.teamR.participant5.championId)
# print(match1.teamB.participant5.championId)

