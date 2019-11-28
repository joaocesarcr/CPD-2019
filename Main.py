import sys
import json
import queue
import time

from APIrequests import *
from  jsonManipulations import *
import timeControl
#######################
# FUNCOES PARA O LOOP #
#######################
# Funcoes que permitem pegar varias partidas
# Recebe um match history e coloca 20 partidas na queue
# JSON -> Fila
def put20MatchesFromMH(matchH):
    for i in range(20):
        match = getMatchFMH(matchH,i)
        match = getMatchIDFMH(match)
        matchQueue.put(match)
########
# MAIN #
########

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
for i in range(100):
    match = getMatchInfo(str(matchQueue.get())) # Pega partida da fila
    if (match):
        for j in range(9):
            summoner = getSummoner(match,j) # Roda pelos 10 jogadores da partida
            if (summoner): 
                accID = getPlayerAccountId(summoner) # Pega o ID dos jogadores para conseguir acessar o historico de partidas
                time.sleep(0.3)
                matchH = getSummonerMatchHistory(accID) # Pega o historico de partidas dos jogadores
                #############################
                # BOTAR O TESTE COM A B TREE #
                if (matchH): put20MatchesFromMH(matchH) # Coloca 20 partidas de cada jogador na fila
        ######
        # COLOCAR O ENPACOTADOR PARA BINARIO AQUI
        #####
        fulP = fullPack(match)
        f.write(fullP)
        ####
        # CRIA ARQUIVO OU ADICIONA PARTIDA A LISTA INVERTIDA
f.close()

#### Funcoes teste
# matchQueueSize = matchQueue.qsize()
# print(matchQueueSize)
# for i in range(0, matchQueueSize):
    # print(matchQueue.get())
# with open('output.json', 'w') as json_file:
    # json.dump((match, indent=4,sort_keys=True),json_file) 
# sys.exit()


