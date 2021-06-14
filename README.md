# NJ_NASAT_BONUSES
Stores bonus results of players and finds best teams of a given size. One can change desired team size on line 66.

For use: populate players folder with .json files with name format playerName.json. 
Bonus results are stored as can be seen in the existing .json files: key is the number of the bonus (not meaningful to the code, just for convenience with user), value is a list containing bonus conversion. **Each player needs to be read the same bonuses in the same order.** If one wants to run main.py with only the first n tossups (in case a player has only heard some of the tryout), change the 'limit' variable on line 24.
Run main.py, it will print the top 10 sets of players that combine for the greatest number of bonus parts converted and the ppb of those sets.

If one uncomments line 66, random data will instead be used with names as defined by line 55 (can be edited) with number of bonuses as defined in the argument of the line 64 function call. Currently, 80% of bonus parts will be failed to be answered. This can be altered on line 48. This is to create a variance between different sets of 4 without adding additional factors to the data generation (e.g. the existence of easy/medium/hard parts).

create_dict() and print_team_dicts() exist to display the names and invidividual conversion strings for teams if desired for debugging or testing.

### I am very welcome to suggestions or contributions! Just dm me on discord @maxryanb#7300.
