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

matchQueue = queue.Queue(maxsize=6000)
matchQueue.put(1773189583)
# matchQueue.put(1798597502)
# matchQueue.put(1798351256)
# matchQueue.put(1799190427)
# matchQueue.put(1799151530)
# matchQueue.put(1798307715)
# matchQueue.put(1798291968)
# matchQueue.put(1795061493)
# matchQueue.put(1794404902)


# TO-DO: COLOCAR PARTIDAS DE TODOS OS ELOS NA QUEUE

match = getMatchInfo(str(matchQueue.get())) # Pega partida da fila
summoner = getSummoner(match,7) # Pega um summoner aleatorio da partida
accID = getPlayerAccountId(summoner) # Pega o ID do summoner
matchH = getSummonerMatchHistory(accID) # Pega o historico de partidas do summoner
put20MatchesFromMH(matchH) # Coloca 20 partidas do jogador na fila

 # Esboco loop
# match = matchQueue.get()
# match = getMatchInfo(str(matchQueue.get())) # Pega partida da fila
# accID = getPlayerAccountId(summoner) # Pega o ID do summoner
# summoner = getSummoner(match,2) # Pega um summoner aleatorio da partida
# matchH = getSummonerMatchHistory(accID) # Pega o historico de partidas do summoner
# put20MatchesFromMH(matchH) # Coloca 20 partidas do jogador na fila

matchQueueSize = matchQueue.qsize()
for i in range(0, matchQueueSize):
    print(matchQueue.get())

# sys.exit()
# print(json.dumps(matchH["matches"][1], indent=4, sort_keys=False))
# for player in match["participantIdentities"]:
    # print(json.dumps(player, indent=4, sort_keys=False))

####################
# SALVA EM ARQUIVO #
####################

# with open('output.json', 'w') as json_file:
    # json.dump((match, indent=4,sort_keys=True),json_file) 
