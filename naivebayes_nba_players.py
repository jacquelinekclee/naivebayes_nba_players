import pandas as pd 
import numpy as np 
import math

def detect_missing_values(df):
    """
    Go through all columns of the DataFrame and detect missing values.
    Print out the results each time.
    """
    for c in list(df.columns):
    #all data are strings, so strings that start with empty space (' ') will be assumed as empty
        if type(df[c][0]) == str:
            print(c + ': ' + str(df[c].str.startswith(' ').values.any()))
        else:
            print(c, ': ', any(list(df[c].isna())))

def per_game_stats(df, games_col):
    """
    Given the aggregate statistics, calculate the per game averages and add the column to the given
    DataFrame
    """
    totals = ['TRB', 'AST', 'PTS', 'BLK', 'STL']
    avgs = ['RPG', 'APG', 'PPG', 'BPG', 'SPG']
    for i in range(len(totals)):
        df[avgs[i]] = df[totals[i]] / df[games_col]

def reset_position(df):
    """
    Replace the positions in the given DataFrame so that each position is in the set
    {G, G-F, F, F-C, C}
    """
    df['Pos'] = df['Pos'].replace(['PG', 'SG', 'SG-PG', 'PG-SG'], 'G')
    df['Pos'] = df['Pos'].replace(['PF-C', 'C-PF', 'C-SF'], 'FC')
    df['Pos'] = df['Pos'].replace(['PF', 'SF', 'SF-PF', 'PF-SF'], 'F')
    df['Pos'] = df['Pos'].replace(['PG-SF', 'SG-SF', 'SG-PF', 'SF-SG'], 'GF')

def quantile_dict(df):
    """
    Calculate the quartiles for a given DataFrame.
    Return a dictionary containing the quartiles for each column.
    """
    cols = list(df.columns[list(df.columns).index('TS%'):])
    q_vals = [0.25, 0.75]
    return {col:[np.quantile(df[col], q) for q in q_vals] for col in cols}

def discretize(val, col, dictionary):
    """
    Return the quartile a given value falls in.
    """
    percentiles = dictionary[col] + [val]
    index = sorted(percentiles).index(val)
    if index == 0:
        return '1st'
    elif index == 1:
        return '2nd'
    else:
        return '3rd'

def categorical_df(df, discretized_cols):
    """
    Convert all continuous data to discrete data and return a new DataFrame
    """
    copy = df.copy()
    for col in discretized_cols:
        copy[col] = discretized_cols[col]
    return copy

def build_tups(df):
    """
    Build tuples of (Player, Year) to check for intersections across DataFrames
    """
    tups = []
    for i in range(df.shape[0]):
        row = (df.iloc[i])
        tups.append((row['Player'], row['Year']))
    return tups

def create_yn_cols(player_tups, other_tups):
    """
    Return a list that indicates whether or not a player_tup is in other_tups
    """
    return ['Y' if tup in other_tups else 'N' for tup in player_tups]

def assign_decades(df):
    """
    Assign a decade based on a given year
    """
    df['Decade'] = ['80s' if str(year)[2] == '8'
                  else '90s' if str(year)[2] == '9'
                  else '2000s' if str(year)[2] == '0'
                  else '2010s'
                  for year in df['Year']]


