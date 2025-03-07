import streamlit as st
import requests



# FastAPI URL (Change this if running on a different server)
API_URL = "http://127.0.0.1:8000/predict/"

# Streamlit UI
st.title("SMS Spam Classifier 📩")
st.write("Type an SMS below and click **Scan** to check if it's Spam or Ham.")

# User Input
user_input = st.text_area("Enter your SMS here", "")

if st.button("Scan"):
    if user_input:
        # Send request to FastAPI backend
        response = requests.post(API_URL, json={"text": user_input})

        if response.status_code == 200:
            result = response.json()
            label = result["prediction"]
            model_used = result["model_used"]

            # Display Result
            if label == "spam":
                st.error(f"🚨 This message is **SPAM** ")
            else:
                st.success(f"✅ This message is **HAM**")
        else:
            st.error("Error: Could not connect to the API!")
    else:
        st.warning("⚠️ Please enter a message before scanning.")

