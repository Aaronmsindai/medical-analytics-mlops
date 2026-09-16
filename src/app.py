import os
import streamlit as st
import joblib
import numpy as np

# 1. Load the model directly (no backend needed)
MODEL_PATH = os.path.join(os.path.dirname(__file__), "medical_model.pkl")
model = joblib.load(MODEL_PATH)

# 2. Set up clean page configuration
st.set_page_config(
    page_title="Medical Analytics Portal",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 Medical Analytics & Risk Prediction Portal")
st.markdown("""
This interactive interface runs a trained **machine learning model** directly 
to serve predictions using verified patient metrics.
""")
st.write("---")

st.sidebar.header("📋 Patient Biometrics Input")

# 3. Build interactive UI entry forms
age = st.sidebar.slider("Age", min_value=1, max_value=100, value=45)
bmi = st.sidebar.slider("Body Mass Index (BMI)", min_value=10.0, max_value=50.0, value=24.5, step=0.1)
blood_pressure = st.sidebar.slider("Systolic Blood Pressure", min_value=80, max_value=200, value=120)

# 4. Package the inputs into a structured array (3 features matching the trained model)
features = np.array([[
    age,
    bmi,
    blood_pressure
]])

st.subheader("🔍 Real-time Inference Analysis")

# 5. Create an execution trigger button
if st.button("Run Diagnostic Prediction", type="primary"):
    with st.spinner("Running model inference..."):
        try:
            prediction = int(model.predict(features)[0])

            # Get probability if the model supports it
            if hasattr(model, "predict_proba"):
                probability = float(model.predict_proba(features)[0][1])
            else:
                probability = float(prediction)

            st.success("✅ Analysis completed successfully!")

            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="Model Risk Output Classification", value=f"Category {prediction}")
            with col2:
                st.metric(label="Calculated Statistical Probability", value=f"{probability * 100:.1f}%")

            if probability > 0.5:
                st.warning("⚠️ **Notice:** The model identifies elevated risk markers. Clinical evaluation advised.")
            else:
                st.info("💚 **Notice:** Metrics fall within baseline statistical regularities.")

        except Exception as e:
            st.error(f"❌ Model inference failed: {e}")

st.write("---")
st.caption("Developed as part of the Medical Analytics MLOps Infrastructure Framework.")
