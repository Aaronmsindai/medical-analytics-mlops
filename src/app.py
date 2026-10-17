import streamlit as st
import requests

# 1. Point to your live Render API
API_URL = "https://medical-analytics-api.onrender.com/predict"

# 2. Set up clean page configuration
st.set_page_config(
    page_title="Medical Analytics Portal",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 Medical Analytics & Risk Prediction Portal")
st.markdown("""
This interactive interface communicates with a **live FastAPI backend** 
to serve predictions using verified patient metrics.
""")
st.write("---")

st.sidebar.header("📋 Patient Biometrics Input")

# 3. Build interactive UI entry forms (Changed Blood Pressure to Cholesterol to match API)
age = st.sidebar.slider("Age", min_value=1, max_value=100, value=45)
bmi = st.sidebar.slider("Body Mass Index (BMI)", min_value=10.0, max_value=50.0, value=24.5, step=0.1)
cholesterol = st.sidebar.slider("Cholesterol", min_value=100, max_value=400, value=200)

st.subheader("🔍 Real-time Inference Analysis")

# 4. Create an execution trigger button
if st.button("Run Diagnostic Prediction", type="primary"):
    with st.spinner("Calling the ML API..."):
        try:
            # Package data exactly as the API expects it
            payload = {
                "age": age,
                "bmi": bmi,
                "cholesterol": cholesterol
            }
            
            # Send the POST request to Render
            response = requests.post(API_URL, json=payload)
            response.raise_for_status() # Check for HTTP errors
            
            # Parse the response
            result = response.json()
            
            st.success("✅ Analysis completed successfully!")

            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="Model Risk Output", value=result["prediction_output"])
            with col2:
                st.metric(label="Model Confidence", value=f"{result['inference_confidence_percentage']}%")

            if "High Risk" in result["prediction_output"]:
                st.warning("⚠️ **Notice:** The model identifies elevated risk markers. Clinical evaluation advised.")
            else:
                st.info("💚 **Notice:** Metrics fall within baseline statistical regularities.")

        except requests.exceptions.RequestException as e:
            st.error(f"❌ Failed to connect to API: {e}")
        except Exception as e:
            st.error(f"❌ An error occurred: {e}")

st.write("---")
st.caption("Developed as part of the Medical Analytics MLOps Infrastructure Framework. Powered by FastAPI & Render.")
