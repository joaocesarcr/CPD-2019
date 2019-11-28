import struct

from bytesClasses import *
# TODO e possivel criar uma struct para nao precisarepetir codigo

# USAR FSEEk
matchPSTR = '2I h'
teamPack = '10H'
player = '10h 17H'
# Abre e le o arquivo
binaryFILE = open("bin.bin", 'rb')
binary = binaryFILE.read(590)
# binary unpack
bu = struct.unpack(matchPSTR + teamPack + player*5 + teamPack + player * 5,binary)
matchC = binaryMatch(bu)
# gameId = bu[0]
# gameDuration = bu[1]
# byteBoolean = bu[2]

# TeamStatsB
# towerKills,inibKills, baronKills, dragonKills, riftHeraldKills = bu[3:8] 
# bans = bu[8:13]
#           TeamPlayers Pack
#participantPack
#pstats
# PLAYER 1
# [0:26]
# championId,kills,deaths,largestKS,largestMK,longSTL,doubleKills,tripleKills,quadraKills,pentaKills = bu[13:23]
#pdmg
# totalddtc, mddtc, pddtc,trueddtc,dmgObj,dmgTur = bu[23:29]
#pinfo
# visionscore, timeCCO, totalGod, turretKills,inhibKills,totalMinionsK,neutralMinionsK,neutralMinionsKTJ,neutralMinionsKEJ,champLevel = bu[29:39]
# PLAYER 2
# 39:65
# PLAYER 3
# 65:91
# PLAYER 4
# 91:117
# PLAYER 5
# 117:143

#team Pack
# towerKills,inibKills, baronKills, dragonKills, riftHeraldKills = bu[146:181]
# bans = bu[44:49]

