import pandas as pd
from sklearn.ensemble import RandomForestRegressor

def clothes(high, low):
    temp = [[high, low]]
    
    # Predicting upper clothing
    data = pd.read_csv('up.csv')
    X = data.iloc[:, :-1].values
    Y = data.iloc[:, -1].values
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X, Y)
    up_pred = model.predict(temp)

    if up_pred[0] not in [3, 4]:
        # Predicting lower clothing
        data = pd.read_csv('down.csv')
        X = data.iloc[:, :-1].values
        Y = data.iloc[:, -1].values
        model = RandomForestRegressor(n_estimators=100, random_state=0)
        model.fit(X, Y)
        down_pred = model.predict(temp)

    # Predicting shoes
    data = pd.read_csv('shoes.csv')
    X = data.iloc[:, :-1].values
    Y = data.iloc[:, -1].values
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X, Y)
    shoes_pred = model.predict(temp)

    return int(up_pred[0]), int(down_pred[0]), int(shoes_pred[0])