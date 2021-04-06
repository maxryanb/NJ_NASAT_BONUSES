# NJ_NASAT_BONUSES
Stores bonus results of players and finds best set of four

For use: populate players folder with jsons with name format playerName.json. 
Bonus results are stored as can be seen in the existing json files: keys are the number of the bonus (not meaningful to the code, just for convenience with user), value is a list containing bonus conversion.
Run nasat.py, it will print the sets of 4 players that combine for the greatest number of bonus parts converted (possible that multiple sets achieve the max) and that number itself.
