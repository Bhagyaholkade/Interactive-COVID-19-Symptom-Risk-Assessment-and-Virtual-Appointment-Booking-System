import streamlit as st

st.set_page_config(page_title="About", page_icon="ℹ️")

st.title("ℹ️ About This Healthcare Data Dashboard")

# 🌸 Symptom Checker Access Instructions
st.markdown("""
<div style="background-color:#FFD700;padding:15px;border-radius:10px;margin-bottom:20px">
    <h3 style="color:#111;text-align:center">🔐 Symptom Checker Access</h3>
    <p style="color:#111;font-size:18px;text-align:center">
        To access the <strong>COVID Symptom Checker</strong> tool from the sidebar, use the login credentials provided here.  
        If you don't remember them — don't worry, you can always revisit this page anytime.
    </p>
    <p style="color:#111;text-align:center">
        ⚠️ <strong>Hint:</strong> Default username is typically set to <code>admin</code> and password to <code>covid123</code>  
        (You may confirm or retrieve these from your instructor if customized)
    </p>
</div>
""", unsafe_allow_html=True)

# 📊 Project Overview
st.markdown("""
## 📊 Project Overview

This multi-page interactive healthcare dashboard is built to visualize and analyze COVID-19 data globally, along with a custom COVID Symptom Checker tool.  
It allows users to select countries, time ranges, and see trends in cases, deaths, vaccinations, hospital infrastructure, and more, through interactive charts and maps.

Additionally, a password-protected Symptom Checker lets users input their personal symptoms and receive health guidance based on their responses.

---

## 💻 Technologies & Tools Used

- **Streamlit** → to build the web-based interactive UI and navigation  
- **Pandas** → for data loading, filtering, and processing  
- **Plotly** → for generating interactive visualizations like line charts, bar graphs, pie charts, choropleths, and animated charts  
- **HTML / CSS / JavaScript** → for custom backgrounds, styling, and embedding animated effects  
- **Our World In Data COVID-19 Dataset** → as the data source for global COVID-19 metrics  

---

## 🛠️ Symptom Checker Rules

- Enter your name, age, symptoms, and temperature.
- Your symptom score is calculated based on the number of symptoms selected.
- **If your symptom score is more than 50%** or you have a **fever ≥ 38°C**, you’ll be advised to consult a doctor.
- In such cases, a list of hospitals with available time slots will appear for you to book a hospital bed.
- **Payment options** like Cash, UPI, Card, or Netbanking are also available while confirming your booking.
- A styled booking receipt with your details, hospital address, and payment method will be generated after confirming.

---

## 📂 Project Structure Summary


---

## 📥 Data Source

The COVID-19 dataset used here is sourced from  
[Our World In Data COVID-19 Dataset](https://ourworldindata.org/coronavirus-data)

---

## 👩‍💻 About the Developer

This project is built by **Bhagya Holkade** as a hands-on data visualization and healthcare data analysis project.  
It was designed to combine **interactive data science dashboards with health advisory tools** — all accessible through a clean, web-based interface without any backend server.

Built with ❤️ using Streamlit, Pandas, Plotly, HTML, CSS, and a lot of coffee ☕.

---
""")
