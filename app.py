import pandas as pd
import streamlit as st
import joblib


# Page setup

st.set_page_config(page_title = "Digital Anxiety Predictor", page_icon="🧠")
st.title("🧠 Digital Anxiety Predictor")
st.write("Enter your daily digital habits below to see your predicted anxiety level.")



# Load The Brains

@st.cache_resource

def load_models():

    model = joblib.load('notebooks/anxiety_rf_model.pkl')
    
    scaler = joblib.load('notebooks/anxiety_scaler.pkl')

    return model, scaler

model, scaler = load_models()



# User Interface (Side Bar)

st.sidebar.header("Your Daily Habits")

sleep_hours = st.sidebar.slider("Sleep Hours", min_value = 0.0, max_value = 12.0)
screen_time = st.sidebar.slider("Daily Screen Time (Minutes)",min_value=0, max_value=1000, value=300)
social_media = st.sidebar.slider("Social Media Time (Minutes)", min_value=0, max_value=600, value=120)
digital_wellbeing = st.sidebar.slider("Digital Wellbeing Score", min_value=30.0, max_value=85.0, value=52.0)

st.sidebar.markdown("---") 

notifications = st.sidebar.slider("Daily Notifications", min_value=0, max_value=200, value=50)
app_switches = st.sidebar.slider("App Switches per hour", min_value=0, max_value=100, value=20)
focus_score = st.sidebar.slider("Focus Score", min_value=0.0, max_value=10.0, value=5.0)
mood_score = st.sidebar.slider("Mood Score", min_value=0.0, max_value=10.0, value=5.0)



st.write("### Your Input Data")
st.write(f"- **Sleep:** {sleep_hours} hours")
st.write(f"- **Screen Time:** {screen_time} minutes")
st.write(f"- **Digital Wellbeing:** {digital_wellbeing}/100")




#  PREPARE THE DATA FOR THE MODEL ---
# We pack the user's inputs into a Pandas DataFrame (just like our training data)



input_data = pd.DataFrame({
    'daily_screen_time_min': [screen_time],
    'num_app_switches': [app_switches],
    'sleep_hours': [sleep_hours],
    'notification_count': [notifications],
    'social_media_time_min': [social_media],
    'focus_score': [focus_score],
    'mood_score': [mood_score],
    'digital_wellbeing_score': [digital_wellbeing]
})


# Draws a Visual dividing line

st.write("---")   



# THE PREDICTION BUTTON --- 

       # Run Ai only when user clicks button

if st.button("Predict My Anxiety level") :

    scaled_data = scaler.transform(input_data)   

    prediction = model.predict(scaled_data)


    st.write("### 🤖 The AI Predicts:")


    if prediction[0] == 'Low':

        st.success("🌟 Low Annxiety - Great job managing your digital habits!")

    elif prediction[0] == 'Medium':

        st.warning("⚠️ Medium Anxiety - You might want to watch your screen time.")

    else:

        st.error("🚨 High Anxiety - It is  highly recommended to disconnect and take a break.")

