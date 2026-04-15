import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# -------------------------------
# PAGE CONFIG (MUST BE FIRST)
# -------------------------------
st.set_page_config(
    page_title="Climate Trend Analyzer",
    layout="wide",
    page_icon="🌍"
)

# -------------------------------
# CUSTOM STYLING
# -------------------------------
# -------------------------------
# TITLE
# -------------------------------
st.title("🌍 Climate Trend Analyzer Dashboard")
st.markdown("Analyze climate trends, detect anomalies, and forecast future temperatures 🚀")

# -------------------------------
# LOAD DATA (DEFAULT + UPLOAD)
# -------------------------------
uploaded_file = st.file_uploader("Upload CSV (Optional)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("data/GlobalLandTemperaturesByCity.csv")

# -------------------------------
# PREPROCESSING
# -------------------------------
df = df.rename(columns={'dt': 'date', 'AverageTemperature': 'temperature'})
df['date'] = pd.to_datetime(df['date'])
df = df.dropna(subset=['temperature'])

# -------------------------------
# SIDEBAR FILTER
# -------------------------------
st.sidebar.title("Controls")

city = st.sidebar.selectbox("Select City", df['City'].unique())
df = df[df['City'] == city]

# -------------------------------
# METRICS
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    st.metric("🌡 Avg Temperature", f"{df['temperature'].mean():.2f} °C")

with col2:
    st.metric("📊 Total Records", len(df))

# -------------------------------
# DATA PREVIEW
# -------------------------------
st.subheader("📋 Data Preview")
st.write(df.head())

# -------------------------------
# TREND ANALYSIS
# -------------------------------
df['year'] = df['date'].dt.year
yearly = df.groupby('year')['temperature'].mean()

st.subheader("📈 Temperature Trend")

fig1 = plt.figure()
plt.plot(yearly.index, yearly.values, marker='o')
plt.grid(True)
plt.title("Temperature Trend")
plt.xlabel("Year")
plt.ylabel("Temperature")
st.pyplot(fig1)

# -------------------------------
# ANOMALY DETECTION
# -------------------------------
mean = df['temperature'].mean()
std = df['temperature'].std()

df['anomaly'] = (df['temperature'] > mean + 2*std) | \
                (df['temperature'] < mean - 2*std)

anomalies = df[df['anomaly']]

st.subheader("🚨 Anomaly Detection")

fig2 = plt.figure()
plt.plot(df['date'], df['temperature'], label='Temperature')
plt.scatter(anomalies['date'], anomalies['temperature'], color='red', label='Anomaly')
plt.legend()
plt.xlabel("Date")
plt.ylabel("Temperature")
st.pyplot(fig2)

# -------------------------------
# FORECASTING
# -------------------------------
st.subheader("🔮 Forecast")

yearly_df = yearly.reset_index()

X = yearly_df[['year']]
y = yearly_df['temperature']

model = LinearRegression()
model.fit(X, y)

future_years = np.array([2024, 2025, 2026, 2027, 2028]).reshape(-1,1)
predictions = model.predict(future_years)

fig3 = plt.figure()
plt.plot(yearly_df['year'], yearly_df['temperature'], label="Past")
plt.plot(future_years, predictions, linestyle='dashed', label="Forecast")
plt.legend()
plt.xlabel("Year")
plt.ylabel("Temperature")
st.pyplot(fig3)

# -------------------------------
# PREDICTIONS OUTPUT
# -------------------------------
st.subheader("📊 Future Predictions")

for year, temp in zip(future_years.flatten(), predictions):
    st.write(f"{year} → {temp:.2f} °C")