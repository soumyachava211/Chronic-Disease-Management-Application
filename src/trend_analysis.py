import pandas as pd

def weekly_trend(df):
    df['date'] = pd.to_datetime(df['date'])
    df['week'] = df['date'].dt.isocalendar().week
    return df.groupby('week')['glucose_mgdl'].mean()

def detect_high_trend(df, threshold=180):
    recent = df.tail(5)
    return (recent['glucose_mgdl'] > threshold).sum()
