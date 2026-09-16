![MLOps CI Status](https://github.com/Deodael/medical-analytics-mlops/actions/workflows/test.yml/badge.svg)

# 🏥 Medical Analytics MLOps Pipeline

> Production-grade MLOps pipeline for medical risk prediction — FastAPI serving, Streamlit UI, Docker containerization, and GitHub Actions CI/CD.

## 🎯 Live Demo

🚀 **[Access the Live Interactive App](https://medical-analytics-mlops-4lxy4tpzmb7jxqjhq6wtpy.streamlit.app)**

The Streamlit app runs the trained model **in-process** for the demo, ensuring reliability without external API dependencies. The FastAPI microservice architecture is available in the repo for local/containerized deployment:

```bash
docker-compose up --build
