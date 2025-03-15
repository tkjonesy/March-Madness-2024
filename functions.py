import pandas as pd
import numpy as np

'''
fuction to merge two dataframes
param df1: first dataframe
param df2: second dataframe
return: a single dataframe of the merged dataframes 
'''
def mergeDataframes(df1, df2):
    df = pd.concat([df1, df2])
    return df