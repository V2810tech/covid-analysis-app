import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


lang = st.selectbox("Select Language", ["English", "Hindi", "Marathi"])

if lang == "English":
    title = "COVID-19 Data Analysis – India"
    preview_text = "Dataset Preview"
    daily_text = "Daily COVID-19 Cases in India"
    top_state_text = "Top 5 States by Total Cases"
    growth_text = "Growth Rate of Cases"
    search_text = "Search by Date"

elif lang == "Hindi":
    title = "कोविड-19 डेटा विश्लेषण – भारत"
    preview_text = "डेटासेट पूर्वावलोकन"
    daily_text = "भारत में दैनिक कोविड-19 मामले"
    top_state_text = "कुल मामलों के अनुसार शीर्ष 5 राज्य"
    growth_text = "मामलों की वृद्धि दर"
    search_text = "तारीख से खोजें"

elif lang == "Marathi":
    title = "कोविड-19 डेटा विश्लेषण – भारत"
    preview_text = "डेटासेट पूर्वदृश्य"
    daily_text = "भारतामधील दैनिक कोविड-19 रुग्ण"
    top_state_text = "एकूण प्रकरणांनुसार शीर्ष 5 राज्य"
    growth_text = "प्रकरणांची वाढ दर"
    search_text = "तारखेनुसार शोधा"

st.title(title)


df = pd.read_csv("covid_india.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Prepare Year / Month / Day
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day


st.subheader(preview_text)
st.dataframe(df.head())


st.sidebar.header(search_text)

year = st.sidebar.selectbox("Select Year", sorted(df["Year"].unique()))
month = st.sidebar.selectbox("Select Month", sorted(df["Month"].unique()))
day = st.sidebar.selectbox("Select Day", sorted(df["Day"].unique()))

filtered_df = df[
    (df["Year"] == year) &
    (df["Month"] == month) &
    (df["Day"] == day)
]

st.subheader(f"COVID Data for {day}-{month}-{year}")
st.dataframe(filtered_df)

daily = df.groupby("Date")["Confirmed"].sum()

st.subheader(daily_text)
fig1 = plt.figure()
daily.plot()
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
st.pyplot(fig1)


state_total = df.groupby("State")["Confirmed"].sum().sort_values(ascending=False)

st.subheader(top_state_text)
fig2 = plt.figure()
state_total.head(5).plot(kind="bar")
plt.xlabel("State")
plt.ylabel("Total Cases")
st.pyplot(fig2)


growth = daily.pct_change() * 100

st.subheader(growth_text)
fig3 = plt.figure()
growth.plot()
plt.xlabel("Date")
plt.ylabel("Growth Rate (%)")
st.pyplot(fig3)")

st.pyplot(fig3)
