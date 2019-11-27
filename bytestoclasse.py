import matchClasses
import struct

# USAR FSEEk
matchPSTR = '2I h'
teamPack = '10H'
player = '10h 17H'
# Abre e le o arquivo
binaryFILE = open("bin.bin", 'rb')
binary = binaryFILE.read(590)
# binary unpack
bu = struct.unpack(matchPSTR + teamPack + player*5 + teamPack + player * 5,binary)

gameId = bu[0]
gameDuration = bu[1]
byteBoolean = bu[2]
# TeamStatsB
towerKills,inibKills, baronKills, dragonKills, riftHeraldKills = bu[3:8] 
bans = bu[9:19]

# TeamPlayers Pack
#team Pack
#teamplayersPack

