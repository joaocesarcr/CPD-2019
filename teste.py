import sys
import requests
import json
import queue
import time

#######
# ETC #
#######
# Deixa a chave da API em um outro arquivo para impedir que esta seja exposta no GitHub.
keyFile = open("apiKey.txt", 'r')

key = keyFile.read() # Le o arquivo
key = key.rstrip()   # Remove o \n
api_key = "api_key=" + key # Finaliza a chave que será usada nas requests

################
# TIME CONTROL #
################
# 20 requests every 1 seconds(s)
# 100 requests every 2 minutes(s)

# Recebe uma funcao e um parametro para ser utilizado nela. Retorna o tempo de decorrimento da funcao e seu retorno
# str + generic -> int, generic
# TO-D0 : Transformar parameter em uma lista
def functionTime(functionName, parameter):
    initTime = time.time()
    retorno = functionName(parameter)
    endTime = time.time()
    return (endTime - initTime), retorno

########################
# MANIPULACAO COM HTML #
########################

# Informa se ocorrou algum erro na request
# Caso tenha ocorrido, o status_code será maior ou igual a 400
def requestError(response):
    if (response.status_code >= 400): return True
    else: return False

# match v4
# Recebe o ID de uma partida e retorna um json com todas as informacoes
# int -> json
def getMatchInfo(matchID):
    URL = "https://br1.api.riotgames.com/lol/match/v4/matches/" + matchID + "?" + api_key
    response = requests.get(URL)
    if requestError(response): return None
    else: return response.json()


# Recebe um account id e retorna seu historico de partidas contendo apenas partidas rankeadas
# String -> json
def getSummonerMatchHistory(accountid):
    URL = "https://br1.api.riotgames.com/lol/match/v4/matchlists/by-account/" + accountid + "?queue=420&" + api_key
    response = requests.get(URL)
    if requestError(response): return None
    else: return response.json()

#####################################################
# MANIPULACAO COM OS DADOS RECEBIDOS DE UMA REQUEST #
#####################################################
# Recebe um sumonner  de uma partida e retorna o seu ID
# int + int -> int
def getSummonerID(summoner):
    sumID = str(summoner["summonerId"])
    return sumID

# Recebe uma partida e um inteiro e retorna as informacoes do jogador na posicao int
# int + int -> json
def getSummoner(match, number):
    summoner = match["participantIdentities"][number]
    return summoner
    
# Recebe um sumonner  de uma partida e retorna o seu ID
# int + int -> int
def getPlayerAccountId(summoner):
    accountID = summoner["player"]["accountId"]
    return accountID 

# Get match from match history
# Recebe um historico de partidas e uma posicao e retorna a partida a posicao number
# json + int -> json
def getMatchFMH(matchHistory, number):
    return matchHistory["matches"][number]

# Get match ID from a match in match history
# Recebe uma partida de um historico de partidas e retorna seu ID
# json -> int 
def getMatchIDFMH(matchFMH):
    return matchFMH["gameId"]

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
matchQueue = queue.Queue(maxsize=6000)
matchQueue.put(1773189583)
#TO-DO: COLOCAR PARTIDAS DE TODOS OS ELOS NA QUEUE

match = getMatchInfo(str(matchQueue.get())) # Pega partida da fila
summoner = getSummoner(match,8) # Pega um summoner aleatorio da partida
accID = getPlayerAccountId(summoner) # Pega o ID do summoner
matchH = getSummonerMatchHistory(accID) # Pega o historico de partidas do summoner
put20MatchesFromMH(matchH) # Coloca 20 partidas do jogador na fila
#print(json.dumps(match, indent=4, sort_keys=False))
sys.exit()


# Esboco loop
match = matchQueue.get()
match = matchQueue.get()
match = matchQueue.get()
match = getMatchInfo(str(matchQueue.get())) # Pega partida da fila
accID = getPlayerAccountId(summoner) # Pega o ID do summoner
summoner = getSummoner(match,2) # Pega um summoner aleatorio da partida
matchH = getSummonerMatchHistory(accID) # Pega o historico de partidas do summoner
put20MatchesFromMH(matchH) # Coloca 20 partidas do jogador na fila

matchQueueSize = matchQueue.qsize()
for i in range(0, matchQueueSize):
    print(matchQueue.get())

# print(json.dumps(matchH["matches"][1], indent=4, sort_keys=False))
# for player in match["participantIdentities"]:
    # print(json.dumps(player, indent=4, sort_keys=False))

####################
# SALVA EM ARQUIVO #
####################

# with open('output.json', 'w') as json_file:
    # json.dump((match, indent=4,sort_keys=True),json_file) 
