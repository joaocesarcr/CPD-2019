import sys
import requests
import json
import time

#######
# ETC #
#######
# Deixa a chave da API em um outro arquivo para impedir que esta seja exposta no GitHub.
keyFile = open("apiKey.txt", 'r')

key = keyFile.read() # Le o arquivo
key = key.rstrip()   # Remove o \n
api_key = "?api_key=" + key # Finaliza a chave que será usada nas requests
matchID =str(1773189583)

################
# TIME CONTROL #
################
# 20 requests every 1 seconds(s)
# 100 requests every 2 minutes(s)

# Recebe uma funcao e um parametro para ser utilizado nela. Retorna o tempo de decorrimento da funcao e seu retorno
# str + generic -> int, generic
def functionTime(functionName, parameter):
    initTime = time.time()
    retorno = functionName(parameter)
    endTime = time.time()
    return (endTime - initTime), retorno

########################
# MANIPULACAO COM HTML #
########################

# match v4
# Recebe o ID de uma partida e retorna um json com todas as informacoes
# int -> json

def getMatchInfo(matchid):
    URL = "https://br1.api.riotgames.com/lol/match/v4/matches/" + matchID + api_key
    response = requests.get(URL)
    return response.json()

#####################################################
# MANIPULACAO COM OS DADOS RECEBIDOS DE UMA REQUEST #
#####################################################

 # Recebe uma partida e um inteiro e retorna as informacoes do jogador na posicao int
 # int + int -> json
def getSummoner(match, number):
    summoner = match["participantIdentities"][number]
    return summoner
    
# Recebe um sumonner  de uma partida e retorna o seu ID
# int + int -> int
def getSummonerID(summoner):
    sumID = str(summoner["player"]["summonerId"])
    return sumID


##########
# TESTES #
##########

tempoDecorrido, retorno = functionTime(getMatchInfo, matchID)
match = getMatchInfo(matchID)
print(json.dumps(match, indent=4, sort_keys=True))
sys.exit()
summoner = getSummoner(match,1)
sumID = getSummonerID(summoner)
summonerInfo = getSummonerInfo(sumID)
print(json.dumps(match, indent=4, sort_keys=True))

####################
# SALVA EM ARQUIVO #
####################

# with open('output.json', 'w') as json_file:
        # json.dump(match,json_file) 

