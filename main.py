import itertools
from random import random
import json
import os


# load jsons as dictionaries
player_dicts = {}
for filename in os.listdir('players'):
    if filename.endswith(".json"):
        with open("players/"+filename) as f:
            player_dicts[filename[:-5]] = json.load(f)


# convert player json dictionary to result string dictionary
players = {}
for player in player_dicts:
    string = ""
    for li in list(player_dicts[player].values()):
        for value in li:
            string += str(value)
    players[player] = string


# generate random player data for testing
def get_random_data(bonus_part_count):
    # create random result string of given length
    def rando(length):
        rand_str = ""
        for i in range(length):
            # arbitrarily each part has 20% chance of being gotten
            boolean = random() > 0.8
            if boolean:
                rand_str += "1"
            else:
                rand_str += "0"
        return rand_str

    names = ["A", "B", "C", "D",
             "E", "F", "G", "H", "I"]
    players = {}
    for name in names:
        players[name] = rando(bonus_part_count)
    return players
# players = get_random_data(99)


# create dictionaries of result scores and result strings for each possible team
result_scores = {}
result_strings = {}
# create list of all size 4 sets of players
teams = list(itertools.combinations(players.keys(), 4))
for team in teams:
    result = ""
    # iterate through bonuses
    for i in range(len(players[team[0]])):
        got = "0"
        # check if any player got bonus
        for player in team:
            if players[player][i] == "1":
                got = "1"
                break
        # update result string
        result += got
    result_scores[team] = result.count("1")
    result_strings[team] = result


# find teams with best combined score
best_teams = []
best_score = max(list(result_scores.values()))
for team in list(result_scores.keys()):
    if result_scores[team] == best_score:
        best_teams.append(team)


# create sub-dictionary of players dictionary with players of an inputted team
def create_dict(team):
    d = {key: value for key, value in players.items() if key in team}
    return d


# prints team dictionaries of multiple teams
def print_team_dicts(teams):
    for team in teams:
        print(create_dict(team))


print("Best teams: "+str(best_teams))
print("Combined score: "+str(best_score))
