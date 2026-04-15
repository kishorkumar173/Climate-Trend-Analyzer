import matplotlib.pyplot as plt

def perform_eda(df):
    print("\n🔹 Performing EDA...")

    # Extract year
    df['year'] = df['date'].dt.year

    # Yearly average temperature
    yearly_temp = df.groupby('year')['temperature'].mean()

    # Plot 1: Temperature Trend
    plt.figure()
    plt.plot(yearly_temp.index, yearly_temp.values)
    plt.title("Yearly Average Temperature Trend (India)")
    plt.xlabel("Year")
    plt.ylabel("Temperature")
    plt.savefig("outputs/plots/yearly_temp_trend.png")

    print("✅ EDA Completed - Plot Saved")