import time
import json


teamKillsHeader = 33

class Team:
    def __init__(self, teamId: str, teamName: str, teamLeague: str):  
        self.teamId = teamId
        self.teamName = teamName
        self.teamLeague = teamLeague

    def convertToJson(self):
        return "zz"

    @staticmethod
    def teamExistsById(teamId, teams):
        for team in teams:
            if(team.teamId == teamId): return team
        #Se não encontrar time return false
        #Pra que eu comentei isso, LMAO

#A match vai ter uma tag e um id proprio, vai dar pra ver o outro lado do "TeamMatch" pela tag
class Match:
    def __init__(self, matchTag: str, matchLeague: str, split: str, date: str, teamName: str, teamId: str, matchDuration: int, result: int, kills: int, dragons: int, towers: int):
        
        self.matchTag = matchTag
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
    def matchExistsInList(matchTag, teamId, matches: []):
        #procura na lista se ja esta la, se esta retorna algo, se nao retorna nada
        for match in matches:
            if(match.matchTag == matchTag and match.teamId == teamId): return match

             
def createList(methodCall):
    list = []
    with open("2025_LoL_esports_match_data_from_OraclesElixir.csv", "r", encoding="utf-8") as file:
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

def retrieveNewData():
    url = "https://drive.google.com/drive/u/1/folders/1gLSw0RLjBbtaNy0dgnGQDAZOHIgCe-HH"
    output = "newData.csv"
    gdown.download(url, output)

def createJsonFile(list):
    jsonArray = []
    for item in range(len(list)):
        jsonArray[item] = json.dumps(item.__dict__)
    return jsonArray
        
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


if __name__ == "__main__":
    #Começo do processo puxando novos dados do drive e jogando no file newData.csv
    #retrieveNewData()
    print("Hi")

