import streamlit as st
from datetime import datetime

# 🌸 Page Config
st.set_page_config(page_title="COVID Symptom Checker", page_icon="🦠")

st.markdown("""
    <style>
    body {
        overflow-x: hidden;
    }
    .stApp {
        background-color: #0e0e0e;
        color: #fff;
    }
    .virus {
        position: fixed;
        font-size: 35px;
        animation: float 20s linear infinite;
        opacity: 0.6;
    }
    .virus:nth-child(1) {
        top: 10%;
        left: 5%;
        animation-delay: 0s;
        animation-duration: 18s;
    }
    .virus:nth-child(2) {
        top: 50%;
        left: 20%;
        animation-delay: 2s;
        animation-duration: 22s;
    }
    .virus:nth-child(3) {
        top: 80%;
        left: 75%;
        animation-delay: 4s;
        animation-duration: 20s;
    }
    .virus:nth-child(4) {
        top: 30%;
        left: 90%;
        animation-delay: 6s;
        animation-duration: 24s;
    }
    .virus:nth-child(5) {
        top: 60%;
        left: 40%;
        animation-delay: 3s;
        animation-duration: 26s;
    }
    .virus:nth-child(6) {
        top: 20%;
        left: 70%;
        animation-delay: 5s;
        animation-duration: 28s;
    }
    .virus:nth-child(7) {
        top: 70%;
        left: 10%;
        animation-delay: 7s;
        animation-duration: 30s;
    }
    .virus:nth-child(8) {
        top: 40%;  
        left: 30%;
        animation-delay: 9s;
        animation-duration: 32s;
    }
    .virus:nth-child(9) {
        top: 90%;
        left: 60%;
        animation-delay: 11s;
        animation-duration: 34s;
    }
    .virus:nth-child(10) {
        top: 15%;
        left: 80%;
        animation-delay: 13s;
        animation-duration: 36s;
    }
    @keyframes float {
        0% { transform: translateY(0) rotate(0deg); }
        50% { transform: translateY(-30px) rotate(180deg); }
        100% { transform: translateY(0) rotate(360deg); }
    }
    </style>
    <div class="virus">🦠</div>
    <div class="virus">🦠</div>
    <div class="virus">🦠</div>
    <div class="virus">🦠</div>
    <div class="virus">🦠</div>
    <div class="virus">😷</div>
    <div class="virus">🩺</div>
    <div class="virus">💉</div>
    <div class="virus">🚑</div>
    <div class="virus">🏥</div>
    
""", unsafe_allow_html=True)

# Title
st.title("🩺 COVID Symptom Checker")
st.write("🦠 Floating virus animation working — no JavaScript needed!")


# 🌸 Session State init
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "show_booking_section" not in st.session_state:
    st.session_state.show_booking_section = False
if "booking_history" not in st.session_state:
    st.session_state.booking_history = []

# 🌸 Login Function
def login_check():
    def credentials_entered():
        if st.session_state["username"] == "admin" and st.session_state["password"] == "covid123":
            st.session_state.authenticated = True
            del st.session_state["username"]
            del st.session_state["password"]
        else:
            st.session_state.authenticated = False

    if not st.session_state.authenticated:
        st.markdown("<h2 style='color:#FFD700;'>🛡️ Secure Access</h2>", unsafe_allow_html=True)
        st.markdown("Enter your secure credentials to proceed.")
        st.info("🔐 Hint: Hey there! If you’re unsure about the username and password, just hop over to the About page via the sidebar.")
        st.text_input("👤 Username", key="username")
        st.text_input("🔑 Password", type="password", key="password")
        st.button("Login", on_click=credentials_entered)
        return False
    else:
        return True

# 🌸 Main App
if login_check():
    st.title("🩺 COVID-19 Symptom Checker")

    name = st.text_input("👤 Enter your Name")
    age = st.number_input("🎂 Enter your Age", min_value=1, max_value=120)

    states = {
        "Karnataka": ["Bengaluru", "Mysuru", "Mangaluru"],
        "Maharashtra": ["Mumbai", "Pune", "Nagpur"],
        "Telangana": ["Hyderabad", "Warangal"],
        "Delhi": ["New Delhi"],
        "Tamil Nadu": ["Chennai", "Coimbatore"]
    }

    selected_state = st.selectbox("🏙️ Select your State", ["Select"] + list(states.keys()))
    if selected_state != "Select":
        selected_city = st.selectbox("🏙️ Select your City", ["Select"] + states[selected_state])
    else:
        selected_city = None

    st.subheader("🦠 Select your Symptoms")
    symptoms_list = [
        'Fever', 'Dry Cough', 'Fatigue', 'Difficulty Breathing',
        'Loss of Taste/Smell', 'Sore Throat', 'Headache',
        'Body Pain', 'Chest Pain', 'Nausea', 'Diarrhea'
    ]
    symptoms = st.multiselect("Choose symptoms you're experiencing:", symptoms_list)
    fever_degree = st.slider("🌡️ Select your temperature (°C):", 35.0, 42.0, 36.5)

    hospitals = {
        "Bengaluru": ["Manipal Hospital", "Fortis", "Apollo Hospitals", "Aster CMI"],
        "Mumbai": ["Nanavati Max", "Kokilaben Dhirubhai Ambani", "Hiranandani"],
        "Hyderabad": ["Yashoda Hospitals", "Care Hospitals", "Continental"],
        "New Delhi": ["AIIMS Delhi", "Max Super Specialty", "BLK Hospital"],
        "Chennai": ["Apollo Hospital", "MIOT International", "Fortis Malar"]
    }

    if st.button("🔍 Check My Status"):
        if not name or age == 0 or selected_state == "Select" or selected_city == "Select" or selected_city is None:
            st.error("⚠️ Please fill Name, Age, State, and City.")
        else:
            matching_count = len(symptoms)
            total_symptoms = len(symptoms_list)
            symptom_percentage = (matching_count / total_symptoms) * 100

            if symptom_percentage >= 50 or fever_degree >= 38:
                st.error(f"⚠️ {name}, your symptom score is {symptom_percentage:.1f}%. You should consult a doctor immediately.")
                st.session_state.show_booking_section = True
            else:
                st.session_state.show_booking_section = False
                st.success(f"✅ {name}, your symptom score is {symptom_percentage:.1f}%. You can rest at home and stay safe.")

    # 🌸 Booking Section
    if st.session_state.show_booking_section and selected_city in hospitals:
        st.markdown(f"### 🏥 Available Hospitals in {selected_city}:")
        selected_hospital = st.selectbox("🏥 Select a Hospital", hospitals[selected_city])
        mobile = st.text_input("📱 Enter your Mobile Number")
        slots = ["10:00 AM", "11:30 AM", "1:00 PM", "3:00 PM", "5:00 PM"]
        selected_slot = st.selectbox("🗓️ Select a Time Slot for Today", slots)

        if st.button("✅ Confirm Booking"):
            if mobile:
                booking = {
                    "Name": name,
                    "Mobile": mobile,
                    "State": selected_state,
                    "City": selected_city,
                    "Hospital": selected_hospital,
                    "Date": datetime.today().strftime('%d-%b-%Y'),
                    "Time": selected_slot
                }
                st.session_state.booking_history.append(booking)
                st.success("✅ Booking Confirmed!")
                st.markdown(f"""
                    <div style="background-color:#f8f9fa;padding:20px;border-radius:10px;">
                        <h4 style="color:#FF4B4B;">📋 Booking Receipt</h4>
                        <p><strong>Name:</strong> {name}</p>
                        <p><strong>Mobile:</strong> {mobile}</p>
                        <p><strong>State:</strong> {selected_state}</p>
                        <p><strong>City:</strong> {selected_city}</p>
                        <p><strong>Hospital:</strong> {selected_hospital}</p>
                        <p><strong>Date:</strong> {booking['Date']}</p>
                        <p><strong>Time Slot:</strong> {selected_slot}</p>
                        <p style="color:green;"><strong>Status:</strong> Confirmed ✅</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.warning("📱 Please enter your mobile number.")

    elif st.session_state.show_booking_section and selected_city not in hospitals:
        st.warning("No hospitals registered in your city. Please visit your nearest facility.")

    # 🌸 Booking History Section
    if st.session_state.booking_history:
        st.markdown("### 📜 Your Booking History:")
        for idx, record in enumerate(st.session_state.booking_history, 1):
            st.markdown(f"""
                <div style="background-color:#f0f0f0;padding:10px;border-radius:8px;margin-bottom:5px;">
                    <strong>Booking {idx}</strong> - {record['Date']} at {record['Time']}<br>
                    {record['Hospital']} ({record['City']}, {record['State']})<br>
                    📱 {record['Mobile']}
                </div>
            """, unsafe_allow_html=True)

    if st.button("🔄 Reset All Data"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()

