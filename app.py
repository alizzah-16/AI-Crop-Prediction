import streamlit as st
import joblib
import numpy as np
import os
import random  # Added for fun fact

# Load the trained model
model = joblib.load("crop_recommendation_model.pkl")

# Crop image mapping
crop_images = {
    "rice": "crop_images/rice.jpg",
    "maize": "crop_images/maize.jpg",
    "chickpea": "crop_images/chickpea.jpg",
    "kidneybeans": "crop_images/kidneybeans.jpg",
    "pigeonpeas": "crop_images/pigeonpeas.jpg",
    "mothbeans": "crop_images/mothbeans.jpg",
    "mungbeans": "crop_images/mungbeans.jpg",
    "blackgram": "crop_images/blackgram.jpg",
    "lentil": "crop_images/lentil.jpg",
    "pomegranate": "crop_images/pomegranate.jpg",
    "banana": "crop_images/banana.jpg",
    "mango": "crop_images/mango.jpg",
    "grapes": "crop_images/grapes.jpg",
    "watermelon": "crop_images/watermelon.jpg",
    "muskmelon": "crop_images/muskmelon.jpg",
    "apple": "crop_images/apple.jpg",
    "orange": "crop_images/orange.jpg",
    "papaya": "crop_images/papaya.jpg",
    "coconut": "crop_images/coconut.jpg",
    "cotton": "crop_images/cotton.jpg",
    "jute": "crop_images/jute.jpg",
    "coffee": "crop_images/coffee.jpg"
}

# Styling
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(-45deg, #000000 25%, #f8c8dc 50%, #030d33 75%, #000000 100%);
        background-size: 400% 400%;
        animation: diagonalSweepOnce 2.5s ease-in-out forwards;
        color: white !important;
    }

    @keyframes diagonalSweepOnce {
        0% {
            background-position: 0% 50%;
        }
        25% {
            background-position: 25% 50%;
        }
        50% {
            background-position: 50% 50%;
        }
        75% {
            background-position: 75% 50%;
        }
        100% {
            background-position: 100% 50%;
        }
    }
    .big-font {
        font-size: 40px !important;
        color: white;
        text-align: center;
        padding: 20px;
        border-radius: 10px;
        background-color: rgba(152, 251, 152, 0.3);
        box-shadow: 0 0 20px rgba(152, 251, 152, 0.8);
        margin-bottom: 30px;
        animation: zoomInOut 5s ease infinite;
    }
    @keyframes zoomInOut {
        0% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.1);
        }
        100% {
            transform: scale(1);
        }
    }
    .description-text {
        font-size: 22px !important;
        text-align: center;
        padding: 10px;
        margin-bottom: 50px;
        color: #fff;
    }
    .rotation-box {
        border: 2px solid #f8c8dc;
        padding: 20px;
        background-color: rgba(248, 200, 220, 0.15);
        border-radius: 10px;
        font-size: 18px;
        color: #f8c8dc;
        margin-top: 20px;
        box-shadow: 0 0 12px rgba(248, 200, 220, 0.6);
        animation: floatTip 3s ease-in-out infinite;
    }
    .fun-fact {
        border: 2px solid #FFD1DC;
        background-color: rgba(255, 182, 193, 0.2);
        color: #FFD1DC;
        padding: 15px 20px;
        border-radius: 10px;
        box-shadow: 0 0 15px rgba(255, 182, 193, 0.5);
        font-size: 18px;
        text-align: center;
        margin-top: 30px;
        animation: slideIn 2s ease-out;
    }
    @keyframes slideIn {
        0% {
            transform: translateX(-100%);
            opacity: 0;
        }
        100% {
            transform: translateX(0);
            opacity: 1;
        }
    }
</style>
""", unsafe_allow_html=True)

# --- Welcome Page ---
if 'page' not in st.session_state or st.session_state.page != "input_page":
    st.markdown("<h2 class='big-font'>🌾 Welcome to the AI-powered Crop Recommendation System! 🌱</h2>", unsafe_allow_html=True)
    
    # Updated description with larger font
    st.markdown("<div class='description-text'>This system helps you choose the best crop for your farm based on soil conditions. 🌿</div>", unsafe_allow_html=True)

    # Fun Fact Feature
    fun_facts = [
        "💧 Did you know? Drip irrigation saves up to 70% of water.",
        "🌻 Sunflowers follow the sun – a phenomenon called heliotropism!",
        "🐛 Crop rotation reduces the risk of pest infestations naturally.",
        "🌾 Wheat was one of the first crops ever cultivated by humans.",
        "🍅 Tomatoes were once thought to be poisonous in Europe!",
        "🌽 Maize is a staple food in over 80 countries worldwide.",
        "🍌 Bananas are technically berries, but strawberries aren't!",
        "🥕 Carrots were originally purple, not orange."
    ]
    random_fact = random.choice(fun_facts)
    st.markdown(f"<div class='fun-fact'>🌟 Fun Fact: {random_fact}</div>", unsafe_allow_html=True)

    # Spacing between fun fact and button
    st.markdown("<br><br>", unsafe_allow_html=True)

    if st.button("Start the Recommendation Process"):
        st.session_state.page = "input_page"

# --- Input Page ---
if 'page' in st.session_state and st.session_state.page == "input_page":
    st.markdown("<h2 class='big-font'>Enter your soil parameters below to get a recommendation!</h2>", unsafe_allow_html=True)

    N = st.number_input("Nitrogen (N)", 0, 140, value=60)
    P = st.number_input("Phosphorus (P)", 5, 145, value=50)
    K = st.number_input("Potassium (K)", 5, 205, value=60)
    temperature = st.number_input("Temperature (°C)", 8.0, 43.0, value=25.0)
    humidity = st.number_input("Humidity (%)", 14.0, 100.0, value=60.0)
    ph = st.number_input("pH", 3.5, 9.5, value=6.5)
    rainfall = st.number_input("Rainfall (mm)", 20.0, 300.0, value=100.0)

    crop_rotation_tips = {
        "rice": "🌾 Rotate with legumes like mungbeans or chickpeas for nitrogen fixation. 🌱", 
        "maize": "🌽 Rotate with legumes or soybeans to improve soil fertility. 🌿", 
        "chickpea": "🌱 Rotate with cereals like wheat or maize to prevent soil depletion. 🌾", 
        "kidneybeans": "🫘 Rotate with cotton or wheat to maintain soil health. 🌾", 
        "pigeonpeas": "🌱 Rotate with cereal crops to improve soil structure. 🌾", 
        "mothbeans": "🌿 Rotate with crops like cotton or pulses. 🌱",
        "mungbeans": "🌱 Rotate with crops like maize or rice. 🌾", 
        "blackgram": "🫘 Rotate with maize or groundnut for soil health. 🌾", 
        "lentil": "🌿 Rotate with wheat or barley to reduce soil diseases. 🌾", 
        "pomegranate": "🍊 Rotate with legumes to maintain soil nutrients. 🌱", 
        "banana": "🍌 Rotate with cereals like rice or maize for healthy soil. 🌾", 
        "mango": "🥭 Rotate with pulses or legumes to reduce soil pressure. 🌿", 
        "grapes": "🍇 Rotate with legumes or other fruits like citrus. 🍊", 
        "watermelon": "🍉 Rotate with legumes or root crops for soil improvement. 🌱", 
        "muskmelon": "🍈 Rotate with maize or legumes to enhance soil nutrients. 🌾", 
        "apple": "🍏 Rotate with pulses or grasses to rejuvenate the soil. 🌿", 
        "orange": "🍊 Rotate with legumes to prevent nutrient depletion. 🌱", 
        "papaya": "🍍 Rotate with maize or legumes to improve soil health. 🌾",
        "coconut": "🥥 Rotate with legumes or vegetables to keep soil balanced. 🌱", 
        "cotton": "🌾 Rotate with pulses or rice to maintain soil structure. 🌱",
        "jute": "🧵 Rotate with pulses or vegetables for better soil health. 🌿", 
        "coffee": "☕ Rotate with legumes or other crops to enhance soil fertility. 🌱"
    }

    if st.button("Recommend Crop"):
        input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        prediction = model.predict(input_data)
        recommended_crop = prediction[0]

        st.success(f"✅ **Recommended Crop:** {recommended_crop.capitalize()}")

        image_path = crop_images.get(recommended_crop.lower())
        if image_path and os.path.exists(image_path):
            st.image(image_path, caption=f"{recommended_crop.capitalize()} Crop", use_column_width=True)
        else:
            st.warning("🔍 Image not found for this crop.")

        tip = crop_rotation_tips.get(recommended_crop.lower(), "🌱 No specific rotation tips available.")
        st.markdown(f"<div class='rotation-box'>{tip}</div>", unsafe_allow_html=True)

        st.info("🌾 These recommendations are based on AI analysis of your soil input. Always cross-check with a local expert!")

# Footer
st.markdown("""
    <hr style="margin-top: 40px;">
    <p style="text-align: center;">Made with ❤️ | AI Crop Recommendation System</p>
""", unsafe_allow_html=True)
