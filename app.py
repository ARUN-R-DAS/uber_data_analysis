import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

st.title("Uber ride data EDA")
# =================== Loading df =========================================
df = pd.read_csv(r'Assets\ncr_ride_bookings.csv')

# =================== Overview section ===================================
st.subheader("▪ Dataset")
st.dataframe(df)

# =================== Monthly Rides and Booking Value ====================
st.subheader("▪ Monthly Rides and Booking Value")
st.image(r'Plots\montly rides vs booking value.png')

# =================== Count Plots ====================
st.subheader("▪ Count Plots")
st.image(r'Plots/countplots.png')

# =================== Hist Plots ====================
st.subheader("▪ Hist Plots")
st.image(r'Plots/histplots.png')

# =================== Box Plots ====================
st.subheader("▪ Box Plots")
st.image(r'Plots/boxplots.png')

# =================== Joint Plots ====================
st.subheader("▪ Joint Plots")
st.image(r'Plots/jointplot.png')

# =================== Scatter Plots ====================
st.subheader("▪ Scatter Plots")
st.image(r'Plots/scatter.png')

# =================== Heatmap ====================
st.subheader("▪ Heatmap Plots")
st.image(r'Plots/heatmap.png')

# =================== Monthly Rides and Booking Value ====================
st.subheader("▪ Vehicle types and Booking Value")
styled_df = (
    df.groupby('Vehicle Type')['Booking Value']
    .mean()
    .sort_values()
    .reset_index()
)
st.dataframe(styled_df, use_container_width=True)

# =================== Location based insights ====================
location_popularity = df['Pickup Location'].value_counts().sort_values()
st.subheader("▪ Pickup Location Popularity")

col1, col2 = st.columns(2)

with col1:
    st.write("▪ Popular Pickup Locations")
    st.dataframe(location_popularity.head(10))
with col2:
    st.write("▪ Least Popular Pickup Locations")
    st.dataframe(location_popularity.tail(10))