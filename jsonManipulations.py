##################################################### # MANIPULACAO COM OS DADOS RECEBIDOS DE UMA REQUEST #
#####################################################
# Recebe um sumonner  de uma partida e retorna o seu ID
# int + int -> int
def getSummonerID(summoner):
    sumID = str(summoner["summonerId"])
    return sumID

# Recebe uma partida e um inteiro e retorna as informacoes do jogador na posicao int
# int + int -> json
def getSummoner(match, number):
    summoner = None
    if (match): summoner = match["participantIdentities"][number]
    return summoner
    
# Recebe uma partida e retorna uma lista com todos personagens da partida
# json -> list
def getMatchChampions(match):
    matchChampionsList = ()
    for player in match["participants"]:
        matchChampionsList.append(player["championId"])
    return matchChampionsList

# Recebe um sumonner  de uma partida e retorna o seu ID
# recebe um participant identities"
# json -> str
def getPlayerAccountId(summoner):
    accountID = summoner["player"]["currentAccountId"]
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

# Cria uma lista com os bans de um time
# match["teams"]
# json -> lista
def getBans(teamJSON):
    banList = []
    for ban in teamJSON["bans"]:
        banList.append(ban["championId"])
    return banList


