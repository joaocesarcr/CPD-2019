from bytesClasses import *
from btree import *
import json
import struct

###### COMO CHAMAR:
# searchFunctions NOME PERSONAGEM + DADOS QUE GOSTARIA DE CALCULAR A MEDIA
# TODO = FUNCAO PARA CRUZAR PESQUISAS, EX = YASUO WINRATE > 50%, QUAL A  MEDIA CREEPS

### Constantes
matchPSTR = '2I h'
teamPack = '10H'
player = '10h 17H'
matchSize = 590
###

numeropartida = 1
offset = numeropartida * matchSize
raiz = nodo_btree(0, btree_matchs)
#### Cria um dicionario se baseando no arquivo champion.json
# Possui Nome Personagem: ID
# ID : Nome Personagem
with open('champion.json', 'r') as cj:
    data = json.load(cj)
data = data["data"]
c = {}
for champion, d in data.items():
    c[int(d['key'])] = champion
    c[champion] = int(d['key'])
cj.close()

def playerTeam(championID, matchBIN):
    # Retorna 1 se o jogador está no time azul
    position = 13
    bu = struct.unpack(matchPSTR + teamPack + player*5 + teamPack + player * 5,matchBIN) #"explica" o formato do arquivo e desempacota
    for player in range(1,6):
        playerPick = bu[position]
        position = position + (28 * i)
        if playerPick == championID:
            return 1
    return 0
             
def playerWon(championID, matchBIN):
    bu = struct.unpack(matchPSTR + teamPack + player*5 + teamPack + player * 5,matchBIN) #"explica" o formato do arquivo e desempacota
    bytesWhoWon = bin(bu[3])
    if (byteWhoWon & bin(64)):
        team1Won = 1
    playerside = playerTeam(championID,matchBIN)
    if (team1won and playerside): # Time 1 ganhou e o player estava no time 1
        return 1
    elif (team1won |playerside): # player estava no time contrario do time ganhador
        return 0
    else: return 1 # jogador ganhou e estava no time 2
    
def winrate(championName):
    championID = c[championName]
    wins = 0
    total = 0
    championGames = championMatchesToList(championID)
    with open('matches.bin','rb') as matchBINFile:
        matchBIN = matchBINFile.read()
        for game in championGames:
            if (playerWon(championID, matchBIN)):
                wins = wins + 1
                total = total + 1
    matchBIN.close()
    if total == 0: return 0
    return (wins/total)

def championMatchesToList(championID):
    championsMatches = []
    championName = c[championID]
    diretorio = './championsMatches/' + championName + '.bin'
    with open(diretorio,'ab') as championMatchesFile:
        numberOfBytes = championMatchesFile.tell()
        numberOfMatches = int(numberOfBytes/8)
    with open (diretorio, 'rb') as championsMatchesFile:
        for i in range(1,numberOfMatches + 1):
            offset = i * 4
            championsMatchesFile.seek(offset)
            matchIDBIN = championsMatchesFile.read(8)
            matchID = struct.unpack('L',matchIDBIN)
            championsMatches.append(matchID[0] % 10000)
    championsMatchesFile.close()
    return championsMatches

def matchPositionsFromList(matchList):
    matchesList = []
    return matchesList

with open('btree_matchs', 'rb') as btree_matchs:
    print(raiz.consulta(0,9491,btree_matchs))
print(championMatchesToList(c['Yasuo']))

# print("%.2f" % winrate('Irelia'))
##################
#     TESTES     #
##################
# bu = struct.unpack(matchPSTR + teamPack + player*5 + teamPack + player * 5,binary) #"explica" o formato do arquivo e desempacota
# Declaracao da classe se encontra em bytesClasses.py
# p = binaryMatch(bu) # variavel p se transforma numa classe que contem todas informacoes de uma partida

# for i in range(10,30):
    # offset = i * matchSize + 8
    # with open('matches.bin', 'rb') as binaryFILE: # Abre o bin.bin, arquivo gerado pelo empacota.py
        # binaryFILE.seek(offset)
        # binary = binaryFILE.read(matchSize)
        # binaryFILE.close()
   
    # bu = struct.unpack(matchPSTR + teamPack + player*5 + teamPack + player * 5,binary) #"explica" o formato do arquivo e desempacota
    # p = binaryMatch(bu)
    # print('offset ',offset)
    # print('ID da partida=',p.gameId)
    # print('Duracao da partida =',p.gameDuration,'segundos')
# print('Abates player 2 time vermelho =',p.teamB.participant2.kills)
# print('Mortes player 5 time vermelho =',p.teamB.participant5.deaths)
# print('Abates player 1 time azul =',p.teamB.participant1.kills)
# print('Personagem utilizado pelo player 5 time vermelho =',p.teamR.participant2.championId)

