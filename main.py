import numpy

try:
    from lck import *
    from lpl import *
    from lec import *
    from lcs import *
except Exception as e:
    print(e)

def read_csv_file():
    games = []
    with open("2024_LoL_esports_match_data_from_OraclesElixir.csv", "r", encoding="utf-8") as file:
        linhas = file.readlines()
        for linha in linhas:
            game = linha.strip().split(",")
            indices = [1, 2, 4, 10, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 30, 31, 32, 35, 36,
                       37, 38, 39, 40, 41, 42, 45, 50, 51, 52, 53, 54, 55, 57, 59, 60, 61, 62, 63, 70, 71, 72, 73, 76,
                       77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100,
                       101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119,
                       120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130]

            indices.sort(reverse=True)
            for indice in indices:
                game.pop(indice)

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
                "Tempo": int(game[9]),
                "Resultado": game[10],
                "Kills": kills,
                "Dragoes": dragons,
                "Baroes": barons,
                "Torres": towers,
                "Inibidores": inhibitors,

            }

def mostrar_dados(dado, stat):
    print("Jogos da {}:".format(dado["name"]))
    marker()
    for jogo in dado:
        if jogo != "name":
            print(dado[jogo]["Patch"])
            print(dado[jogo]["Data"])
            print("{} - {}".format(stat, dado[jogo][stat]))
            marker()

def mostrar_dados_time(dado, stat, time):
    print("Jogos da {}:".format(dado["name"]))
    marker()
    for jogo in dado:
        if jogo != "name" == time:
            print(dado[jogo]["Patch"])
            print("{} - {}".format(stat, dado[jogo][stat]))
            marker()
def media(dados, dado):
    for jogo in dados:
        if jogo != "name":
            try:
                dados[jogo][dado]
            except:
                print("Dado: {} não encontrado!".format(dado))
                return None
    media = []
    for jogo in dados:
        if jogo != "name":
            media.append(dados[jogo][dado])
    if dado == "Tempo":
        tempo = float(numpy.mean(media))
        minutos, segundos = divmod(tempo, 60)
        print("{} - {}:{} {} em media".format(dados["name"], int(minutos), int(segundos), dado))
    else:
        print("{} - {} {} em media".format(dados["name"], float(numpy.mean(media)), dado))

def mediana(dados, dado):
    mediana = []
    for jogo in dados:
        if jogo != "name":
            mediana.append(dados[jogo][dado])
    print(float(numpy.median(mediana)))

def poison(time, dado, lines, overunder):
    if lines:
        for jogo in time:
            if jogo != "name":
                try:
                    time[jogo][dado]
                except:
                    print("Dado: {} não encontrado!".format(dado))
                    return None
        if overunder == "over" or overunder == "under":
            linhas = lines.split(" ")
            for linha in linhas:
                try:
                    linha = float(linha)
                except ValueError:
                    print("Por favor digite apenas numeros nas linhas")
                    return None
                corretos = []
                for jogo in time:
                    if jogo != "name":
                        if overunder == "over":
                            if time[jogo][dado] > linha:
                                corretos.append(time[jogo][dado])
                        elif overunder == "under":
                            if time[jogo][dado] < linha:
                                corretos.append(time[jogo][dado])
                porcentagem = round((len(corretos) / (len(time) - 1)) * 100, 1)
                if dado == "Tempo":
                    minutos, segundos = divmod(linha, 60)
                    print("{} ({}:{}) {} - {}%".format(time["name"], int(minutos), int(segundos), dado, porcentagem))
                else:
                    print("{} ({}) {} - {}%".format(time["name"], linha, dado, porcentagem))
        else:
            print("Por favor digite se é Over ou Under!")
    else:
        return None
def media_time_patch(time, dado):
    for jogo in time:
        if jogo != "name":
            try:
                time[jogo][dado]
            except:
                print("Dado: {} não encontrado!".format(dado))
                return None
    jogos = []
    patchs = []
    indi = []
    for jogo in time:
        if jogo != "name":
            if time[jogo]["Patch"] not in patchs:
                patchs.append(time[jogo]["Patch"])
            if time[jogo]["Patch"]:
                jogos.append(time[jogo]["Patch"])
    print("{}: ".format(time["name"]))
    for patch in patchs:
        for jogo in time:
            if jogo != "name":
                if time[jogo]["Patch"] == patch:
                    indi.append(time[jogo][dado])
        if dado == "Tempo":
            tempo = float(numpy.mean(indi))
            minutos, segundos = divmod(tempo, 60)
            print("Patch {} - ({}) jogos - {}:{} {} em Media".format(patch, jogos.count(patch), int(minutos), int(segundos), dado))
            indi.clear()
        else:
            print("Patch {} - ({}) jogos - {} {} em Media".format(patch, jogos.count(patch), float(numpy.mean(indi)), dado))
            indi.clear()


def poison_patch(time, dado, lines, overunder):
    for jogo in time:
        if jogo != "name":
            try:
                time[jogo][dado]
            except:
                print("Dado: {} não encontrado!".format(dado))
                return None
    if overunder == "under" or overunder == "over":
        linhas = lines.split(" ")
        for linha in linhas:
            try:
                linha = float(linha)
            except ValueError:
                print("Por favor digite apenas numeros nas linhas")
                return None
            jogos = []
            corretos = []
            patchs = []
            for jogo in time:
                if jogo != "name":
                    if time[jogo]["Patch"]:
                        if time[jogo]["Patch"] not in patchs:
                            patchs.append(time[jogo]["Patch"])
                        jogos.append(time[jogo]["Patch"])
            if dado == "Tempo":
                minutos, segundos = divmod(linha, 60)
                print("{} - {}:{} : ".format(time["name"], int(minutos), int(segundos)))
            else:
                print("{} - {}: ".format(time["name"], linha))
            for patch in patchs:
                for jogo in time:
                    if jogo != "name":
                        if overunder == "over":
                            if time[jogo]["Patch"] == patch and time[jogo][dado] > linha:
                                corretos.append(time[jogo][dado])
                        elif overunder == "under":
                            if time[jogo]["Patch"] == patch and time[jogo][dado] < linha:
                                corretos.append(time[jogo][dado])
                if len(corretos) > 0:
                    print("Patch {} - ({}) jogos - {} - {}% Poison".format(patch, jogos.count(patch), dado, round((len(corretos) / jogos.count(patch) * 100), 1)))
                elif len(corretos) == 0:
                    print("Patch {} - ({}) jogos - {} - {}% Poison".format(patch, jogos.count(patch), dado, 0))

                corretos.clear()
            marker()
    else:
        print("Please type if its over or under! ")

def menu():
    print("Type 1 to see what informations we are getting from each game")
    print("Type 2 to see teams name (atm you will need to type the full name to get data)")
    print("Type 3 to get the media from a team stat (tower, dragon, time, kills)")
    print("Type 4 to get the relative frequency of a team stat")
    print("Type 0 to close the program (or Ctrl + C)")
    marker()


def atualizar_dados():
    data = read_csv_file()
    for liga in LCK, LPL, LEC, LCS:
        for time in liga:
            add_data(data, time)

def mostrar_times_liga():
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
    atualizar_dados()
    while True:
        menu()
        escolha = input("Type here: ")
        marker()
        if escolha == "1":
            items()
            marker()
        elif escolha == "2":   
            mostrar_times_liga()
        elif escolha == "3":
            time, time2, dado = get_team_stat()
            marker()
            for liga in LCK, LPL, LEC, LCS:
                for team in liga:
                    if time == team["name"]:
                        media(team, dado)
                        marker()
                        media_time_patch(team, dado)
                        marker()
            if time2:
                for liga in LCK, LPL, LEC, LCS:
                    for team in liga:
                        if time2 == team["name"]:
                            media(team, dado)
                            marker()
                            media_time_patch(team, dado)
                            marker()

        elif escolha == "4":
            time, time2, dado = get_team_stat()
            underover = input("under or over: ")
            linha = input("Type the number you wanna compare: ")
            marker()
            nigger = ""
            numerator = 0
            if dado == "Tempo":
                tempo = linha.split(" ")
                for minuto in tempo:
                    tempo1 = minuto.split(":")
                    segundos = (int(tempo1[0]) * 60) + int(tempo1[1])
                    if numerator < len(tempo):
                        nigger = nigger + str(segundos) + " "
                        numerator += 2
                    else:
                        nigger = nigger + str(segundos)
            for liga in LCK, LPL, LEC, LCS:
                for team in liga:
                    if time == team["name"]:
                        if dado == "Tempo":
                            poison(team, dado, nigger, underover)
                            marker()
                            poison_patch(team, dado, nigger, underover)
                            marker()
                        else:
                            poison(team, dado, linha, underover)
                            marker()
                            poison_patch(team, dado, linha, underover)
                            marker()
            if time2:
                for liga in LCK, LPL, LEC, LCS:
                    for team in liga:
                        if time2 == team["name"]:
                            if dado == "Tempo":
                                poison(team, dado, nigger, underover)
                                marker()
                                poison_patch(team, dado, nigger, underover)
                                marker()
                            else:
                                poison(team, dado, linha, underover)
                                marker()
                                poison_patch(team, dado, linha, underover)
                                marker()

        elif escolha == "0":
            print(f"Closing... Goodbye {chr(0x2665)}")
            break
        else:
            print("Invalid choice!")
            marker()