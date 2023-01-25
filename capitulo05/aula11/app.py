list_teams = ["Barcelona", "Flamengo", "Manchester City", "Grêmio", "Milan", "Real Madrid", "River Plate", "Liverpool",]
found = False
team = input("Search a team: ")

for i in range(0, len(list_teams)):
    if team == list_teams[i]:
        found = True


print("Team found.") if found == True else print("Team not found.")
