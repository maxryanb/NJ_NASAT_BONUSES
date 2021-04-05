import itertools
from random import random
import json
import os

# import jsons as dictionaries
def load_players():  
    player_dicts = {}
    for filename in os.listdir('players'):
        if filename.endswith(".json"):
            with open("players/"+filename) as f:
                player_dicts[filename[:-5]] = json.load(f)
    return(player_dicts)


player_dicts = load_players()


# TO BE MADE: convert player json to result string
def dict_to_string(d):  
    string = ""


# create random result string of given length
def rando(length):
    rand_str = ""
    for i in range(length):
        boolean = random() > 0.8
        if boolean:
            rand_str += "1"
        else:
            rand_str += "0"
    return rand_str


bonus_count = 100


names = ["A", "B", "C", "D",
         "E", "F", "G", "H", "I"]

# temporary


def load_random_data(names):
    players = {}

    for name in names:
        players[name] = rando(bonus_count)

    return players


players = load_random_data(names)


# create dictionaries of result scores and result strings for each possible team
def create_teams(players):
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

    return result_scores, result_strings


# store score and string dictionaries
result_scores, result_strings = create_teams(players)


# find teams with best combined score
def get_best_teams(result_scores):
    best_teams_list = []

    max_score = max(list(result_scores.values()))

    for team in list(result_scores.keys()):
        if result_scores[team] == max_score:
            best_teams_list.append(team)

    return best_teams_list, max_score


best_teams, best_score = get_best_teams(result_scores)


def create_dict(team):
    d = {key: value for key, value in players.items() if key in team}
    return d


def print_team_dicts(teams):
    for team in teams:
        print(create_dict(team))


print("Best teams: "+str(best_teams))
print("Combined score: "+str(best_score))
