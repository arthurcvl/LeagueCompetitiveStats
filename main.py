import numpy


from lck import *
from lpl import *
from lec import *
from lcs import *


def read_csv_file():
    games = []
    with open("2024_LoL_esports_match_data_from_OraclesElixir.csv", "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            game = line.strip().split(",")
            index = [1, 2, 4, 10, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 30, 31, 32, 35, 36,
                       37, 38, 39, 40, 41, 42, 45, 50, 51, 52, 53, 54, 55, 57, 59, 60, 61, 62, 63, 70, 71, 72, 73, 76,
                       77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100,
                       101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119,
                       120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130]

            index.sort(reverse=True)
            for ind in index:
                game.pop(ind)

            games.append(game)
    return games

def items():
    stat = ["gameid","datacompleteness","url","league","year","split","playoffs","date","game","patch","participantid",
           "side","position",'playername',"playerid","teamname","teamid","champion","ban1","ban2","ban3","ban4","ban5",
           "pick1","pick2","pick3","pick4","pick5","gamelength","result","kills","deaths","assists","teamkills",
           "teamdeaths","doublekills","triplekills","quadrakills","pentakills","firstblood","firstbloodkill",
           "firstbloodassist","firstbloodvictim","team" "kpm","ckpm","firstdragon","dragons","opp_dragons",
           "elementaldrakes","opp_elementaldrakes","infernals","mountains","clouds","oceans","chemtechs","hextechs",
           "dragons","elders","opp_elders","firstherald","heralds","opp_heralds","void_grubs","opp_void_grubs",
           "firstbaron","barons","opp_barons","firsttower","towers","opp_towers","firstmidtower","firsttothreetowers",
           "turretplates","opp_turretplates","inhibitors","opp_inhibitors","damagetochampions","dpm","damageshare",
           "damagetakenperminute","damagemitigatedperminute","wardsplaced","wpm","wardskilled","wcpm",
           "controlwardsbought","visionscore","vspm","totalgold","earnedgold","earned gpm","earnedgoldshare",
           "goldspent","gspd","gpr","total cs","minionkills","monsterkills","monsterkillsownjungle",
           "monsterkillsenemyjungle","cspm","goldat10","xpat10","csat10","opp_goldat10","opp_xpat10","opp_csat10",
           "golddiffat10","xpdiffat10","csdiffat10","killsat10","assistsat10","deathsat10","opp_killsat10",
           "opp_assistsat10","opp_deathsat10","goldat15","xpat15","csat15","opp_goldat15","opp_xpat15","opp_csat15",
           "golddiffat15","xpdiffat15","csdiffat15","killsat15","assistsat15","deathsat15","opp_killsat15",
           "opp_assistsat15","opp_deathsat15"]
    index = [1, 2, 4, 10, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 30, 31, 32, 35, 36,
               37, 38, 39, 40, 41, 42, 45, 50, 51, 52, 53, 54, 55, 57, 59, 60, 61, 62, 63, 70, 71, 72, 73, 76,
               77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100,
               101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119,
               120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130]

    index.sort(reverse=True)
    for i in index:
        stat.pop(i)

    for data in stat:
        print("{} - {}".format(stat.index(data),data))


def add_data(stats, team):
    for game in stats:
        if game[8] == team["name"]:
            kills = int(game[11]) + int(game[12])
            if game[15] and game[16]:
                dragons = int(game[15]) + int(game[16])
            else:
                dragons = 0
            if game[22] and game[23]:
                barons = int(game[22]) + int(game[23])
            else:
                barons = 0
            if game[25] and game[26]:
                towers = int(game[25]) + int(game[26])
            else:
                towers = 0
            if game[27] and game[28]:
                inhibitors = int(game[27]) + int(game[28])
            else:
                inhibitors = 0
            team[game[0]] = {
                "gameid": game[0],
                "Split": game[2],
                "Playoffs": game[3],
                "Patch": game[6],
                "Side": game[7],
                "Data": game[4],
                "Time": int(game[9]),
                "Winner": game[10],
                "Kill": kills,
                "Dragon": dragons,
                "Baron": barons,
                "Tower": towers,
                "Inhibitors": inhibitors,

            }


def average(data, stat):
    for game in data:
        if game != "name":
            try:
                data[game][stat]
            except:
                print("Stat: {} not found!".format(stat))
                return None
    average = []
    for game in data:
        if game != "name":
            average.append(data[game][stat])
    if stat == "Time":
        time = float(numpy.mean(average))
        minute, second = divmod(time, 60)
        print("{} - {}:{} {} on average\n".format(data["name"], int(minute), int(second), "minutes"))
    else:
        print("{} - {} {} on average\n".format(data["name"], round(float(numpy.mean(average)), 1), stat))

    games = []
    patchs = []
    index = []
    for game in data:
        if game != "name":
            if data[game]["Patch"] not in patchs:
                patchs.append(data[game]["Patch"])
            if data[game]["Patch"]:
                games.append(data[game]["Patch"])
    for patch in patchs:
        for game in data:
            if game != "name":
                if data[game]["Patch"] == patch:
                    index.append(data[game][stat])
        if stat == "Time":
            time = float(numpy.mean(index))
            minute, second = divmod(time, 60)
            print("Patch {} - ({}) games - {}:{} {}".format(patch, games.count(patch), int(minute), int(second), "minutes"))
            index.clear()
        else:
            print("Patch {} - ({}) games - {} {}".format(patch, games.count(patch), round(float(numpy.mean(index)), 1), stat))
            index.clear()


def relative_frequency(team, stat, lines, overunder):
    for game in team:
        if game != "name":
            try:
                team[game][stat]
            except:
                print("Stat: {} not found!".format(stat))
                return None
    if overunder == "under" or overunder == "over":
        l = lines.split(" ")
        for line in l:      
            try:
                float(line)
            except ValueError:
                print("Please only type numbers in lines of relative frequency")
                return None
            games = []
            correct = []
            patchs = []
            frequency = []
            if stat == "Time":
                minute, second = divmod(line, 60) 
            for game in team:
                    if jogo != "name":
                        if overunder == "over":
                            if team[game][stat] > line:
                                frequency.append(team[game][stat])
                        elif overunder == "under":
                            if team[game][stat] < line:
                                frequency.append(team[game][stat])
                        percentage = round((len(frequency) / (len(team) - 1)) * 100, 1)
            if stat == "Time":
                print("{} ({}:{}) - {}% of {} relative frequency \n".format(team["name"], int(minute), int(second), percentage, stat))
            else:
                print("{} ({}) {} - {}% of relative frequency".format(team["name"], line, stat, percentage))
            
            for game in team:
                if game != "name":
                    if team[game]["Patch"]:
                        if team[game]["Patch"] not in patchs:
                            patchs.append(team[game]["Patch"])
                        games.append(team[game]["Patch"])
            for patch in patchs:
                for game in team:
                    if game != "name":
                        if overunder == "over":
                            if team[game]["Patch"] == patch and team[game][stat] > line:
                                correct.append(team[game][stat])
                        elif overunder == "under":
                            if team[game]["Patch"] == patch and team[game][stat] < line:
                                correct.append(team[game][stat])
                if len(correct) > 0:
                    print("Patch {} - ({}) games - {}%".format(patch, games.count(patch),round((len(correct) / games.count(patch) * 100), 1)))
                elif len(correct) == 0:
                    print("Patch {} - ({}) games - {}%".format(patch, games.count(patch),0))

                correct.clear()
            marker()
    else:
        print("Please type if its over or under! ")

             

def interface():
    print("Type 1 to see what informations we are getting from each game")
    print("Type 2 to see teams name (atm you will need to type the full name to get data)")
    print("Type 3 to get the average from a team stat (tower, dragon, time, kills)")
    print("Type 4 to get the relative frequency of a team stat")
    print("Type 0 to close the program (or Ctrl + C)")
    marker()


def update_data():
    data = read_csv_file()
    for league in LCK, LPL, LEC, LCS:
        for team in league:
            add_data(data, team)

def show_teams():
    leagues = ["LCK", "LPL", "LEC", "LCS"]
    print("Currently teams: ")
    for league in LCK, LPL, LEC, LCS:
        print(leagues[0], "\n")
        leagues.pop(0)
        for team in league:
            print(team["name"])
        marker()

def get_team_stat():
    team = input("Type the name of the team: ")
    team2 = input ("Type another team name (Opcional choice): ")
    stat = input("Type the stat you wanna get: ")

    return team, team2, stat

def marker():
    print("----------------------------------------------------------------")

if __name__ == "__main__":
    update_data()
    while True:
        interface()
        choice = input("Type here: ")
        marker()
        if choice == "1":
            items()
            marker()
        elif choice == "2":   
            mostrar_times_liga()
        elif choice == "3":
            team, team2, stat = get_team_stat()
            marker()
            for league in LCK, LPL, LEC, LCS:
                for squad in league:
                    if team == squad["name"]:
                        average(squad, stat)
                        marker()
            if team2:
                for league in LCK, LPL, LEC, LCS:
                    for squad in league:
                        if team2 == squad["name"]:
                            average(squad, stat)
                            marker()

        elif choice == "4":
            team, team2, stat = get_team_stat()
            underover = input("under or over: ")
            line = input("Type the number you wanna compare: ")
            marker()
            linetime = ""
            numerator = 1
            if stat == "Time":
                time = line.split(" ")
                for minute in time:
                    time1 = minute.split(":")
                    second = (int(time1[0]) * 60) + int(time1[1])
                    if numerator < len(time):
                        linetime = linetime + str(second) + " "
                        numerator += 1
                    else:
                        linetime = linetime + str(second)
            for league in LCK, LPL, LEC, LCS:
                for squad in league:
                    if team == squad["name"]:
                        if stat == "Time":
                            relative_frequency(squad, stat, linetime, underover)
                        else:
                            relative_frequency(squad, stat, line, underover)
            if team2:
                for league in LCK, LPL, LEC, LCS:
                    for squad in league:
                        if team2 == squad["name"]:
                            if stat == "Time":
                                relative_frequency(squad, stat, linetime, underover)
                            else:
                                relative_frequency(squad, stat, line, underover)
                                

        elif choice == "0":
            print(f"Closing... Goodbye {chr(0x2665)}")
            break
        else:
            print("Invalid choice!")
            marker()