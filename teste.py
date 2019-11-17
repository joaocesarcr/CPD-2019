import requests
import json

#######
# ETC #
#######

key = ""   # coloque sua chave aqui
api_key = "?api_key=" + key

matchID =str(1773277412)


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

#Recebe o ID de um sumonner e retorna suas informacoes
# int -> json
def getSummonerInfo(sumID):
    URL = "https://br1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + sumID + api_key
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

# Recebe  as informacoes de um summoner e retorna seu tier e rank
# json -> string, string
def getRank5v5Solo(summonerInfo):
    for rank in summonerInfo:
        if (rank["queueType"] == "RANKED_SOLO_5x5"):
            tier = rank["tier"]
            rank = rank["rank"]
            return (tier,rank)
    return("Unranked", "Unranked")

##########
# TESTES #
##########

match = getMatchInfo(matchID)
summoner = getSummoner(match,1)
sumID = getSummonerID(summoner)
summonerInfo = getSummonerInfo(sumID)
getRank5v5Solo(summonerInfo)
print(json.dumps(match, indent=4, sort_keys=True))
# print(json.dumps(summonerInfo, indent=4, sort_keys=True))

# for playerIdt in match["participantIdentities"]:
    # sumID = getSummonerID(playerIdt)
    # summonerInfo = getSummonerInfo(sumID)
    # tier, rank = getRank5v5Solo(summonerInfo)
    # print(tier,rank)

####################
# SALVA EM ARQUIVO #
####################

# with open('output.json', 'w') as json_file:
        # json.dump(match,json_file) 

