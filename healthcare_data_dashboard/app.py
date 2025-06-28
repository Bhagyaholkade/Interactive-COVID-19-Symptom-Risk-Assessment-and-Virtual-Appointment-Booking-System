import streamlit as st

st.set_page_config(page_title="Healthcare Dashboard Home", page_icon="🌍")

# 🌸 Sidebar Title & Navigation Info
st.sidebar.markdown("""
## 📊 Healthcare & COVID-19 Dashboard  

Use the sidebar menu to navigate between:

- 🌐 **Global Dashboard**
- 🩺 **Symptom Checker**
- ℹ️ **About Page**
""")

# 🌸 Welcome Title
st.title("🌍 Welcome to the Healthcare Data & COVID Symptom App")

# 🌸 Hero Banner
st.markdown("""
<div style="background-color:#FF4B4B;padding:15px;border-radius:12px;margin-bottom:25px">
    <h3 style="color:#fff;text-align:center">📊 Live COVID-19 Data Insights + 🩺 Symptom Self-Check & Booking Tool</h3>
</div>
""", unsafe_allow_html=True)

# 🌸 About the App
st.markdown("""
This interactive, multi-page application allows you to explore **global healthcare & COVID-19 trends** 📈 and run a **COVID Symptom Self-Check** 🩺, complete with animated UI effects for an immersive user experience.

---

## 📌 Features & Highlights

- 📊 **Global Healthcare Dashboard:**  
  View total COVID-19 cases, recoveries, deaths, hospital data, vaccination rates, and testing info worldwide using interactive maps, bar charts, pie charts, and line graphs.

- 🩺 **COVID Symptom Checker (with secure login):**  
  Enter your health details like symptoms, age, location, and temperature to receive instant risk assessment.  
  🏥 If necessary, it recommends nearby hospitals, allows appointment booking, and generates a detailed booking receipt.  
  *(Login credentials available on the 'About' page)*

- 🎨 **Animated Visual Backgrounds:**  
  Particle-based virus animation enhances the Symptom Checker interface for a dynamic, themed experience.

- 📥 **Download Custom Data:**  
  Filter and download country-specific or date-specific healthcare datasets directly as CSV.

---

## 🚀 How to Use This App

1. Use the **sidebar navigation** to switch between:
   - 🌐 *Global Dashboard*
   - 🩺 *COVID Symptom Checker*
   - ℹ️ *About Page*

2. Apply available **filters** in each section to customize the views and insights.

3. Run the Symptom Checker to get health advice, find hospital recommendations, and book appointments with receipts.

4. Explore project description, data source links, and login info via the **About page**.

---

## 🛠️ Built With

- 🐍 **Streamlit**
- 🐼 **Pandas**
- 📊 **Plotly**
- 🎨 **Custom HTML/CSS/JavaScript**
- ❤️ Passion for coding and healthcare solutions  

---

## 👩‍💻 Creator

This project was conceptualized and developed by **Bhagya Holkade**, integrating data analysis, health advisory logic, UI design, and interactive visualizations.

---

<div style="text-align:center;font-size:18px;margin-top:20px;">
✨ Stay informed. Stay safe. Stay healthy. ✨
</div>
""", unsafe_allow_html=True)
