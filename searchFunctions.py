import json
import struct

from bytesClasses import *
from btree import *
###### COMO CHAMAR:
# searchFunctions NOME PERSONAGEM + DADOS QUE GOSTARIA DE CALCULAR A MEDIA
# TODO = FUNCAO PARA CRUZAR PESQUISAS, EX = YASUO WINRATE > 50%, QUAL A  MEDIA CREEPS

### Constantes
matchPSTR = '2I h'
teamPack = '10H'
player = '10h 17H'
matchSize = 590
###

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


# TODO ALTERAR PARA STRUCT
# championID + binario de uma partida -> boolean
# int + bin -> bool
# Retorna 1 se o jogador esta no time azul
def playerBlueTeam(championID, structedMatch):
    # Retorna 1 se o jogador está no time azul
    if structedMatch.teamB.participant1.championId == championID: return 1
    if structedMatch.teamB.participant2.championId == championID: return 1
    if structedMatch.teamB.participant3.championId == championID: return 1
    if structedMatch.teamB.participant4.championId == championID: return 1
    if structedMatch.teamB.participant5.championId == championID: return 1
    return 0

def participantByChampion(structedMatch,championID):
    if structedMatch.teamB.participant1.championId == championID: return 0
    if structedMatch.teamB.participant2.championId == championID: return 1
    if structedMatch.teamB.participant3.championId == championID: return 2
    if structedMatch.teamB.participant4.championId == championID: return 4
    if structedMatch.teamB.participant5.championId == championID: return 5

    if structedMatch.teamR.participant1.championId == championID: return 5
    if structedMatch.teamR.participant2.championId == championID: return 6
    if structedMatch.teamR.participant3.championId == championID: return 7
    if structedMatch.teamR.participant4.championId == championID: return 8
    if structedMatch.teamR.participant5.championId == championID: return 9
    else:
        return 2


# Indica se o jogador ganhou a partir do seu personagem
# int + bin -> bool
def playerWon(championID, structed):
    playerInTeamBlue = playerBlueTeam(championID,structed)
    boolByte = int(structed.byteBoolean)
    if boolByte < 0:
        boolByte = abs(boolByte) + 128
    mask = 64
    # print(mask,boolByte)
    teamBlueWon = mask & boolByte
    if (teamBlueWon & playerInTeamBlue): return 1
    if (not(teamBlueWon) and not(playerInTeamBlue)): return 1
    else: return 0

def firstDragon(championID, structed):
    playerInTeamBlue = playerBlueTeam(championID,structed)
    boolByte = int(structed.byteBoolean)
    if boolByte < 0:
        boolByte = abs(boolByte) + 128
    mask = 2
    # print(mask,boolByte)
    teamFirstDragon = mask & boolByte
    if (teamFirstDragon & playerInTeamBlue): return 1
    if (not(teamFirstDragon) and not(playerInTeamBlue)): return 1
    else: return 0
   
# TODO = CALCULAR O WINRATE A PARTIR DE UM NOME DE PERSONAGEM
def winrate(championName):
    championID = c[championName]
    wins = 0
    total = 0
    championGames = championMatchesToList(championID)
    with open('matches.bin','rb') as matchBINFile:
        for game in championGames:
            posicao = game * matchSize
            matchBINFile.seek(posicao + 8)
            matchBIN = matchBINFile.read(matchSize)
            structedMatchTuple = struct.unpack(matchPSTR + teamPack + player*5 + teamPack + player * 5,matchBIN) 
            structedMatch = binaryMatch(structedMatchTuple)

            if (playerWon(championID, structedMatch)):
                wins = wins + 1
            # print(structedMatch.byteBoolean)
            total = total + 1
    matchBINFile.close()
    result = ((wins/len(championGames)) * 100)
    result = format(result,'.3f')
    print('Winrate {} = {}%'.format(championName,result))
    return result

def firstDragonPrc(championName):
    championID = c[championName]
    dragons = 0
    total = 0
    championGames = championMatchesToList(championID)
    with open('matches.bin','rb') as matchBINFile:
        for game in championGames:
            posicao = game * matchSize
            matchBINFile.seek(posicao + 8)
            matchBIN = matchBINFile.read(matchSize)
            structedMatchTuple = struct.unpack(matchPSTR + teamPack + player*5 + teamPack + player * 5,matchBIN) 
            structedMatch = binaryMatch(structedMatchTuple)

            if (firstDragon(championID, structedMatch)):
                dragons = dragons + 1
            # print(structedMatch.byteBoolean)
            total = total + 1
    matchBINFile.close()
    result = dragons/len(championGames)
    result = result * 100
    result = format(result,'.3f')
    print('Chance de {} abater o primeiro dragao = {}%'.format(championName,result))


def firstDragonAndWin(championName):
    wins = 0
    dragons = 0
    championID = c[championName]
    championGames = championMatchesToList(championID)
    with open('matches.bin','rb') as matchBINFile:
        for game in championGames:
            posicao = game * matchSize
            matchBINFile.seek(posicao + 8)
            matchBIN = matchBINFile.read(matchSize)
            structedMatchTuple = struct.unpack(matchPSTR + teamPack + player*5 + teamPack + player * 5,matchBIN) 
            structedMatch = binaryMatch(structedMatchTuple)

            if (firstDragon(championID, structedMatch)):
                dragons = dragons + 1
            if playerWon(championID,structedMatch):
                wins = wins + 1
            # print(structedMatch.byteBoolean)
    matchBINFile.close()
    result = dragons/wins
    result = result * 10
    result = format(result,'.3f')
    print('Chance de {} ganhar apos abater o primeiro dragao = {}%'.format(championName,result))

def CS(championName):
    championID = c[championName]
    championGames = championMatchesToList(championID)
    creepscore = 0
    total = 0
    champl = list(championGames)
    champl.pop(0)
    with open('matches.bin','rb') as matchBINFile:
        i = 0
        # for game in champl:
        game = champl[0]
        for i in range(100):
            # posicao = game * matchSize
            matchBINFile.seek(matchSize + i)
            matchBIN = matchBINFile.read(matchSize)
            structedMatchTuple = struct.unpack(matchPSTR + teamPack + player*5 + teamPack + player * 5,matchBIN) 
            structedMatch = binaryMatch(structedMatchTuple)

            pId = participantByChampion(structedMatch,championID)
            playerInf = participantInfoByNumber(structedMatch,pId)
            creepscore = creepscore + playerInf.totalMinionsK
            total = total + 1
            print(creepscore)
    print(structedMatchTuple)

    # print('asdsa')
    # print(total)
    # print(creepscore/total)
    matchBINFile.close()
    return creepscore/total
    if total == 0: return 0

def teste():
    with open('matches.bin','rb') as matchBINFile:
        # for game in champl:
        game = 1 
        # matchSize = 293
        for i in range(10):
            posicao = i * 590
            matchBINFile.seek(posicao + 8)
            matchBIN = matchBINFile.read(590)
            structedMatchTuple = struct.unpack(matchPSTR + teamPack + player*5 + teamPack + player * 5,matchBIN) 
            structedMatch = binaryMatch(structedMatchTuple)
            print(structedMatch.gameId)
            print(structedMatch.teamB.participant1.championId)


 
def participantInfoByNumber(structedMatch, number):
    if number == 0: return structedMatch.teamB.participant1
    if number == 1: return structedMatch.teamB.participant2
    if number == 2: return structedMatch.teamB.participant3
    if number == 3: return structedMatch.teamB.participant4
    if number == 4: return structedMatch.teamB.participant5
    if number == 5: return structedMatch.teamR.participant1
    if number == 6: return structedMatch.teamR.participant2
    if number == 7: return structedMatch.teamR.participant3
    if number == 8: return structedMatch.teamR.participant4
    if number == 9: return structedMatch.teamR.participant5
    else: return structedMatch.teamR.participant5

# Faz uma lista com todas as partidas que tal personagem jogou
# int -> list
def championMatchesToList(championID):
    championsMatches = []
    championName = c[championID]
    diretorio = './championsMatches/' + championName + '.bin'
    numberOfMatches = elementQtt(diretorio,4)
    with open(diretorio,'rb') as championMatchesFile:
        matchPositionBIN = championMatchesFile.read()
        matchPositionList = struct.unpack('I' * numberOfMatches,matchPositionBIN)
        championMatchesFile.close()
    return matchPositionList

# Informa quantos elementos de tal tamanho existem em tal diretorio
# path + size -> qtt
# str + int -> int
def elementQtt(directory,sizeEachElement):
    with open(directory,'ab') as directoryToTest:
        totalSize = directoryToTest.tell()
        elementQ = int(totalSize / sizeEachElement)
        directoryToTest.close()
        return elementQ


with open('matches.bin','rb') as matchesBIN:
    matchesBIN.seek(8)
    match1Bin = matchesBIN.read(matchSize)
    
    bina = struct.unpack(matchPSTR + teamPack + player*5 + teamPack + player * 5,match1Bin) #"explica" o formato do arquivo e desempacota
    p = binaryMatch(bina)
    matchesBIN.close()


# print(playerWon(champID,p))
diretorio = './championsMatches/' + 'Jax' + '.bin'
# print(elementQtt(diretorio,4))
# print(championMatchesToList(c["Jax"]))
# print("%.2f" % winrate('Irelia'))
##################
#     TESTES     #
##################
winrate('Amumu')
winrate('Caitlyn')
winrate('Rengar')
winrate('Volibear')
winrate('Jax')
winrate('Janna')
winrate('Lulu')
winrate('Fiora')
winrate('Morgana')
winrate('Veigar')
winrate('Fiora')
firstDragonPrc('Yasuo')
firstDragonPrc('Lissandra')
firstDragonPrc('Amumu')
firstDragonPrc('Janna')
firstDragonPrc('Darius')
# print(AnnieList)
def testeLoopAnnie():
    with open('matches.bin','rb') as AnnieFile:
        for game in AnnieList:
            posicao = game * matchSize
            AnnieFile.seek(posicao + 8)
            matchBinary = AnnieFile.read(matchSize)
            matchTuple = struct.unpack(matchPSTR + teamPack + player*5 + teamPack + player * 5,matchBinary) 
            game = AnnieList[1]
            print(matchTuple)
            print (posicao)

def testeStruc():
    with open('matches.bin','rb') as AnnieFile:
        for game in AnnieList:
            posicao = game * matchSize
            AnnieFile.seek(posicao + 8)
            matchBinary = AnnieFile.read(matchSize)
            matchTuple = struct.unpack(matchPSTR + teamPack + player*5 + teamPack + player * 5,matchBinary) 
            maa = binaryMatch(matchTuple)
            print(maa.gameId)

# testeStruc()
# testeLoopAnnie()
# print(winrate('LeeSin'))
# print(CS('LeeSin'))
# with open('matches.bin','rb') as matchtst:
    # matchtst.seek(8)
    # binM = matchtst.read(matchSize)
    # stuple = struct.unpack(matchPSTR + teamPack + player*5 + teamPack + player * 5,binM) 
    # maa = binaryMatch(stuple)
    # print(maa.gameId)
    # print(maa.teamB.participant1.championId)
    # print(maa.teamB.participant1.kills)

def testeAnnie():
    with open('matches.bin','rb') as AnnieFile:
        # for game in AnnieL ist:
        game = AnnieList[0]
        posicao = game * matchSize
        AnnieFile.seek(posicao + 8)
        matchBinary = AnnieFile.read(matchSize)
        matchTuple = struct.unpack(matchPSTR + teamPack + player*5 + teamPack + player * 5,matchBinary) 
        print(matchTuple)

        game = AnnieList[1]
        posicao = game * matchSize
        AnnieFile.seek(posicao + 8)
        matchBinary = AnnieFile.read(matchSize)
        matchTuple = struct.unpack(matchPSTR + teamPack + player*5 + teamPack + player * 5,matchBinary) 
        print(matchTuple)

        game = AnnieList[2]
        posicao = game * matchSize
        AnnieFile.seek(posicao + 8)
        matchBinary = AnnieFile.read(matchSize)
        matchTuple = struct.unpack(matchPSTR + teamPack + player*5 + teamPack + player * 5,matchBinary) 
        print(matchTuple)
     # print('Kills = ',strucMatch.teamB.participant1.kills)
# Declaracao da classe se encontra em bytesClasses.py
# p = binaryMatch(bu) # variavel p se transforma numa classe que contem todas informacoes de uma partida

# for i in range(10,30):
    # offset = i * matchSize + 2
    # with open('matches.bin', 'rb') as binaryFILE: # Abre o bin.bin, arquivo gerado pelo empacota.py
        # binaryFILE.seek(offset)
        # binary = binaryFILE.read(matchSize)
        # matchTuple = struct.unpack(matchPSTR + teamPack + player*5 + teamPack + player * 5,binary) 
        # match = binaryMatch(matchTuple)
        # print(match.teamB.participant1.championId)
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

