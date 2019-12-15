from bytesClasses import *
import struct

binaryFILE = open("matches.bin", 'rb') # Abre o bin.bin, arquivo gerado pelo empacota.py
binaryFILE.seek(8)
binary = binaryFILE.read(590)

matchPSTR = '2I h'
teamPack = '10H'
player = '10h 17H'
bu = struct.unpack(matchPSTR + teamPack + player*5 + teamPack + player * 5,binary) #"explica" o formato do arquivo e desempacota
# Declaracao da classe se encontra em bytesClasses.py
p = binaryMatch(bu) # variavel p se transforma numa classe que contem todas informacoes de uma partida
print(bu)
print('')
print('ID da partida=',p.gameId)
print('Duracao da partida =',p.gameDuration,'segundos')
print('Abates player 2 time vermelho =',p.teamB.participant2.kills)
print('Mortes player 5 time vermelho =',p.teamB.participant5.deaths)
print('Abates player 1 time azul =',p.teamB.participant1.kills)
print('Personagem utilizado pelo player 5 time vermelho =',p.teamR.participant2.championId)
binaryFILE.seek(598)
binary = binaryFILE.read(590)
bu = struct.unpack(matchPSTR + teamPack + player*5 + teamPack + player * 5,binary) #"explica" o formato do arquivo e desempacota
p = binaryMatch(bu) # variavel p se transforma numa classe que contem todas informacoes de uma partida
print(bu)
print('')
print('ID da partida=',p.gameId)
print('Duracao da partida =',p.gameDuration,'segundos')
print('Abates player 2 time vermelho =',p.teamB.participant2.kills)
print('Mortes player 5 time vermelho =',p.teamB.participant5.deaths)
print('Abates player 1 time azul =',p.teamB.participant1.kills)
print('Personagem utilizado pelo player 5 time vermelho =',p.teamR.participant2.championId)

for i in range(20):
    posicao = i * 590
    binaryFILE.seek(posicao + 8)
    binary = binaryFILE.read(590)
    bu = struct.unpack(matchPSTR + teamPack + player*5 + teamPack + player * 5,binary) #"explica" o formato do arquivo e desempacota
    p = binaryMatch(bu) # variavel p se transforma numa classe que contem todas informacoes de uma partida
    print(bu)
    print('')
    print('ID da partida=',p.gameId)
    print('Duracao da partida =',p.gameDuration,'segundos')
