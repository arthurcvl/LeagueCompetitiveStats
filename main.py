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

def itens():
    pqp = ["gameid","datacompleteness","url","league","year","split","playoffs","date","game","patch","participantid",
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
    indices = [1, 2, 4, 10, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 30, 31, 32, 35, 36,
               37, 38, 39, 40, 41, 42, 45, 50, 51, 52, 53, 54, 55, 57, 59, 60, 61, 62, 63, 70, 71, 72, 73, 76,
               77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100,
               101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119,
               120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130]

    indices.sort(reverse=True)
    for indice in indices:
        pqp.pop(indice)

    for data in pqp:
        print("{} - {}".format(pqp.index(data),data))


def adicionar_dados(dados, time):
    for jogo in dados:
        if jogo[8] == time["name"]:
            kills = int(jogo[11]) + int(jogo[12])
            if jogo[15] and jogo[16]:
                dragons = int(jogo[15]) + int(jogo[16])
            else:
                dragons = 0
            if jogo[22] and jogo[23]:
                barons = int(jogo[22]) + int(jogo[23])
            else:
                barons = 0
            if jogo[25] and jogo[26]:
                towers = int(jogo[25]) + int(jogo[26])
            else:
                towers = 0
            if jogo[27] and jogo[28]:
                inhibitors = int(jogo[27]) + int(jogo[28])
            else:
                inhibitors = 0
            time[jogo[0]] = {
                "gameid": jogo[0],
                "Split": jogo[2],
                "Playoffs": jogo[3],
                "Patch": jogo[6],
                "Side": jogo[7],
                "Data": jogo[4],
                "Tempo": int(jogo[9]),
                "Resultado": jogo[10],
                "Kills": kills,
                "Dragoes": dragons,
                "Baroes": barons,
                "Torres": towers,
                "Inibidores": inhibitors,

            }

def mostrar_dados(dado, stat):
    print("Jogos da {}:".format(dado["name"]))
    print("----------------------------------------------------------------")
    for jogo in dado:
        if jogo != "name":
            print(dado[jogo]["opp"])
            print(dado[jogo]["Patch"])
            print(dado[jogo]["Data"])
            print("{} - {}".format(stat, dado[jogo][stat]))
            print("----------------------------------------------------------------")

def mostrar_dados_time(dado, stat, time):
    print("Jogos da {}:".format(dado["name"]))
    print("----------------------------------------------------------------")
    for jogo in dado:
        if jogo != "name" and dado[jogo]['opp'] == time:
            print(dado[jogo]["opp"])
            print(dado[jogo]["Patch"])
            print("{} - {}".format(stat, dado[jogo][stat]))
            print("----------------------------------------------------------------")
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
                porcentagem = (len(corretos) / (len(time) - 1)) * 100
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
                    print("Patch {} - ({}) jogos - {} - {}% Poison".format(patch, jogos.count(patch), dado, (len(corretos) / jogos.count(patch) * 100)))
                elif len(corretos) == 0:
                    print("Patch {} - ({}) jogos - {} - {}% Poison".format(patch, jogos.count(patch), dado, 0))

                corretos.clear()
            print("----------------------------------------------------------------")
    else:
        print("Por favor digite se é Over ou Under!")

def menu():
    print("Digite 1 para ver as informações guardadas por jogo")
    print("Digite 2 para ver os nomes dos Times")
    print("Digite 3 para mostrar os dados de um Time")
    print("Digite 4 para mostrar os dados de um Time contra um adversario especifico")
    print("Digite 5 para mostrar a Media de um Dado Especifico de um time")
    print("Digite 6 para mostrar o Poison de um Dado Especifico de um time")
    print("Digite 0 para fechar a Agenda")
    print("----------------------------------------------------------------")


def atualizar_dados():
    data = read_csv_file()
    for liga in LCK, LPL, LEC, LCS:
        for time in liga:
            adicionar_dados(data, time)

def mostrar_times_liga(liga="Todas"):
    if liga == "Todas":
        print("Times Disponiveis no Software:")
        for liga in LCK, LPL, LEC, LCS:
            for time in liga:
                print(time["name"])
            print("----------------------------------------------------------------")
    elif liga == "LCK":
        print("Times da LCK: ")
        for team in LCK:
            print(team["name"])
        print("----------------------------------------------------------------")
    elif liga == "LPL":
        print("Times da LPL: ")
        for team in LPL:
            print(team["name"])
        print("----------------------------------------------------------------")
    elif liga == "LCS":
        print("Times da LCS: ")
        for team in LCS:
            print(team["name"])
        print("----------------------------------------------------------------")
    elif liga == "LEC":
        print("Times da LEC: ")
        for team in LEC:
            print(team["name"])
        print("----------------------------------------------------------------")
    else:
        print("Liga não encontrada!")
        print("----------------------------------------------------------------")

# Criar método para obter dados por Fase Regular / Playoff - Criar um método para adicionar os games automaticamente

def function_retardad(data, gameid):
    lista = []
    for jogo in data:
        if jogo[0] == gameid and jogo[8] not in lista:
            lista.append(jogo[8])


    return lista

def adicionar_adversario():
    data = read_csv_file()
    lista = []
    for jogo in data:
        if jogo[0] not in lista and jogo[0] != "gameid":
            lista.append(jogo[0])
    for gameid in lista:
        set = function_retardad(data, gameid)
        for liga in LCK, LPL, LEC, LCS:
            for team in liga:
                if team["name"] in set and team[gameid]:
                    if team["name"] == set[0]:
                        team[gameid]["opp"] = set[1]
                    elif team["name"] == set[1]:
                        team[gameid]["opp"] = set[0]


if __name__ == "__main__":
    atualizar_dados()
    adicionar_adversario()
    while True:
        menu()
        escolha = input("Digite sua opcao: ")
        print("----------------------------------------------------------------")
        if escolha == "1":
            itens()
            print("----------------------------------------------------------------")
        elif escolha == "2":
            print(">>>Se voce deseja ver de uma liga especifica digite o nome da Liga, caso deseja ver todos não digite"
                  "nada")
            opcional = input("Digite aqui: ")
            print("----------------------------------------------------------------")
            if opcional:
                mostrar_times_liga(opcional)
            else:
                mostrar_times_liga()
        elif escolha == "3":
            time = input("Digite o nome do time que voce deseja ver os dados:")
            dado = input("Digite o nome do dado que voce deseja ver:")
            print("----------------------------------------------------------------")
            for liga in LCK, LPL, LEC, LCS:
                for team in liga:
                    if time == team["name"]:
                        mostrar_dados(team, dado)
                        print("----------------------------------------------------------------")
        elif escolha == "4":
            time = input("Digite o nome do time que voce deseja ver os dados:")
            opp = input("Digite o nome do time adversario:")
            dado = input("Digite o nome do dado que voce deseja ver:")
            print("----------------------------------------------------------------")
            for liga in LCK, LPL, LEC, LCS:
                for team in liga:
                    if time == team["name"]:
                        mostrar_dados_time(team, dado, opp)
                        print("----------------------------------------------------------------")
        elif escolha == "5":
            time = input("Digite o nome do time que voce deseja ver os dados: ")
            time2 = input("Digite o nome do outro time: ")
            dado = input("Digite o dado que voce deseja obter a media: ")
            print("----------------------------------------------------------------")
            for liga in LCK, LPL, LEC, LCS:
                for team in liga:
                    if time == team["name"]:
                        media(team, dado)
                        print("----------------------------------------------------------------")
                        media_time_patch(team, dado)
                        print("----------------------------------------------------------------")
            if time2:
                for liga in LCK, LPL, LEC, LCS:
                    for team in liga:
                        if time2 == team["name"]:
                            media(team, dado)
                            print("----------------------------------------------------------------")
                            media_time_patch(team, dado)
                            print("----------------------------------------------------------------")

        elif escolha == "6":
            time = input("Digite o nome do time que voce deseja ver os dados:")
            time2 = input("Digite o nome do outro time: ")
            dado = input("Digite o dado que voce deseja obter o poison: ")
            underover = input("Digite se é under ou over: ")
            linha = input("Digite as linhas: ")
            print("----------------------------------------------------------------")
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
                            print("----------------------------------------------------------------")
                            poison_patch(team, dado, nigger, underover)
                            print("----------------------------------------------------------------")
                        else:
                            poison(team, dado, linha, underover)
                            print("----------------------------------------------------------------")
                            poison_patch(team, dado, linha, underover)
                            print("----------------------------------------------------------------")
            if time2:
                for liga in LCK, LPL, LEC, LCS:
                    for team in liga:
                        if time2 == team["name"]:
                            if dado == "Tempo":
                                poison(team, dado, nigger, underover)
                                print("----------------------------------------------------------------")
                                poison_patch(team, dado, nigger, underover)
                                print("----------------------------------------------------------------")
                            else:
                                poison(team, dado, linha, underover)
                                print("----------------------------------------------------------------")
                                poison_patch(team, dado, linha, underover)
                                print("----------------------------------------------------------------")

        elif escolha == "0":
            print("Saindo do programa")
            break
        else:
            print("Escolha Invalida")
            print("----------------------------------------------------------------")