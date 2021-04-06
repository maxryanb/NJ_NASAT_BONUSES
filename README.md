# NJ_NASAT_BONUSES
Stores bonus results of players and finds best team(s) of four.

For use: populate players folder with jsons with name format playerName.json. 
Bonus results are stored as can be seen in the existing json files: key is the number of the bonus (not meaningful to the code, just for convenience with user), value is a list containing bonus conversion.
Run main.py, it will print the set(s) of 4 players that combine for the greatest number of bonus parts converted (possible that multiple sets achieve the max) and that max number itself.

Currently in the players folder are five players with data for 3 bonuses. If one uncomments line 43 in main.py, random data will instead be used with names as defined by line 37 (can be edited) with number of bonuses as defined in the argument of the line 43 function call. Currently, 80% of bonus parts will be failed to be answered. This can be altered on line 31. This is to create a large variance between different sets of 4 without adding additional factors to the data generation (e.g. the existence of easy/medium/hard parts).

create_dict() and print_team_dicts() exist to display the names and invidividual conversion strings for teams if desired.
