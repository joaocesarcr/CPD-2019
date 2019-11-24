
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

