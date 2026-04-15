import matplotlib.pyplot as plt

def detect_anomalies(df):
    print("\n🔹 Detecting Anomalies...")

    # Calculate mean & std
    mean = df['temperature'].mean()
    std = df['temperature'].std()

    # Define anomaly condition
    df['anomaly'] = (df['temperature'] > mean + 2*std) | \
                    (df['temperature'] < mean - 2*std)

    anomalies = df[df['anomaly'] == True]

    print("✅ Total Anomalies Found:", len(anomalies))

    # Plot anomalies
    plt.figure()
    plt.plot(df['date'], df['temperature'], label='Temperature')

    plt.scatter(anomalies['date'], anomalies['temperature'],
                color='red', label='Anomaly')

    plt.title("Temperature Anomaly Detection")
    plt.xlabel("Date")
    plt.ylabel("Temperature")
    plt.legend()

    plt.savefig("outputs/plots/anomaly_plot.png")

    print("✅ Anomaly plot saved")