import pandas as pd

def load_data(path):
    try:
        df = pd.read_csv(path)
        print("✅ Data Loaded Successfully")
        print("Shape:", df.shape)
        print(df.head())
        return df
    except Exception as e:
        print("❌ Error loading data:", e)