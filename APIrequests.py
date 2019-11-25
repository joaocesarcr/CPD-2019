import requests
#######
# KEY #
#######
# Deixa a chave da API em um outro arquivo para impedir que esta seja exposta no GitHub.
keyFile = open("apiKey.txt", 'r')

key = keyFile.read() # Le o arquivo key = key.rstrip()   # Remove o \n
api_key = "api_key=" + key # Finaliza a chave que será usada nas requests
api_key = api_key.rstrip()

########################
# MANIPULACAO COM HTML #
########################

# Informa se ocorreu algum erro na request
# Caso tenha ocorrido, o status_code será maior ou igual a 400
def requestError(response):
    if (response.status_code >= 400): return True
    else: return False

# match v4
# Recebe o ID de uma partida e retorna um json com todas as informacoes
# int -> json
def getMatchInfo(matchID):
    URL = "https://br1.api.riotgames.com/lol/match/v4/matches/" + str(matchID) + "?" + api_key
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
