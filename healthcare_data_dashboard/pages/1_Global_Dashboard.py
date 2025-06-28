import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio
import os
from PIL import Image

# ───────────────────────────────────────────────
# 🌸 Page Config
st.set_page_config(
    page_title="Global Healthcare Data Dashboard",
    page_icon="🌍",
    layout="wide"
)

# ───────────────────────────────────────────────
# 🌸 Dynamically resolve paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'healthcare_data.csv')
LOGO_PATH = os.path.join(BASE_DIR, 'images', 'logo.png')

# ───────────────────────────────────────────────
# 🌸 Load dataset
@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH, parse_dates=['date'])

@st.cache_data
def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

# ───────────────────────────────────────────────
# 🌸 Load Data
with st.spinner("📊 Loading data..."):
    df = load_data()
st.success("✅ Data loaded successfully!")

# ───────────────────────────────────────────────
# 🌸 Display Logo if available
if os.path.exists(LOGO_PATH):
    logo = Image.open(LOGO_PATH)
    st.image(logo, width=100)

# ───────────────────────────────────────────────
# 🌸 App Title and Description
st.markdown("<h1 style='color:#4CAF50;'>🌍 Global Healthcare Data Dashboard</h1>", unsafe_allow_html=True)
st.markdown("Explore COVID-19 healthcare trends, vaccinations, and more with interactive visualizations 📊")

# ───────────────────────────────────────────────
# 🌸 Sidebar Theme Toggle with dynamic CSS
theme_choice = st.sidebar.radio("🎨 Theme Mode", ['Light', 'Dark'])

if theme_choice == 'Dark':
    pio.templates.default = "plotly_dark"
    st.markdown(
        """
        <style>
        :root {
            --bg-color: #121212;
            --text-color: #F5F5F5;
            --card-color: #1E1E1E;
        }
        body, .stApp {
            background-color: var(--bg-color);
            color: var(--text-color);
        }
        .sidebar-content {
            background-color: var(--card-color);
        }
        </style>
        """, unsafe_allow_html=True)
else:
    pio.templates.default = "plotly_white"

# ───────────────────────────────────────────────
# 🌸 Sidebar Filters
st.sidebar.markdown("## 📊 Filters")

country_search = st.sidebar.text_input("🔍 Search Country")

if country_search:
    countries = [c for c in df['location'].unique() if country_search.lower() in c.lower()]
else:
    countries = st.sidebar.multiselect("🌐 Select Country(s)", df['location'].unique(), default=['India', 'United States'])

start_date = st.sidebar.date_input("📅 Start Date", value=pd.to_datetime('2021-01-01'))
end_date = st.sidebar.date_input("📅 End Date", value=pd.to_datetime('2022-12-31'))

# Sidebar COVID Symptom Checker link
st.sidebar.markdown("""
<hr>
<h3 style='margin-bottom:5px;'>🩺 COVID Symptom Checker</h3>
<a href="http://localhost:8502" target="_blank" style="text-decoration:none; font-size:16px; color:#4CAF50;">➤ Take Symptom Test</a>
""", unsafe_allow_html=True)

# ───────────────────────────────────────────────
# 🌸 Filter dataset
filtered_df = df[
    (df['location'].isin(countries)) &
    (df['date'] >= pd.to_datetime(start_date)) &
    (df['date'] <= pd.to_datetime(end_date))
]

if filtered_df.empty:
    st.warning("⚠️ No data available for selected filters. Please adjust your selection.")
else:
    filtered_df = filtered_df.copy()
    filtered_df['new_cases'] = filtered_df.groupby('location')['total_cases'].diff()

    # Summary KPIs
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🦠 Total Cases", f"{int(filtered_df['total_cases'].sum()):,}")
    col2.metric("☠️ Total Deaths", f"{int(filtered_df['total_deaths'].sum()):,}")
    col3.metric("💉 People Vaccinated", f"{int(filtered_df['people_vaccinated'].sum()):,}")
    col4.metric("🌏 Countries Selected", len(countries))

    if 'total_recovered' in filtered_df.columns:
        st.metric("💚 Total Recovered", f"{int(filtered_df['total_recovered'].sum()):,}")

    color_seq = px.colors.qualitative.Set1
    latest_vax_df = filtered_df.groupby('location').last().reset_index()

    st.markdown("### 📈 Total COVID-19 Cases Over Time")
    st.plotly_chart(px.line(filtered_df, x='date', y='total_cases', color='location', markers=True, color_discrete_sequence=color_seq), use_container_width=True)

    st.markdown("### 📊 Daily New COVID-19 Cases")
    st.plotly_chart(px.line(filtered_df, x='date', y='new_cases', color='location', markers=True, color_discrete_sequence=color_seq), use_container_width=True)

    st.markdown("### 💉 People Vaccinated (Latest Available)")
    st.plotly_chart(px.bar(latest_vax_df, x='location', y='people_vaccinated', color='location', color_discrete_sequence=color_seq), use_container_width=True)

    st.markdown("### ☠️ Deaths Distribution")
    st.plotly_chart(px.pie(latest_vax_df, names='location', values='total_deaths', color='location', color_discrete_sequence=color_seq), use_container_width=True)

    if 'hospital_beds_per_thousand' in latest_vax_df.columns:
        st.markdown("### 🏥 Hospital Beds per 1000 people")
        st.plotly_chart(px.bar(latest_vax_df, x='location', y='hospital_beds_per_thousand', color='location', color_discrete_sequence=color_seq), use_container_width=True)

    st.markdown("### 🌍 Geographical Spread (Total Cases)")
    st.plotly_chart(px.scatter_geo(latest_vax_df, locations="iso_code", color="location", hover_name="location", size="total_cases", projection="natural earth", color_discrete_sequence=color_seq), use_container_width=True)

    st.markdown("### 🌎 COVID-19 Heatmap (Total Cases)")
    st.plotly_chart(px.choropleth(latest_vax_df, locations="iso_code", color="total_cases", hover_name="location", color_continuous_scale="Reds", projection="natural earth"), use_container_width=True)

    st.markdown("### 📊 Total Cases Animated Over Time")
    st.plotly_chart(px.bar(filtered_df, x='location', y='total_cases', animation_frame='date', color='location', color_discrete_sequence=color_seq), use_container_width=True)

    # Download CSV
    csv_data = convert_df_to_csv(filtered_df)
    st.download_button("📥 Download Filtered Data as CSV", data=csv_data, file_name='filtered_healthcare_data.csv', mime='text/csv')

    with st.expander("📄 View Raw Data"):
        st.dataframe(filtered_df)

# ───────────────────────────────────────────────
# 🌸 About Section
with st.expander("ℹ️ About this Dashboard"):
    st.markdown("""
    This interactive dashboard visualizes COVID-19 healthcare data globally.

    **Features:**  
    📊 Total cases, deaths, vaccinations, infrastructure metrics  
    📅 Date and country filtering  
    🌎 Geo visualizations and animations  

    **Built with:** Streamlit, Pandas, Plotly  
    **Data Source:** [Our World In Data](https://ourworldindata.org/coronavirus-data)  
    📧 [Contact Bhagya Holkade](mailto:your.email@example.com)
    """)

# ───────────────────────────────────────────────
# 🌸 Footer
st.markdown("""
<hr style="border:1px solid #ccc">
<p style='text-align: center; font-size:14px;'>
    📊 Made with ❤️ by Bhagya Holkade | Data Source: Our World in Data
</p>
""", unsafe_allow_html=True)
