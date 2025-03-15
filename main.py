import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import log_loss
from sklearn.metrics import brier_score_loss
from functions import mergeDataframes
from functions import mergeTournamentData
from functions import regularDetailsFocus
from functions import sumStats
from functions import createFeatures
from functions import splitHistTournamentData
from functions import calculateDifferenceHistTourn
from functions import trainTestSplit

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
    compactTourn = mergeTournamentData(mTournCompact, wTournCompact)
    names = mergeDataframes(mNames, wNames)

    # Split regular season detailed results into dataframes focused on outcome for one team
    AllRegDetail = regularDetailsFocus(regDetail)

    # Sum regular season stats per season
    RegSeasonDetail = sumStats(AllRegDetail)

    # Create input features
    RegSeasonFeatures = createFeatures(RegSeasonDetail)

    # Handle historical tournament data
    TourneyInput = splitHistTournamentData(compactTourn)

    # Calculate historical differneces for training
    histData = calculateDifferenceHistTourn(TourneyInput, RegSeasonFeatures)

    # Setup train test split
    XTrain, XTest, yTrain, yTest = trainTestSplit(histData)

    # Setup and train Logistic Regression model
    model = LogisticRegression(
        C=1,
        max_iter=100,
        solver='saga',
        tol=0.0001
    )
    model.fit(XTrain, yTrain)

    # Get model predictions
    yPred = model.predict(XTest)
    yPredProba = model.predict_proba(XTest)

    # Compute Metrics log loss and brier score
    logLoss = log_loss(yTest, yPredProba)
    print(f'Log Loss: {logLoss}')
    yPredProbaClass1 = yPredProba[:, 1]
    brierScore = brier_score_loss(yTest, yPredProbaClass1)
    print(f'Brier Score: {brierScore}')