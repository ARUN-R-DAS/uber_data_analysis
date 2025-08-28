import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
import os
import base64

st.set_page_config(layout="wide")

st.title("Uber data EDA by ARUN R DAS")
# ================================================== bg image ==========================

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
# ================== insights box style ===========================================
st.markdown("""
    <style>
    .insight-box {
        background-color: rgba(0,0,0,0.6);
        padding: 15px;
        border-radius: 10px;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)
# ==================================================================================

# =================== Loading df =========================================
df = pd.read_csv(r'Assets\ncr_ride_bookings.csv')

# =================== Overview section ===================================
st.subheader("▪ Dataset Overview")
st.dataframe(df.head())

# =================== Monthly Rides and Booking Value ====================
st.subheader("▪ Monthly Rides and Booking Value")
st.image(r'Plots\montly rides vs booking value.png')
st.markdown("""
            <div class="insight-box">
            <ul>
            <li> Feb & Aug have highest ride bookings.
            <li> Mar has the lowerst bookings and booking value.
            <li> Booking Value and number of bookings generally move together, but not always aligned.
            <li> After Aug peak, there's a consistent decline in rides until Oct.
            <li> During Dec to Jan, rides continue to fall slightly, while booking value remains relatively stable.
            <li style="color: #e63946"> Launch a "March Momentum" campaign with ride discounts, loyalty bonuses or referral incentives to re-engage users and boost demand.
            <li style="color: #e63946"> Promote holiday travel packgages, premium ride tiers during this period to maximize revenue from fewer but more valuable bookings.
            </ul>
            </div>
""", unsafe_allow_html=True)

# =================== Count Plots ====================
st.subheader("▪ Count Plots")
st.image(r'Plots/countplots.png')
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
                <div class="insight-box">
                <ul>
                <li>  <b>Booking Status</b>
                    <ul>
                    <li> Majority of the bookings are completed
                    <li> Driver cancellations are higher than customer cancellations
                    <li> 'No driver found' and 'Incomplete' cases are relatively low.
                    <li style="color: #e63946"> Reduce driver cancellations through better incentives and support.
                    <li style="color: #e63946"> Maintain "No driver found" cases by optimizing driver supply in peak zones.
                    </ul>
                <li> <b>Vehicle Type</b>
                    <ul>
                    <li> Auto has the highest ride count, followed by Go Mini and Go Sedan.
                    <li> Uber XL is the least used vehicle type.
                    <li> Small cars and autos dominate demand.
                    <li style="color: #e63946"> Focus marketing and fleet expansion on Auto, Go Mini and Go Sedan.
                    <li style="color: #e63946"> Reevaluate Uber XL offering- consider repositioning or phasing out.
                    </ul>
                <li> <b>Customer Cancellation Reasons</b>
                    <ul>
                    <li> Top reasons : 
                        <ul>
                        <li> Driver not moving to pickup location
                        <li> Driver asked to cancel
                        <li> Wrong adress
                        <li> Change of plans
                        <li style="color: #e63946"> Improve driver compliance and tracking to reduce "driver not moving" issues.
                        <li style="color: #e63946"> Enhance address input UX and offer flexible cancellation options.
                        </ul>
                    <li> AC not working is the least common reason.
                    </ul>
                </ul>
                </div>
    """, unsafe_allow_html=True) 

with col2:
    st.markdown("""
                <div class="insight-box">
                <ul>
                    <li> <b>Driver Cancellation Reasons</b>
                    <ul>
                    <li> All reasons have similar frequency.
                    <li> No single driver<li>related reason dominates cancellations.
                    <li style="color: #e63946"> Implement proactive vehicle maintenance checks and offer flexible scheduling to accomodate driver needs.
                    <li style="color: #e63946"> Improve rider behaviour tracking and offer drivers the ability to flag problematic customers discreetly.
                </ul>
                <li> <b>Incomplete Rides Reasons</b>
                    <ul>
                    <li> Vehicle breakdown, other issues and customer demand occur at almost equal levels.
                    <li> Suggests multiple operational inefficiencies, not just a single bottleneck.
                    <li style="color: #e63946"> Implement ride audit tools to identify and resolve breakdowns and service gaps.     
                </ul>
                <li> <b>Payment Method</b>
                    <ul>
                    <li> UPI is the most preferred method followed by cash.
                    <li> Debit card, credit card and wallets are relatively less used.
                    <li style="color: #e63946"> Strengthen UPI experience and cash-handling protocols.
                    <li style="color: #e63946"> Promote digital payments and wallets via rewards.   
                </ul>
                </ul>
                </div>
    """, unsafe_allow_html=True) 

# =================== Hist Plots ====================
st.subheader("▪ Hist Plots")
st.image(r'Plots/histplots.png')

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
                <div class="insight-box">
                <ul>
                <li>  <b>Booking Value</b>
                    <ul>
                    <li> The distribution is heavily right-skewed meaning most bookings are low in value.
                    <li style="color: #e63946"> Customers could be segmented based on booking value to tailor promotions or loyalty rewards
                </ul>
                <li> <b>Ride Distance</b>
                    <ul>
                    <li> The distribution is relatively uniform, suggesting a wide range of ride distances.
                    <li style="color: #e63946"> Optimize pricing models to reflect this diversity- maybe offer flat rates for short rides and dynamic pricing for longer ones.
                </ul>
                <li> <b>VTAT</b>
                    <ul>
                    <li> The histogram shows multiple peaks, meaning driver arrival times vary widely.
                    <li> This could be due to differences in traffic, driver density, or geographic spread.
                    <li> Some drivers reach quickly, others take longer possibly due to being farther away or navigating congested areas.
                    <li style="color: #e63946"> Optimize dispatch logic to assign closer drivers.
                    <li style="color: #e63946"> Identify high VTAT zones and consider driver incentives or repositioning strategies
                </ul>
                </div>
    """, unsafe_allow_html=True) 

with col2:
    st.markdown("""
             <div class="insight-box">
                <ul>
                <li> <b>CTAT</b>
                    <ul>
                    <li> The distribution is fairly uniform, with some fluctuations.
                    <li> While many customers are prompt, a noticeable portion takes longer to get ready- perhaps due to last minute prep, location confusion or app delays.
                    <li style="color: #e63946"> Introduce gentle nudge or reminders when the driver is nearing arrival.
                    <li style="color: #e63946"> Offer pickup readiness tracking (example : "Your driver is 2 minutes away, please be ready")
                    </ul>
                <li> <b>Customer Rating</b>
                    <ul> 
                    <li>Most customers are either very satisfied or neutral; few are extremely dissatisfied.
                    <li style="color: #e63946">Analyze low-rating feedback to identify recurring issues. Also reward high-rated drivers to reinforce good service.
                    </ul>
    """, unsafe_allow_html=True)
# =================== Box Plots ====================
st.subheader("▪ Box Plots")
st.image(r'Plots/boxplots.png')

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
                <div class="insight-box">
                <ul>
                <li>  <b>VTAT</b>
                    <ul>
                    <li> VTAT shows moderate variability, with most vehicles prepared within 7-8 minutes.
                    <li style="color: #e63946"> Standardize vehicle readiness protocols to reduce delays.
                <li style="color: #e63946"> Identify and address operational inefficiencies in high-VTAT zones.
                </ul>
                <li> <b>CTAT</b>
                    <ul>
                    <li> CTAT is relatively consistent with most customers ready within 29 minutes even though high.
                    <li style="color: #e63946"> Introduce customer notifications and reminders to reduce wait time.
                <li style="color: #e63946"> Monitor high CTAT cases to identify behavioral or location-based patterns.
                </ul>
                <li> <b>Booking Value</b>
                    <ul>
                    <li> Majority of bookings fall around 500 Rupees, but there is a long tail of high-value rides indicating a skewed distribution.
                    <li style="color: #e63946"> Segment high-value bookings for premium service optimization
                </ul>
                </div>
    """, unsafe_allow_html=True) 

with col2:
    st.markdown("""
             <div class="insight-box">
                <ul>
                <li> <b>Ride Distance</b>
                    <ul>
                    <li> Rides distances vary widely with a median around 25 kms, indicating a mix of short and long trips.
                    <li style="color: #e63946"> Adjust driver allocation and pricing strategies based on distance clusters.
                    </ul>
                <li> <b>Driver Rating</b>
                    <ul> 
                    <li> Driver ratings are generally high, with a median near 4.3, though some outliers suggest performance concerns.
                    <li style="color: #e63946"> Provide coaching and support for low-rated drivers
                <li style="color: #e63946"> Recognize and reward consistently high performers to maintain service quality.
                    </ul>
                <li> <b>Customer Rating</b>
                    <ul> 
                    <li>Customer ratings mirror driver ratings, with most customers rated positively and a few outliers indicating problematic behaviour.
                    <li style="color: #e63946"> Monitor low-rated customers for recurring issues.
                    <li style="color: #e63946"> Use ratings to personalize service and enhance loyalty programs.
                    </ul>
    """, unsafe_allow_html=True)

# =================== Joint Plots ====================
st.subheader("▪ Joint Plots")
st.image(r'Plots/jointplot.png')

st.markdown("""
             <div class="insight-box">
                <ul>
                    <li> The highest density of ratings occurs around Driver Rating ~ 4.25 and Customer Rating ~ 4.75.
                    <li> Suggesting that most interactions are positively rated but drivers tend to rate slightly lower than customers.
                    <li style="color: #e63946"> Calibrate expectations: Educate drivers on common customer rating behaviours to reduce frustration and improve service consistency.
                    <li style="color: #e63946"> Enhance feedback prompts: Use targeted follow-up questions after rides to conver subtle service gaps.
                </ul>
    """, unsafe_allow_html=True) 
# =================== Scatter Plots ====================
st.subheader("▪ Scatter Plots")
st.image(r'Plots/scatter.png')
st.markdown("""
             <div class="insight-box">
                <ul>
                    <li> There's high variability in booking value across all ride distances, indicating that ride distance alone doesn't reliably predict booking value.
                    <li style="color: #e63946"> Refine pricing models by incorporating additional variables like time of day, demand surges or service type to better explain booking value fluctuations.
                    <li style="color: #e63946"> Segment rides into categories (Example: short distance-high value vs long distance-low value) to tailor promotions or optimize resource allocation.
                </ul>
    """, unsafe_allow_html=True) 

# =================== Heatmap ====================
st.subheader("▪ Heatmap Plots")
st.image(r'Plots/heatmap.png')
st.markdown("""
             <div class="insight-box">
                <ul>
                    <li> Avg CTAT and Ride Distance show the strongest correlation at 0.102 followed by Avg VTAT and Ride Distance (0.063) and Avg CTAT and Avg VTAT (0.062). All other correlations are negligible indicating weak linear relationships across most variables.
                    <li style="color: #e63946"> Target long-distance rides for turnaround optimization: Since longer rides tend to stretch customer turnaround time, streamlining post-ride processes could improve efficiency.
                    <li style="color: #e63946"> Monitor Avg VTAT and Avg CTAT together. Even with modest correlation, improving one may subtly influence the other and enhance overall fleet responsiveness.
                </ul>
    """, unsafe_allow_html=True) 

# =================== Monthly Rides and Booking Value ====================
st.subheader("▪ Vehicle types and Booking Value")
styled_df = (
    df.groupby('Vehicle Type')['Booking Value']
    .mean()
    .sort_values()
    .reset_index()
)
st.dataframe(styled_df, use_container_width=True)

st.markdown("""
             <div class="insight-box">
                <ul>
                    <li> Go Sedan has the highest average booking value and Uber XL has the least. Though overall range range across vehicle types is quite narrow.
                    <li style="color: #e63946"> Focus premium strategies on Go sedan: Its slightly higher booking value may reflect preference on pricing leveragae, making it a good candidate for loyalty perks or upselling.
                    <li style="color: #e63946"> Standardize pricing tiers: Since booking values are tightly clustered, consider simplifying fare structures to reduce customer confusion and improve operational clarity.
                    <li style="color: #e63946"> Promotions and offers or even upgrading regular customers to Uber XL services will provide exposure to the service and improve its value.
                </ul>
    """, unsafe_allow_html=True) 

# =================== Location based insights ====================
location_popularity = df['Pickup Location'].value_counts().sort_values()
st.subheader("▪ Pickup Location Popularity")

col1, col2 = st.columns(2)

with col1:
    st.write("▪ Popular Pickup Locations")
    st.dataframe(location_popularity.tail(10))
with col2:
    st.write("▪ Least Popular Pickup Locations")
    st.dataframe(location_popularity.head(10))

st.markdown("""
             <div class="insight-box">
                <ul>
                    <li> The difference between the most and leasat popular pickup locations is relatively small, suggesting a fairly even distribution of demand across all the pickup locations.
                    <li style="color: #e63946"> Optimize drive allocation across all zones, not just high-demanded areas, to maintain service efficiency and reduce wait times.
                    <li style="color: #e63946"> Monitor emerging hotspots: Though currently less popular, may be growing- consider targeted promotions or increased visibility in these zones.
                </ul>
    """, unsafe_allow_html=True) 

# =================== Top 20 Routes ====================
st.subheader("▪ Top 20 Routes")
st.image(r'Plots/top 20 pickup_drop routes.png')

st.markdown("""
             <div class="insight-box">
                <ul>
                    <li> The route DLF City Court -> Bhiwadi stands out as the most frequented, but the overall trip counts across the top 20 routes are tightly clustered (mostly between 13-16) indicating broad and balanced demand across multiple routes rather than a single dominant route.
                    <li style="color: #e63946"> Ensure consistent vehicle availability across all top routes, not just the highest one, to maintain service quality and reduce wait times.
                    <li style="color: #e63946"> Route Based Promotions: Launch targeted offers or loyalty rewards on frequently travelled routes to encourage repeat usage and boost retention.
                    <li style="color: #e63946"> Shared Ride Opportunities: Explore pooling options on high-frquency routes to improve efficiency and margins. 
                </ul>
    """, unsafe_allow_html=True) 

# =================== Peak Booking Hours ====================
st.subheader("▪ Peak Booking Hours")
st.image(r'Plots/peak booking hours.png')

st.markdown("""
             <div class="insight-box">
                <ul>
                    <li> Booking activity follows a clear daily rhythm, with a sharp rise starting at 6AM peaking around 6PM (Hour 18) and tapering off into the night. This pattern suggests strong commuter or evening travel demand.
                    <li style="color: #e63946"> Peak Hour Reinforcement: Allocate more drivers and support staff between 6AM - 10AM and 4PM - 8PM to handle surges efficiently. 
                    <li style="color: #e63946"> Off-Peak Engagement: Offer discounts or loyalty perks during low-demand hours (Example: midnight to 5AM)
                </ul>
    """, unsafe_allow_html=True) 

# =================== Cancellation by Hour ====================
st.subheader("▪ Cancellation by Hour")
st.image(r'Plots/cancellation count by hour.png')

st.markdown("""
             <div class="insight-box">
                <ul>
                    <li> Cancellations peak between 4PM and 8PM with driver cancellations consistently outnumbering customer cancellations throughout the day. This trend suggests operational strain or mismatch during high-demand hours.
                    <li style="color: #e63946"> Driver Incentives During Peak Hours: Introduce bonuses or flexible shift options between the peak hours to reduce driver drop-offs when demand is highest.
                    <li style="color: #e63946"> Smart Matchin Algorithms: Improve ride-matching logic to minimize cancellations due to long wait times or poor route alignment.
                    <li style="color: #e63946"> Send proactive alerts or estimated wait times during peak hours to manage expectations and reduce voluntary cancellations.
                </ul>
    """, unsafe_allow_html=True) 

# =================== Pie plot : Rides cancelled ====================
st.subheader("▪ Pie plot : Rides cancelled")
st.image(r'Plots/pie_rides cancelled.png')

st.markdown("""
             <div class="insight-box">
                <ul>
                    <li> Driver-initiated cancellations account for 72% of all ride cancellations, significantly outweighing customer cancellations at 28 %
                    <li style="color: #e63946"> Introduce driver retention measures: Offer incentives, flexible scheduling or improved ride-matching to reduce cancellation rates and improve reliability.
                </ul>
    """, unsafe_allow_html=True) 

# =================== Top customer cancellation reasons ====================
st.subheader("▪ Top customer cancellation reasons")
st.image(r'Plots/top cust cancellation reasons.png')

st.markdown("""
             <div class="insight-box">
                <ul>
                    <li > Wrong addresses and drivers not heading toward pickup suggest issues with navigation or app accuracy.
                    <li > "Change of plans" is inevitable, but better scheduling options or cancellation policies might help.
                    <li > "Driver asked to cancel" is a red flag- possibly indicating poor driver - customer communication or lack of accountability.
                </ul>
    """, unsafe_allow_html=True) 

# =================== Top Driver cancellation reasons ====================
st.subheader("▪ Top Driver cancellation reasons")
st.image(r'Plots/top driver cancellation reasons.png')

st.markdown("""
             <div class="insight-box">
                <ul>
                    <li > Driver cancellations are not dominated by a single issue but rather spread across multiple recurring concerns.
                    <li > "Customer was coughing/sick" points to heightened sensitivity around hygiene and safety
                    <li > Overcrowding and general customer-related issues hint at mismatched expectations or poor communication.
                    <li > "Personal & Car-related issue" suggests operational gaps like vehicle maintenance or driver availability.

                </ul>
    """, unsafe_allow_html=True) 

# =================== Cancellations by Vehicle Type ====================
st.subheader("▪ Cancellations by Vehicle Type")
st.image(r'Plots/cancellation by vehicle type.png')

st.markdown("""
             <div class="insight-box">
                <ul>
                    <li> Driver-initiated cancellations account for 72% of all ride cancellations, significantly outweighing customer cancellations at 28 %
                    <li style="color: #e63946"> Introduce driver retention measures: Offer incentives, flexible scheduling or improved ride-matching to reduce cancellation rates and improve reliability.
                </ul>
    """, unsafe_allow_html=True) 

# =================== Distribution of ratings ====================
st.subheader("▪ Distribution of Ratings")
st.image(r'Plots/distribution of ratings.png')

st.markdown("""
<div class="insight-box">
            <ul>
            <li> Customer ratings peak at 5.0, showing a strong tendency toward perfect scores.
            <li> Driver ratings are more evenly spread, with fewer perfect scores and a gradual rise toward 4.5
            <li style="color: #e63946"> Prompt customers post-ride with reminders to rate drivers, nudging more 5-star ratings.
            <li style="color: #e63946"> Analyze driver feedback to uncover why they recieve fewer top ratings.
            </ul>
            """, unsafe_allow_html=True)

# =================== Distribution of ratings kde ====================
st.subheader("▪ Distribution of Ratings KDE")
st.image(r'Plots/driver vs customer ratings kde.png')

st.markdown("""
<div class="insight-box">
            <ul>
            <li> Driver ratings peak sharply around 4.2, suggesting a consistent but slightly conservative rating pattern.
            <li> Customer ratings show multiple peaks - around 4.3,4.6 and 4.9 indicating more variability and a tendency toward higher scores.
            <li style="color: #e63946"> Standardize rating prompts to reduce variability in customer ratings and ensure more consistent feedback.
            <li style="color: #e63946"> Explore driver performance at peak rating zones to identify what behaviours or experiences lead to higher customer ratings and replicate them across the board. 
            </ul>
            """,unsafe_allow_html=True)

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

st.markdown("""
<div class="insight-box">
            <ul>
            <li> High-rated rides have longer distances(26.04 vs 19.50), suggesting that longer trips may correlate with better experiences.
            <li> Cancellations are exclusive to low-rated rides, with both customer and driver cancellations significatly higher.
            <li style="color: #e63946"> Reduce cancellations to boost ratings - focus on improving reliability and communication to prevent ride drop-offs.
            <li style="color: #e63946"> Analyze long-ride experiences to identify what makes them more satisfying, then apply those learnings to shorter rides.
            </ul>
            """,unsafe_allow_html=True)

# =================== Distance vs customer ratings ====================
st.subheader("▪ Distance vs customer ratings")
st.image(r'Plots/ride distance vs customer ratings.png')

st.markdown("""
<div class="insight-box">
            <ul>
            <li> Customer ratings remain consistent across all ride distances - no clear upward or downward trend.
            <li> Dense clustering between 4.0 and 5.0 suggests most rides, regardless of length recieve high ratings.
            <li style="color: #e63946"> Focus on service quality over ride length - since distance doesn't impact ratings prioritize driver behaviour, comfort and reliability.
            <li style="color: #e63946"> Segment feedback by rating bands to uncover what differentiates a 4.0 from a 5.0 experience, independent of distance.
            </ul>
            """,unsafe_allow_html=True)

# =================== Payment Method vs Booking Value ====================
st.subheader("▪ Payment Method vs Booking Value")
st.dataframe(df.groupby('Payment Method')['Booking Value'].mean().reset_index())

st.markdown("""
<div class="insight-box">
            <ul>
            <li> Credit Card users have the highest average booking value, slightly above others.
            <li> Uber Wallet shows the lowerst booking value, though the difference is marginal.
            <li> Cash,UPI and Debit Card are all clustered closely around the 507-508 range.
            <li> Credit card users might be more comfortable spending more - possibly due to rewards, credit flexibility or higher income profiles.
            <li style="color: #e63946"> Offer targeted promotions for Uber Wallet users to boost their booking value
            <li style="color: #e63946"> Consider loyalty perks for credit users to reinforce their higher spending behaviour
            </ul>
            """,unsafe_allow_html=True)