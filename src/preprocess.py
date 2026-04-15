import pandas as pd

def clean_data(df):
    print("\n  Cleaning Data...")

    # Rename columns for simplicity
    df = df.rename(columns={
        'dt': 'date',
        'AverageTemperature': 'temperature'
    })

    # Convert date
    df['date'] = pd.to_datetime(df['date'])

    # Drop missing values
    df = df.dropna(subset=['temperature'])

    # Filter only India (optional but recommended)
    df = df[df['Country'] == 'India']

    # Sort data
    df = df.sort_values(by='date')

    print("✅ Data Cleaned")
    print("New Shape:", df.shape)

    return df