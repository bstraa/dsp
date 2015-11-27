#The football.csv file contains the results from the English Premier League. 
# The columns labeled 'Goals' and 'Goals Allowed' contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in 'for' and 'against' goals.


import csv
import pandas as pd

def read_data(data):
   # COMPLETE THIS FUNCTION
    with open(data) as f:
        f = pd.read_csv(f)
        f['Difference'] = f['Goals'] - f['Goals Allowed']
        ff = f.loc[f['Difference'].idxmax()]
        print(ff[0])

#def get_min_score_difference(self, parsed_data):
    # COMPLETE THIS FUNCTION

#def get_team(self, index_value, parsed_data):
    # COMPLETE THIS FUNCTION

def main():
    input = 'football.csv'
    read_data(input)

if __name__ == '__main__':
    main()


