import sys
import json
import queue
import time

from APIrequests import *

#######
# ETC #
#######
# Deixa a chave da API em um outro arquivo para impedir que esta seja exposta no GitHub.
keyFile = open("apiKey.txt", 'r')

key = keyFile.read() # Le o arquivo
key = key.rstrip()   # Remove o \n
api_key = "api_key=" + key # Finaliza a chave que será usada nas requests

#######################
# FUNCOES PARA O LOOP #
#######################
# Funcoes que permitem pegar varias partidas

# Recebe um match history e coloca 20 partidas na queue
# JSON -> Fila
def put20MatchesFromMH(matchH):
    for i in range(0,20):
        match = getMatchFMH(matchH,i)
        match = getMatchIDFMH(match)
        matchQueue.put(match)


########
# MAIN #
########

# matchQueue = queue.Queue(maxsize=6000)
# matchQueue.put(1773189583)
# TO-DO: COLOCAR PARTIDAS DE TODOS OS ELOS NA QUEUE

# match = getMatchInfo(str(matchQueue.get())) # Pega partida da fila
# summoner = getSummoner(match,8) # Pega um summoner aleatorio da partida
# accID = getPlayerAccountId(summoner) # Pega o ID do summoner
# matchH = getSummonerMatchHistory(accID) # Pega o historico de partidas do summoner
# put20MatchesFromMH(matchH) # Coloca 20 partidas do jogador na fila
# print(json.dumps(match, indent=4, sort_keys=False))

 # Esboco loop
# match = matchQueue.get()
# match = matchQueue.get()
# match = matchQueue.get()
# match = getMatchInfo(str(matchQueue.get())) # Pega partida da fila
# accID = getPlayerAccountId(summoner) # Pega o ID do summoner
# summoner = getSummoner(match,2) # Pega um summoner aleatorio da partida
# matchH = getSummonerMatchHistory(accID) # Pega o historico de partidas do summoner
# put20MatchesFromMH(matchH) # Coloca 20 partidas do jogador na fila

# matchQueueSize = matchQueue.qsize()
# for i in range(0, matchQueueSize):
    # print(matchQueue.get())

# print(json.dumps(matchH["matches"][1], indent=4, sort_keys=False))
# for player in match["participantIdentities"]:
    # print(json.dumps(player, indent=4, sort_keys=False))

####################
# SALVA EM ARQUIVO #
####################

# with open('output.json', 'w') as json_file:
    # json.dump((match, indent=4,sort_keys=True),json_file) 
