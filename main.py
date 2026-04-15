from src.data_loader import load_data
from src.preprocess import clean_data
from src.eda import perform_eda
from src.anomaly import detect_anomalies
from src.forecast import forecast_temperature

def main():
    path = "data/GlobalLandTemperaturesByCity.csv"

    df = load_data(path)
    df = clean_data(df)

    perform_eda(df)
    detect_anomalies(df)
    forecast_temperature(df)

if __name__ == "__main__":
    main()