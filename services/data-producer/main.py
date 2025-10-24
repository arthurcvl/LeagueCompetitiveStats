import time
import os
import json
import gdown
from quixstreams import Application

csvDataUrl = "https://drive.google.com/file/d/1v6LRphp2kYciU4SXp0PCjEMuev1bDejc/view?usp=sharing"

'''matchTag = 0
matchLeague = 3
split = 5
date = 7
teamName = 15
teamId = 16
matchDuration = 28
result = 29
kills = 33 (teamkills) + 34 (teamdeaths)
dragons = 46 (owndragons) + 47(oppdragons)
towers = 70(owntowers) + 71(opptowers)'''

brokerAddress = "kafka:9092"
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

class Match:
    def __init__(self, matchId: str, matchLeague: str, split: str, date: str, teamId: str, matchDuration: int, result: int, kills: int, dragons: int, towers: int):
        
        self.matchId = matchId
        self.matchLeague = matchLeague
        self.split = split
        self.date = date
        self.teamId = teamId
        self.matchDuration = matchDuration
        self.result = result
        self.kills = kills
        self.dragons = dragons
        self.towers = towers

    @staticmethod
    def matchExistsInList(matchId, teamId, matches: []):
        #search in list, if is return the match, if not return nothing, this is useful to if
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
            matchDuration = int(matchData[28])
            result = int(matchData[29])
            kills = int(matchData[33]) + int(matchData[34])
            dragons = int(matchData[46]) + int(matchData[47])
            towers =  int(matchData[70]) + int(matchData[71])
            matches.append(Match(matchTag, matchLeague, split, date, teamId, matchDuration, result, kills, dragons, towers))
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
        
#If newData and oldData are equals return false
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

def main():
    #Download new data
    retrieveNewCsvData(newData) 

    if not createFileWitouthDuplicates(tempFile, newData, oldData): 
        print("There is no new Data") 
        return False 

    newTeams = createList(tempFile, createTeamIfNotExists) 
    newMatches = createList(tempFile, createMatchIfNotExists) 

    if len(newTeams) > 0: 
        sendMessages(newTeams, teamsTopicName) 

    if len(newMatches) > 0: 
        sendMessages(newMatches, matchesTopicName)

    #Deletes all data inside oldData
    open(newData, 'w').close()

    #Swap newData -> oldData and oldData -> newData
    os.rename(newData, 'temp')
    os.rename(oldData, newData)
    os.rename('temp', oldData)

def test():
    if not createFileWitouthDuplicates(tempFile, newData, oldData): 
        print("There is no new Data") 
        return False 

    newTeams = createList(tempFile, createTeamIfNotExists) 

    if len(newTeams) > 0: 
        sendMessages(newTeams, teamsTopicName) 


if __name__ == "__main__":
    test()