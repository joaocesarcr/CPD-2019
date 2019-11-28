class binaryMatch:
    def __init__(self,bu):
        self.gameId = bu[0]
        self.gameDuration = bu[1]
        self.byteBoolean = bu[2]

        self.teamB = (binaryTeam(bu[3:145]))
        self.teamR = (binaryTeam(bu[145:285]))

class binaryTeam:
    def __init__(self,bt):
    # NAO PRECISA AVISAR O ID POIS A  ORDEM DO BYTE INDICARA QUAL TIME
        self.towerKills, self.inhibitorKills, self.baronKills, self.dragonKills, self.riftHeraldKills = bt[0:5]
        self.bans = bt[5:10]

        self.participant1 = (binaryParticipants(bt[10:38]))
        self.participant2 = (binaryParticipants(bt[38:64]))
        self.participant3 = (binaryParticipants(bt[64:90]))
        self.participant4 = (binaryParticipants(bt[90:116]))
        self.participant5 = (binaryParticipants(bt[116:142]))

class binaryParticipants:
    # Recebe binary player
    # POR SÓ RECEBER UM PLAYER E NAO A PARTIDA INTEIRA, A ORDEM DA LISTA É DIFERENTE DO QUE SE CHAMADA PELA PARTIDA INTEIRA
    def __init__(self,bp):
        # IN GAME STATS
        self.championId = bp[0]
        self.kills = bp[1] 
        self.deaths = bp[2] 
        self.assists = bp[3] 
        self.largestKS = bp[4] 
        self.largestMK = bp[5] 
        self.longTSL = bp[6] 
        self.doubleKills = bp[7] 
        self.tripleKills = bp[8] 
        self.quadraKills = bp[9] 
        self.pentaKills = bp[10]
        self.totalddtc = bp[11] 
        self.mddtc = bp[12] 
        self.pddtc = bp[13] 
        self.trueddtc = bp[14] 
        self.dmgObj = bp[15] 
        self.dmgTur = bp[16]
        self.visionscore = bp[17] 
        self.timeCCO = bp[18] 
        self.totalGold = bp[19] 
        self.turretKills = bp[20] 
        self.inhibKills = bp[21] 
        self.totalMinionsK = bp[22] 
        self.neutralMinionsK = bp[23] 
        self.neutralMinionsKTJ = bp[24] 
        self.neutralMinionsKEJ = bp[25] 
        self.champLevel = bp[26] 
        self.vwb = bp[27] 


