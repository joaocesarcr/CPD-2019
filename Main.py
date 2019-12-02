import json
import time

# Local Files
from apiRequests import *
from  jsonManipulations import *
import timeControl
from btree import *
from jsonToFile import *

#TODO
# DICIONARIO XXX
# TRANSFORMAR LISTA DE PARTIDAS EM ARQUIVO BINARIO XXX
# Arquivo para todos personagens XXX
# B TREE XXX
# E SE NAO TIVER 20 partidas rankeadas? XXX
# ESCREVER O NUMERO DE PARTIDAS TOTAIS E O NUMERO DE PARTIDAS DA SESSAO. XXX
# TERMINAR DE ESCREVER AS PARTIDAS NA FILA EM UM ARQUIVO XXX

# ORGANIZAR A ESPERA DE TEMPO/NEM SEMPRE ADICIONAR PARTIDAS DE UM MH


#######################
# FUNCOES PARA O LOOP #
#######################
# Funcoes que permitem pegar varias partidas
# Recebe um match history e coloca 20 partidas numa lista 
# JSON -> Lista

print('Inicializando...')
# TODO: NAO USAR ESTA FUNCAO
def matchHToList(matchH):
    matchList = []
    matchList = getMatchFMH(matchH)
    return matchList

################
# Le quantas partidas já foram escritas
with open('matchesnumber.bin', 'rb') as nOfMatchesFile:
    nofmBIN = nOfMatchesFile.read()
    totalMatchesWritten = struct.unpack('L',nofmBIN)
    totalMatchesWritten = totalMatchesWritten[0]
nOfMatchesFile.close()

# Le quantas partidas estao na fila param serem escritas
with open('matchestosearch.bin', 'ab') as matchesListFile:
    numberOfBytes = matchesListFile.tell()
    numberOfMatches = int(numberOfBytes / 8)
matchesListFile.close()

with open('matchestosearch.bin', 'rb') as matchesListFile:
    bytesFromFile = matchesListFile.read()
    matchesToSearch = struct.unpack(numberOfMatches * 'L',bytesFromFile)
    matchesToSearch = list(matchesToSearch)
matchesListFile.close()

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

    

########
# MAIN #
########
print('Total de partidas escritas =', totalMatchesWritten)

print('Começo Loop...')

raiz = nodo_btree(0, btree_matchs)
#######
# O programa toda até a comando CTRL-C ser utilizado
#
i = 0 # TOTAL DE PARTIDAS COLETADAS DESDE O INICIO DO PROGRAMA

matchList = matchesToSearch

try:
    while True:
        print("Don't stop now")
        print(matchList)
        match = getMatchInfo(str(matchList.pop(0))) # Pega partida da fila RETONAR JSON
        time.sleep(1)

        if (match): # Verifica se a partida nao esta vazia
            matchID = (match["gameId"] % 10000)
            print('MachID =',matchID)
            for player in range(10):
                summoner = getSummoner(match,player) # Roda pelos 10 jogadores da partida
                if (summoner): # Checa se a informacao recebida pela API é válida
                    if (len(matchList) < 200):  
                        summonerID = getPlayerAccountId(summoner) # Pega o ID dos jogadores para conseguir acessar o historico de partidas
                        time.sleep(1)
                        summonerMatchH = getSummonerMatchHistory(summonerID) # Pega o historico de partidas dos jogadores em JSON
                        time.sleep(1)
                        matchList = matchList + (getMatchFMH(summonerMatchH))
                else: 
                    print('TIME OUT!!!')
                    time.sleep(120)

            structedMatch = Match(match)
            if (raiz.insert_raiz(0, matchID, totalMatchesWritten + i, 'btree_matchs')): # ESCRITA COM SUCESSO
                with open('matches.bin', 'ab') as f:
                    fulP = fullPack(structedMatch)
                    f.write(fulP)
                    f.close()

                championsList = getMatchChampions(match) # Pega uma lista com todos os personagens da partida
                matchIDBin = struct.pack('L',matchID) # Transforma o ID da partida em binario para escrever na lista invertida dos campeoes
                for champion in championsList:
                    diretorio = './championsMatches/'+ c[champion] + '.bin'
                    with open(diretorio, 'ab+') as championFile:
                        championFile.write(matchIDBin)
                    championFile.close()

                i = i + 1

                with open('matchesnumber.bin', 'wb+') as totalMatches:
                    totalMatchesBin = struct.pack('L',totalMatchesWritten + i)
                    totalMatches.write(totalMatchesBin)
                totalMatches.close()

            else:
                print('PARTIDA REPETIDA')

        else:
            print('Couldnt find match')
            time.sleep(120)

        print('{} Matches written'.format(i))
        print('Good time to stop')
        time.sleep(3)

except KeyboardInterrupt:
    print('Finishing...')
    time.sleep(3)
    print('{} Matches written in this session'.format(i))

    totalMatchesWritten = totalMatchesWritten + i
    print('{} Total matches written'.format(totalMatchesWritten))
    with open('matchesnumber.bin', 'wb+') as totalMatches:
        totalMatchesBin = struct.pack('L',totalMatchesWritten)
        totalMatches.write(totalMatchesBin)
    totalMatches.close()

    with open('matchestosearch.bin', 'wb') as matchestosearchFile:
        for match in matchList:
            matchBin = struct.pack('L',int(match))
            matchestosearchFile.write(matchBin)
    matchestosearchFile.close()
    print('Done!')
        
#### Funcoes teste
# for i in range(0, matchQueueSize):
    # print(matchQueue.get())
# with open('output.json', 'w') as json_file:
    # json.dump((match, indent=4,sort_keys=True),json_file) 
# sys.exit()
