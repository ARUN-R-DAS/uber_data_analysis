import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
import os
import base64

# ================================================== bg image ==========================
st.set_page_config(layout="wide")

# Function to encode image file to base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Encode your local image
bin_str = get_base64_of_bin_file("background.jpg")

# Inject CSS with base64 image
page_bg_img = f"""
<style>
.stApp {{
  background-image: url("data:image/jpg;base64,{bin_str}");
  background-size: cover;
  background-attachment: fixed;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Uber ride data EDA")
# =================== Loading df =========================================
df = pd.read_csv(r'Assets\ncr_ride_bookings.csv')

# =================== Overview section ===================================
st.subheader("▪ Dataset Overview")
st.dataframe(df.head())

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

# =================== Top 20 Routes ====================
st.subheader("▪ Top 20 Routes")
st.image(r'Plots/top 20 pickup_drop routes.png')

# =================== Peak Booking Hours ====================
st.subheader("▪ Peak Booking Hours")
st.image(r'Plots/peak booking hours.png')

# =================== Cancellation by Hour ====================
st.subheader("▪ Cancellation by Hour")
st.image(r'Plots/cancellation count by hour.png')

# =================== Pie plot : Rides cancelled ====================
st.subheader("▪ Pie plot : Rides cancelled")
st.image(r'Plots/pie_rides cancelled.png')

# =================== Top customer cancellation reasons ====================
st.subheader("▪ Top customer cancellation reasons")
st.image(r'Plots/top cust cancellation reasons.png')

# =================== Top Driver cancellation reasons ====================
st.subheader("▪ Top Driver cancellation reasons")
st.image(r'Plots/top driver cancellation reasons.png')

# =================== Cancellations by Vehicle Type ====================
st.subheader("▪ Cancellations by Vehicle Type")
st.image(r'Plots/cancellation by vehicle type.png')

# =================== Distribution of ratings ====================
st.subheader("▪ Distribution of Ratings")
st.image(r'Plots/distribution of ratings.png')

# =================== Distribution of ratings kde ====================
st.subheader("▪ Distribution of Ratings KDE")
st.image(r'Plots/driver vs customer ratings kde.png')

# =================== Comparing High vs Low rated rides ====================
st.subheader("▪ Comparing High vs Low Rated Rides")
df['High Rating'] = df['Customer Rating'] >= 4
st.dataframe(
        df.groupby('High Rating').agg({
        'Ride Distance':'mean',
        'Booking Value':'mean',
        'Cancelled Rides by Customer':'sum',
        'Cancelled Rides by Driver':'sum'
    })
)

# =================== Distance vs customer ratings ====================
st.subheader("▪ Distance vs customer ratings")
st.image(r'Plots/ride distance vs customer ratings.png')

# =================== Payment Method vs Booking Value ====================
st.subheader("▪ Payment Method vs Booking Value")
st.dataframe(df.groupby('Payment Method')['Booking Value'].mean().reset_index())