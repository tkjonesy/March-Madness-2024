import pandas as pd
from functions import mergeDataframes

if __name__ == "__main__":
    # Mens data import
    mRegDetail = pd.read_csv('data/men data/MRegularSeasonDetailedResults.csv')
    mTournCompact = pd.read_csv('data/men data/MNCAATourneyCompactResults.csv')
    mNames = pd.read_csv('data/men data/MTeamSpellings.csv')

    # Womens data import
    wRegDetail = pd.read_csv('data/women data/WRegularSeasonDetailedResults.csv')
    wTournCompact = pd.read_csv('data/women data/WNCAATourneyCompactResults.csv')
    wNames = pd.read_csv('data/women data/WTeamSpellings.csv')

    # Combined data
    regDetail = mergeDataframes(mRegDetail, wRegDetail)
    compactDetail = mergeDataframes(mTournCompact, wTournCompact)
    names = mergeDataframes(mNames, wNames)