# NJ_NASAT_BONUSES
Stores bonus results of players and finds best teams of four.

For use: populate players folder with .json files with name format playerName.json. 
Bonus results are stored as can be seen in the existing .json files: key is the number of the bonus (not meaningful to the code, just for convenience with user), value is a list containing bonus conversion.
Run main.py, it will print the top 10 sets of 4 players that combine for the greatest number of bonus parts converted.

Currently in the players folder are five players with data for 3 bonuses. If one uncomments line 48, random data will instead be used with names as defined by line 39 (can be edited) with number of bonuses as defined in the argument of the line 43 function call. Currently, 80% of bonus parts will be failed to be answered. This can be altered on line 32. This is to create a variance between different sets of 4 without adding additional factors to the data generation (e.g. the existence of easy/medium/hard parts).

create_dict() and print_team_dicts() exist to display the names and invidividual conversion strings for teams if desired.

Random data: there will be many teams close to each other in the top 10, which may make selection in this manner unnattractive. However, with real data, the presence of an abundance of specialists will likely make this not the case. Simulating real data is possible but would require adding data to and create new .jsons. If you would like to do this, you can make a fork.