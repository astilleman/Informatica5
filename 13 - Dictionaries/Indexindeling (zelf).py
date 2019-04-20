def indexindeling(teams):

    even_teams = {}
    oneven_teams = {}

    for team in teams:
        for i in range(len(teams.get(team))):
            if i % 2 == 0 and team not in even_teams:
                even_teams[team] = [teams.get(team)[i]]
            elif i % 2 == 0:
                 even_teams[team].append(teams.get(team)[i])
            elif team not in oneven_teams:
                oneven_teams[team] = [teams.get(team)[i]]
            else:
                oneven_teams[team].append(teams.get(team)[i])

        mes = 'even teams: {}\noneven teams: {}'.format(even_teams, oneven_teams)

    return mes


print(indexindeling({'geel':['sam', 'kim', 'tom', 'ann', 'ine'], 'rood': ['jan']}))