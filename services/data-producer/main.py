import time
import json
import gdown
from quixstreams import Application

csvDataUrl = "https://drive.google.com/file/d/1v6LRphp2kYciU4SXp0PCjEMuev1bDejc/view?usp=sharing"

brokerAddress = "localhost:9092"
teamsTopicName = "data_producer.teams.team_created.json"
matchesTopicName = "data_producer.matches.match_finished.json"

tempFile = "tempFile.csv"
newData = "newData.csv"
oldData = "oldData.csv"

teamKillsHeader = 33

class Team:
    def __init__(self, teamId: str, teamName: str, teamLeague: str):  
        self.teamId = teamId
        self.teamName = teamName
        self.teamLeague = teamLeague

    @staticmethod
    def teamExistsById(teamId, teams):
        for team in teams:
            if(team.teamId == teamId): return team
        #Se não encontrar time return false
        #Pra que eu comentei isso, LMAO

#A match vai ter uma tag e um id proprio, vai dar pra ver o outro lado do "TeamMatch" pela tag
class Match:
    def __init__(self, matchId: str, matchLeague: str, split: str, date: str, teamName: str, teamId: str, matchDuration: int, result: int, kills: int, dragons: int, towers: int):
        
        self.matchId = matchId
        self.matchLeague = matchLeague
        self.split = split
        self.date = date
        self.teamName = teamName
        self.teamId = teamId
        self.matchDuration = matchDuration
        self.result = result
        self.kills = kills
        self.dragons = dragons
        self.towers = towers

    @staticmethod
    def matchExistsInList(matchId, teamId, matches: []):
        #procura na lista se ja esta la, se esta retorna algo, se nao retorna nada
        for match in matches:
            if(match.matchId == matchId and match.teamId == teamId): return match

def retrieveNewCsvData(outputFilename):
    gdown.download(csvDataUrl, outputFilename, quiet=False, fuzzy=True)
             
def createList(filename, methodCall):
    list = []
    with open(filename, "r", encoding="utf-8") as file:
        #ignores the first line, that is the header of the file
        file.readline()

        for line in file:
            data = line.strip().split(",")
            methodCall(data, list)
            
    return list

def createTeamIfNotExists(teamData: [], teams: []):
    teamId = teamData[16]
    if not Team.teamExistsById(teamId, teams):
        teamName = teamData[15]
        teamLeague = teamData[3]
        teams.append(Team(teamId, teamName, teamLeague))

def createMatchIfNotExists(matchData: [], matches: []):
    matchTag = matchData[0]
    teamId = matchData[16]
    if not Match.matchExistsInList(matchTag, teamId, matches):
        try:
            matchLeague = matchData[3]
            split = matchData[5]
            date = matchData[7]
            teamName = matchData[15]
            matchDuration = int(matchData[28])
            result = int(matchData[29])
            kills = int(matchData[33]) + int(matchData[34])
            dragons = int(matchData[46]) + int(matchData[47])
            towers =  int(matchData[70]) + int(matchData[71])
            matches.append(Match(matchTag, matchLeague, split, date, teamName, teamId, matchDuration, result, kills, dragons, towers))
        except ValueError:
            return False

def sendMessages(list, topicName):
    app = Application(broker_address = brokerAddress)

    with app.get_producer() as producer:
        for item in list:
            producer.produce(
                topic = topicName,
                value = json.dumps(item.__dict__)
            )
        
#Se newData e oldData forem iguais é retornado falso
def createFileWitouthDuplicates(newFileName, fileOneName, fileTwoName):
    linesFile1 = set()
    with open(fileOneName, "r", encoding="utf-8") as tempFile:
        for line in tempFile:
            linesFile1.add(line.strip())

    linesFile2 = set()
    with open(fileTwoName, "r", encoding="utf-8") as tempFile:
        for line in tempFile:
            linesFile2.add(line.strip())

    uniqueLines = linesFile1.symmetric_difference(linesFile2)
    if len(uniqueLines) < 1:
        return False
    
    with open(newFileName, "w", encoding="utf-8") as tempFile:
        for line in uniqueLines:
            tempFile.write(line + "\n")
    return True


if __name__ == "__main__":
    

#Cada jogo ser uma mensagem enternamente em um topic
#Cada time ser uma mensagem enternamente em outro topic
#O jogo tem que ser o responsavel por guardar uma mensagem para o time
#A leitura e o recebimento das mensagens do time tem que sempre acontecer antes do que a dos jogos
#Meu medo no caso é um jogo ter a referencia de um time que ainda nao foi criado, mas vou deixar pra pensar
#nesse problema depois

#Reader of a given partition consumes messages in the order they are published

#O jogo tem uma PK composta, nela vai ter o id do jogo (que nao é unico) e a PK do time a qual pertence esse jogo
