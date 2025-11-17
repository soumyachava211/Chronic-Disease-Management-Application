import pandas as pd
import numpy as np

def load_glucose_data(path):
    df = pd.read_csv(path)
    df['datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'])
    df = df.sort_values('datetime')
    return df

def classify_glucose(row):
    if row < 70:
        return "Low"
    elif row <= 180:
        return "Target Range"
    else:
        return "High"

def add_glucose_categories(df):
    df['category'] = df['glucose_mgdl'].apply(classify_glucose)
    return df

def calculate_daily_stats(df):
    stats = df.groupby('date')['glucose_mgdl'].agg(['mean', 'min', 'max'])
    return stats
