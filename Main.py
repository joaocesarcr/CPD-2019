import json
import queue
import time

#TODO
# DICIONARIO XXX
# Arquivo para todos personagens XXX
# B TREE

# FUNCOES DE PESQUISA

from APIrequests import *
from  jsonManipulations import *
import timeControl
from writeChampioMatch import *
#######################
# FUNCOES PARA O LOOP #
#######################
# Funcoes que permitem pegar varias partidas
# Recebe um match history e coloca 20 partidas numa lista 
# JSON -> Lista
def matchHToList(matchH):
    matchList = ()
    for i in range(20):
        match = getMatchFMH(matchH,i)
        match = getMatchIDFMH(match)
        matchList.append(match)
    return matchList

#### Cria um dicionario se baseando no arquivo champion.json
# Possui Nome Personagem: ID
# ID : Nome Personagem
with open('champion.json', 'r') as cj:
data = json.load(cj)
data = data["data"]
c = {} for champion, d in data.items():
    c[int(d['key'])] = champion
    c[champion] = int(d['key'])
cj.close()

########
# MAIN #
########

# Abre o arquivo matches.bin permitindo que se escreva sem apagar os dados do arquivo
f = open('matches.bin', 'ab')

matchQueue = queue.Queue(maxsize=6000)
matchQueue.put(1773189583)
matchQueue.put(1798597502)
matchQueue.put(1798351256)
matchQueue.put(1799190427)
matchQueue.put(1799151530)
matchQueue.put(1798307715)
matchQueue.put(1798291968)
matchQueue.put(1795061493)
matchQueue.put(1794404902)

#### LOOP
for i in range(0):
    match = getMatchInfo(str(matchQueue.get())) # Pega partida da fila
    matchIDBin = struct.pack('L',match) # Transforma o ID da partida em binario para escrever na lista invertida dos campeoes
    if (match): # Verifica se a partida nao esta vazia
        for j in range(0):
            summoner = getSummoner(match,j) # Roda pelos 10 jogadores da partida
            if (summoner): # Checa se a informacao recebida pela API é válida
                summonerID = getPlayerAccountId(summoner) # Pega o ID dos jogadores para conseguir acessar o historico de partidas
                summonerMatchH = getSummonerMatchHistory(accID) # Pega o historico de partidas dos jogadores em JSON
                matchList = matchHToList(summonerMatchH) 
                for match in matchList:
                    #### ESBOCO PARA A B TREE
                    # if (consultaBtree(k):
                    # se esta, matchH.remove(match)
                    
                    # se nao esta, segue normalmente
                    # queue.put(match)
        fulP = fullPack(match)
        f.write(fullP)

        championsList = getMatchChampions(match) # Pega uma lista com todos os personagens da partida
        for champion in championsList:
            diretorio = './championsMatches/'+ c[champion] + '.bin'
            with open(diretorio, 'a+') as championFile:
                championFile.write(matchIDBin)
            championFile.close()
f.close()

#### Funcoes teste
# matchQueueSize = matchQueue.qsize()
# print(matchQueueSize)
# for i in range(0, matchQueueSize):
    # print(matchQueue.get())
# with open('output.json', 'w') as json_file:
    # json.dump((match, indent=4,sort_keys=True),json_file) 
# sys.exit()
