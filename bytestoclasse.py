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
print(matchC.teamB.participant1.kills)
# gameId = bu[0]
# gameDuration = bu[1]
# byteBoolean = bu[2]

# print(bu[3:148][10:37])
# print(bu[3:148][37:64])
# print(bu[3:148][64:91])
# print(bu[3:148][91:118])
# print(bu[3:148][118:145])

# print(bu[148:293][37:64])
# print(bu[148:293][64:91])
# print(bu[148:293][91:118])
# print(bu[148:293][118:145])
