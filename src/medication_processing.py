import pandas as pd

def load_medication_log(path):
    df = pd.read_csv(path)
    df['date'] = pd.to_datetime(df['date'])
    return df

def adherence_rate(df):
    return df['taken'].str.lower().eq('yes').mean()
