
def lags_windows(df):
    lags = [24]
    lag_cols = ["lag_{}".format(lag) for lag in lags ]
    for lag, lag_col in zip(lags, lag_cols):
        df[lag_col] = df["Потребитель"].shift(lag)

    wins = [8]
    for win in wins :
        for lag,lag_col in zip(lags, lag_cols):
            df["rmean_{}_{}".format(lag,win)] = df[lag_col].transform(lambda x : x.rolling(win).mean())
    return df

def feat_eng(df):
    df = lags_windows(df)
    return df

def lags_windows_1(df):
    lags = [1]
    lag_cols = ["lag_{}".format(lag) for lag in lags ]
    for lag, lag_col in zip(lags, lag_cols):
        df[lag_col] = df["Потребитель"].shift(lag)

    wins = [3]
    for win in wins :
        for lag,lag_col in zip(lags, lag_cols):
            df["rmean_{}_{}".format(lag,win)] = df[lag_col].transform(lambda x : x.rolling(win).mean())
    return df

def feat_eng_1(df):
    df = lags_windows_1(df)
    return df

def lags_windows_2(df):
    lags = [3]
    lag_cols = ["lag_{}".format(lag) for lag in lags ]
    for lag, lag_col in zip(lags, lag_cols):
        df[lag_col] = df["Потребитель"].shift(lag)

    wins = [5]
    for win in wins :
        for lag,lag_col in zip(lags, lag_cols):
            df["rmean_{}_{}".format(lag,win)] = df[lag_col].transform(lambda x : x.rolling(win).mean())
    return df

def feat_eng_2(df):
    df = lags_windows_2(df)
    return df