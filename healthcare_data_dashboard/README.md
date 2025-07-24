
# 🦠 Interactive COVID-19 Symptom Risk Assessment & Virtual Appointment Booking System

A smart, user-friendly, and animated web application built using **Streamlit** that enables users to check their COVID-19 symptom risk and book virtual doctor appointments based on their responses.

## 🚀 Project Overview

This interactive platform allows users to:
- Assess their COVID-19 symptom risk through a questionnaire.
- View a visual dashboard of global COVID-19 stats.
- Book appointments with doctors based on the assessed risk.
- Generate booking confirmation receipts.
- Experience a sleek, animated, multi-page interface.

## 🎯 Features

- 🔐 **Login System** with hint-based access.
- 🧠 **Symptom Risk Classification** using user-selected symptoms.
- 📊 **Global COVID-19 Dashboard** using real-time APIs.
- 📅 **Appointment Booking** with persistent history and animated success receipt.
- 🌐 **Animated Backgrounds** using `particles.js` for a modern UI.
- 📑 **PDF Receipt** generation with user and appointment details.

## 🛠️ Tech Stack

| Layer        | Technology                             |
|--------------|----------------------------------------|
| **Frontend** | HTML, CSS, JavaScript, Streamlit       |
| **Backend**  | Python (Streamlit framework)           |
| **Styling**  | Custom CSS, Particle.js animations     |
| **Data**     | COVID-19 APIs, Session State Management|
| **Others**   | Animated login hints, PDF generation   |

## 📁 Project Structure

```
📂 COVID19_Symptom_Assessment_App/
├── pages/
│   ├── 1_Global_Dashboard.py
│   ├── 2_Symptom_Checker.py
│   └── 3_About.py
├── assets/
│   ├── background.js
│   └── styles.css
├── main.py
├── login.py
├── utils.py
├── requirements.txt
└── README.md
```

## 💻 How to Run the Project

1. **Clone the repository**
   ```bash
   git clone https://github.com/Bhagyaholkade/Interactive-COVID-19-Symptom-Risk-Assessment-and-Virtual-Appointment-Booking-System.git
   cd Interactive-COVID-19-Symptom-Risk-Assessment-and-Virtual-Appointment-Booking-System
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**
   ```bash
   streamlit run main.py
   ```

## 📸 Screenshots

> *(Add some screenshots of the dashboard, symptom checker, booking page, and animated background here if available)*

## 🔐 Login Hint

> 💡 Hint: Think like a doctor 🩺 and patient 👩‍⚕️ trying to log in — check `login.py` for default credentials or hint-based access.

## 🏥 Symptom Risk Logic

- If the user selects **more than 50%** of the symptoms listed, a hospital visit is **recommended**.
- If not, the user is advised to **rest at home** with care tips provided.

## 📄 PDF Receipt

- After booking, users receive a **confirmation receipt** with appointment date, time, and personal details.

## ✨ Credits

- Developed by **Bhagya Holkade** – Final Year Information Science Engineer
- UI/UX Design by Bhagya using Figma and animations
- COVID-19 data sourced from public APIs

## 🤝 Let's Connect

- [LinkedIn](https://www.linkedin.com/in/bhagya-holkade-39213425a/)
- [GitHub](https://github.com/Bhagyaholkade)

---

🧪 *A blend of tech and healthcare to promote awareness and smart symptom tracking!*
