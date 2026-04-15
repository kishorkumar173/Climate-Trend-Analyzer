import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

def forecast_temperature(df):
    print("\n🔹 Forecasting Future Temperature...")

    # Extract year
    df['year'] = df['date'].dt.year

    # Group yearly
    yearly = df.groupby('year')['temperature'].mean().reset_index()

    # Prepare data
    X = yearly[['year']]
    y = yearly['temperature']

    # Train model
    model = LinearRegression()
    model.fit(X, y)

    # Future years
    # Step 1: Natural continuation
    start_year = yearly['year'].max() + 1
    future_years = list(range(start_year, start_year + 5))

# Step 2: Extend to modern years
    future_years.extend([2024, 2025, 2026])

    future_years = np.array(future_years).reshape(-1,1)

    predictions = model.predict(future_years)

    print("✅ Future Predictions:")
    for year, temp in zip(future_years.flatten(), predictions):
        print(f"{year} → {temp:.2f}°C")

    # Plot
    plt.figure()
    plt.plot(yearly['year'], yearly['temperature'], label="Past Data")

    plt.plot(future_years, predictions, linestyle='dashed', label="Forecast")

    plt.title("Temperature Forecast")
    plt.xlabel("Year")
    plt.ylabel("Temperature")
    plt.legend()

    plt.savefig("outputs/plots/forecast.png")

    print("✅ Forecast plot saved")