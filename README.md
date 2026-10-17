![MLOps CI Status](https://github.com/Aaronmsindai/medical-analytics-mlops/actions/workflows/test.yml/badge.svg)

# 🏥 Medical Analytics MLOps Pipeline

> Production-grade MLOps pipeline for medical risk prediction — FastAPI serving, Streamlit UI, Docker containerization, and GitHub Actions CI/CD.

## 🎯 Live Demos

🚀 **[Access the Live Interactive App (Streamlit)](https://medical-analytics-mlops-4lxy4tpzmb7jxqjhq6wtpy.streamlit.app)**  
⚙️ **[Access the Live FastAPI Swagger Docs (Render)](https://medical-analytics-api.onrender.com/docs)**

*(Note: The Render API runs on a free tier and may take ~30 seconds to wake up on the first request).*



## 📐 System Architecture & MLOps Pipeline

This repository implements a production-grade, containerized MLOps pipeline designed with a separation of concerns between model training, API delivery, and automated verification.

### 🏗️ Core Architecture Components

1. **Training Pipeline (`train_model.py`)**
   * Responsible for ingestion, data preprocessing, and model training.
   * Serializes the final trained model into a production-ready binary format (`src/medical_model.pkl`) using `joblib`.
2. **Prediction Service (`src/main.py`)**
   * Built on FastAPI for high-performance, asynchronous REST API serving.
   * Utilizes Pydantic data structures to strictly validate incoming biometrics and patient payloads before executing inference.
3. **Automated Verification (`tests/test_api.py`)**
   * Configured with `pytest` to run deterministic component validation.
   * Verifies API response codes (200 OK, 422 Unprocessable Entity), schema integrity, and model inference accuracy.
4. **Continuous Integration (`.github/workflows/test.yml`)**
   * Automated orchestration via GitHub Actions triggered on every push or `pull_request` to `main`.
   * Provisions an isolated `ubuntu-latest` runner, configures a cached Python 3.11 environment, installs dependencies, and runs the test suite to guarantee zero-downtime stability.
5. **Interactive Presentation Layer (`src/app.py`)**
   * Built on Streamlit to provide an intuitive, web-based graphical user interface for medical staff.
   * Sends asynchronous HTTPS POST requests to the FastAPI backend to retrieve real-time predictions.



## 🌐 Production Infrastructure & Deployment

The system is designed as a fully decentralized, decoupled microservice cluster, portable across any container platform:

* **Frontend Client (Streamlit Community Cloud):** Hosts the presentation layer. It manages client-side states, captures real-time biometric indicators, and handles asynchronous HTTPS networking to ship data payloads across the web.
* **API Gateway & Inference Container (Render):** Ships an isolated `src/Dockerfile.backend` image that deploys to Render. Processes inbound JSON metrics through the serialized `medical_model.pkl` pipeline to deliver prediction results in milliseconds.


## 🛠️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Model** | `scikit-learn` (Logistic Regression) |
| **API** | FastAPI + Pydantic |
| **Frontend** | Streamlit + Requests |
| **Containerization** | Docker + Docker Compose |
| **CI/CD** | GitHub Actions |
| **Testing** | Pytest |
| **Language** | Python 3.11 |


## 🚀 How to Run Locally

### Option 1: Docker (full microservice stack)

git clone https://github.com/Aaronmsindai/medical-analytics-mlops.git
cd medical-analytics-mlops
docker-compose up --build
· FastAPI backend: http://localhost:8000/docs
· Streamlit frontend: http://localhost:8501

Option 2: Streamlit only (quick demo)


pip install -r requirements.txt
streamlit run src/app.py




🧪 Running Tests

```bash
pytest tests/




📂 Project Structure

```text
medical-analytics-mlops/
├── .github/workflows/      # CI/CD pipelines
├── src/
│   ├── app.py              # Streamlit UI
│   ├── main.py             # FastAPI service
│   ├── train_model.py      # Model training pipeline
│   ├── Dockerfile.backend  # Backend container
│   └── medical_model.pkl   # Trained model artifact
├── tests/                  # Pytest suite
├── Dockerfile              # Frontend container
├── Dockerfile.frontend
├── docker-compose.yml
├── requirements.txt
└── README.md
```



📊 Model Details

· Algorithm: Logistic Regression
· Features: Age, BMI, Cholesterol
· Output: Binary risk classification (0 = Low Risk Profile, 1 = High Risk Profile)
· Serialization: Joblib (.pkl)



🤝 Contributing

This is a personal portfolio project, but suggestions and feedback are welcome via issues.

📜 License

MIT License — free to use, modify, and distribute.
