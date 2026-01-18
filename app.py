import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("COVID-19 Data Analysis – India")

df = pd.read_csv("covid_india.csv")
df["Date"] = pd.to_datetime(df["Date"])

st.subheader("Dataset Preview")
st.dataframe(df.head())

# Daily cases
daily = df.groupby("Date")["Confirmed"].sum()

st.subheader("Daily COVID-19 Cases in India")
fig1 = plt.figure()
daily.plot()
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
st.pyplot(fig1)

# State-wise
state_total = df.groupby("State")["Confirmed"].sum().sort_values(ascending=False)

st.subheader("Top 5 States by Total Cases")
fig2 = plt.figure()
state_total.head(5).plot(kind="bar")
plt.xlabel("State")
plt.ylabel("Total Cases")
st.pyplot(fig2)

# Growth rate
growth = daily.pct_change() * 100

st.subheader("Growth Rate of Cases")
fig3 = plt.figure()
growth.plot()
plt.xlabel("Date")
plt.ylabel("Growth Rate (%)")
st.pyplot(fig3)