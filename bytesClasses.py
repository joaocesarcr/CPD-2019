# Partida vai até 292
# 3 primeiros sao informacoes da partida
# proximos 10 sao informacoes do time
# proximos 27 * 5 sao informacoes dos jogadores
class binaryMatch:
    def __init__(self,bu):
        self.gameId = bu[0]
        self.gameDuration = bu[1]
        self.byteBoolean = bu[2]

        self.teamB = (binaryTeam(bu[3:148])) # 10 bits time, 27 * 5 players = 145
        self.teamR = (binaryTeam(bu[148:293]))
class binaryTeam:
    def __init__(self,bt):
    # NAO PRECISA AVISAR O ID POIS A  ORDEM DO BYTE INDICARA QUAL TIME
        self.towerKills, self.inhibitorKills, self.baronKills, self.dragonKills, self.riftHeraldKills = bt[0:5]
        self.bans = bt[5:10]

        self.participant1 = (binaryParticipants(bt[10:37]))
        self.participant2 = (binaryParticipants(bt[37:64]))
        self.participant3 = (binaryParticipants(bt[64:91]))
        self.participant4 = (binaryParticipants(bt[91:118]))
        self.participant5 = (binaryParticipants(bt[118:145]))

class binaryParticipants:
    # Recebe binary player
    # POR SÓ RECEBER UM PLAYER E NAO A PARTIDA INTEIRA, A ORDEM DA LISTA É DIFERENTE DO QUE SE CHAMADA PELA PARTIDA INTEIRA
    def __init__(self,bp):
        # IN GAME STATS
        self.championId = bp[0]
        self.kills = bp[1] 
        self.deaths = bp[2] 
        self.largestKS = bp[3] 
        self.largestMK = bp[4] 
        self.longTSL = bp[5] 
        self.doubleKills = bp[6] 
        self.tripleKills = bp[7] 
        self.quadraKills = bp[8] 
        self.pentaKills = bp[9]
        self.totalddtc = bp[10] 
        self.mddtc = bp[11] 
        self.pddtc = bp[12] 
        self.trueddtc = bp[13] 
        self.dmgObj = bp[14] 
        self.dmgTur = bp[15]
        self.visionscore = bp[16] 
        self.timeCCO = bp[17] 
        self.totalGold = bp[18] 
        self.turretKills = bp[19] 
        self.inhibKills = bp[20] 
        self.totalMinionsK = bp[21] 
        self.neutralMinionsK = bp[22] 
        self.neutralMinionsKTJ = bp[23] 
        self.neutralMinionsKEJ = bp[24] 
        self.champLevel = bp[25] 
        self.vwb = bp[26] 
