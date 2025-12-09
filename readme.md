# MLOps Fundamentals: Automated Model Retraining & Deployment Pipeline

## 🛑 Reviewer Instructions: Submission Checklist 🛑

**Before submitting for review**, developers **must** ensure the following requirements are met:

1. **Repository Forking & Naming:** This repository **must be forked** to your personal GitHub account and **renamed** exactly to:
   `MLOps-Fundamentals-Capstone-AutoRetrain-Pipeline`
2. **Language Requirement:** All code must be implemented using **Python**.
3. **Topic Coverage:** The implementation must cover core MLOps concepts including model training, versioning, deployment, monitoring, and automated retraining.
4. **Complete Documentation:** All sections of this README (Requirements, Execution, Views) must be fully completed with project-specific details, code, and screenshots.

-----

## 🌟 Project Summary

This project involves building a **complete MLOps pipeline** for **SMS spam detection** that automates the entire machine learning lifecycle from training to deployment and monitoring. The core objective is to create a system that trains text classification models, versions them using MLflow, deploys them via Docker containers, monitors for data drift in message patterns, and automatically triggers retraining when performance degrades or drift exceeds predefined thresholds.

This project serves as a **fundamental MLOps implementation** that teaches core concepts of model lifecycle management, automated retraining, and monitoring, applied to a real-world NLP use case.

### Project Timeline

* **MVP (Minimum Viable Product):** 2 weeks part-time
* **Full Implementation:** 4 weeks part-time

### Key Technologies

* **ML Framework:** scikit-learn for model training (Naive Bayes, Logistic Regression, SVM)
* **NLP:** TfidfVectorizer for text feature extraction, NLTK for preprocessing
* **MLOps Platform:** MLflow for experiment tracking and model registry
* **Containerization:** Docker and Docker Compose
* **Orchestration:** APScheduler (Python) or lightweight Airflow
* **Monitoring:** Custom drift detection for text data (vocabulary and distribution analysis)
* **API:** FastAPI for model serving
* **Dashboard:** Streamlit for visualization
* **Storage:** SQLite for metadata, local file system for models

-----

## 🧠 Core MLOps Concepts

This project covers fundamental MLOps practices essential for production machine learning systems.

| Concept | Implementation | Technical Details |
| :--- | :--- | :--- |
| **Model Training & Versioning** | Automated training pipeline with experiment tracking | Train multiple model variants (Naive Bayes, Logistic Regression, SVM) with different hyperparameters. Log all experiments to MLflow with metrics (accuracy, precision, recall, F1), parameters, and artifacts for reproducibility. |
| **Model Registry** | Centralized model management | Use MLflow Model Registry to version models, track lineage, and manage model stages (Staging, Production, Archived). Enable easy rollback and A/B testing. |
| **Containerization** | Docker-based deployment | Package models, dependencies, and serving code in Docker containers for consistent deployment across environments. Use multi-stage builds for optimization. |
| **Monitoring & Drift Detection** | Statistical drift detection | Calculate vocabulary drift and TF-IDF distribution shifts to detect when incoming data patterns change. Monitor model performance metrics in production. Set thresholds for automated alerting. |
| **Automated Retraining** | Threshold-based retraining triggers | Implement rule-based system that triggers retraining when: 1) Drift metrics exceed thresholds, 2) Model accuracy degrades below acceptable levels, 3) Scheduled intervals are reached. |
| **CI/CD for ML** | Automated testing and deployment | Implement automated testing for data validation, model performance, and API endpoints. Use orchestration tools to automate the full pipeline. |
| **API Serving** | Production-ready model serving | Deploy models via FastAPI with proper error handling, logging, and monitoring. Include health checks and metrics endpoints. |
| **Observability** | Dashboard and metrics tracking | Create Streamlit dashboard to visualize model performance, drift metrics, retraining history, and system health in real-time. |

-----

## 📋 Requirements (Functional and Non-Functional)

### Functional Requirements (FR)

| ID | Requirement | Specific Description | Complexity | Status |
| :--- | :--- | :--- | :--- | :--- |
| **FR01** | Model Training Script | Train a text classification model for spam detection using Naive Bayes/Logistic Regression with TF-IDF features and configurable hyperparameters. | ⭐ Basic | `PENDING` |
| **FR05** | Scheduled Retraining | Implement automated retraining using APScheduler or Airflow that triggers training on schedule (weekly/daily). | ⭐ Basic | `PENDING` |
| **FR06** | Text Drift Detection | Calculate vocabulary drift, TF-IDF distribution shifts, and new spam pattern emergence for drift monitoring. | ⭐⭐ Moderate | `PENDING` |
| **FR07** | Automated Retraining Logic | Implement rule-based system that triggers retraining when drift exceeds thresholds (>0.15) or accuracy drops below 93%. | ⭐⭐ Moderate | `PENDING` |
| **FR08** | Simple Dashboard | Create Streamlit UI showing current metrics, model versions, drift scores, spam examples, and retraining history. | ⭐ Basic | `PENDING` |
| **FR09** | Model Comparison | Compare current vs previous model performance to decide if new model should be deployed. | ⭐ Basic | `PENDING` |
| **FR10** | Alert System | Send notifications (email/Slack) when retraining is triggered or model performance degrades. | ⭐ Basic | `PENDING` | | ⭐⭐ Moderate | `PENDING` |
| **FR07** | Retraining Agent | Build LangChain agent that analyzes text drift metrics, spam pattern evolution, model performance, and decides when to trigger retraining automatically. | ⭐⭐⭐ Advanced | `PENDING` |
| **FR08** | Simple Dashboard | Create Streamlit UI showing current metrics, model versions, drift scores, spam examples, and retraining history. | ⭐ Basic | `PENDING` |
| **FR09** | Model Comparison | Compare current vs previous model performance to decide if new model should be deployed. | ⭐ Basic | `PENDING` |

### Non-Functional Requirements (NFR)

| ID | Requirement | Category | Metric |
| :--- | :--- | :--- | :--- |
| **NFR01** | Training Time | Performance | Model training must complete in less than **2 minutes** for the SMS spam dataset (5,574 messages). |
| **NFR02** | API Response Time | Performance | Spam prediction endpoint must respond in less than **100ms** for single SMS messages. |
| **NFR03** | Text Preprocessing Time | Performance | Text preprocessing and vectorization must complete in less than **50ms** per message. |
| **NFR05** | Model Registry Access | Performance | Retrieving models and vectorizers from MLflow must take less than **2 seconds**. |
| **NFR06** | Retraining Logic Reliability | Reliability | The automated retraining system must correctly trigger retraining in **90%+** of cases when thresholds are exceeded. |
| **NFR07** | Dashboard Load Time | Performance | Streamlit dashboard must load in less than **3 seconds**. |correct in **80%+** of test cases. |
| **NFR07** | Dashboard Load Time | Performance | Streamlit dashboard must load in less than **3 seconds**. |
| **NFR08** | Container Startup | Performance | Docker containers must be ready to serve predictions within **30 seconds** of startup. |
| **NFR09** | Model Accuracy | Quality | The spam detection model must achieve at least **95% accuracy** and **90% F1-score** on test data. |

-----

## 🚀 Implementation and Execution

### 1\. Prerequisites

Ensure you have the following installed:
* **Python 3.9+** with pip and virtual environment support
* **Docker** and **Docker Compose** for containerization
* **Git** for version control

```bash
# In your .env file (optional):
# MLflow configuration (defaults to local)
MLFLOW_TRACKING_URI="http://localhost:5000"

# Alert system configuration (optional)
SMTP_SERVER="smtp.gmail.com"
SMTP_PORT="587"
ALERT_EMAIL="your-email@example.com"
SLACK_WEBHOOK_URL="https://hooks.slack.com/services/..."
LOW_TRACKING_URI="http://localhost:5000"
```

### 2\. How to Build (Install)

Install all necessary dependencies, primarily using a `requirements.txt` file.

```bash
# 1. Clone the repository
git clone [REPOSITORY_URL]
cd MLOps-Fundamentals-Capstone-AutoRetrain-Pipeline

# 2. Create and activate the virtual environment
python -m venv .venv
# On Windows:
.\.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate

# 3. Install dependencies
# Includes: FastAPI, LangChain, MLflow, scikit-learn, pandas, evidently, streamlit, docker, etc.
pip install -r requirements.txt

# 4. Download sample dataset (if using provided script)
python scripts/download_data.py
```

### 3\. How to Run

#### Option A: Quick Start with Make Commands

```bash
# Start all services (MLflow, FastAPI, Streamlit)
make setup              # First-time setup
make train              # Train initial model
make serve              # Start prediction API
# For automated retraining
make schedule-training  # Start scheduled retraining
make monitor            # Start monitoring and auto-retraining service
make schedule-training  # Start scheduled retraining
make run-agent          # Activate retraining agent
```

#### Option B: Manual Startup

```bash
# 1. Start MLflow tracking server
mlflow server --host 0.0.0.0 --port 5000

# 2. Train initial model (in new terminal)
python src/train.py --experiment-name "initial_training"

# 3. Start FastAPI serving (in new terminal)
uvicorn src.serve:app --host 0.0.0.0 --port 8000 --reload

# 4. Start Streamlit dashboard (in new terminal)
# 5. Start monitoring service (in new terminal)
python src/monitor.py
# 5. Start retraining agent (in new terminal)
python src/agent.py
```

#### Option C: Docker Compose (Recommended for Production)

```bash
# Start all services with Docker Compose
docker-compose up --build

# Services will be available at:
# * MLflow UI: http://localhost:5000
# * FastAPI (Swagger): http://localhost:8000/docs
# * Streamlit Dashboard: http://localhost:8501
```

### 4\. How to Test

Test the complete MLOps pipeline with the following scenarios:

#### A. Test Model Training

```bash
# Train a model and log to MLflow
python src/train.py --experiment-name "test_run"

# Expected output:
# * Model saved to MLflow
# * Metrics logged (accuracy, precision, recall, F1)
# * Run ID displayed
```

#### B. Test Prediction API

```bash
# Single spam prediction
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"message": "Congratulations! You have won a $1000 gift card. Click here to claim now!"}'

# Expected result:
{
  "prediction": "spam",
  "confidence": 0.94,
  "model_version": "v1.2.3",
  "timestamp": "2025-12-09T10:30:00Z",
  "top_features": ["won", "claim", "click", "congratulations"]
}

# Test with legitimate message
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"message": "Hey, are we still meeting for lunch at 12pm?"}'

# Expected result:
{
  "prediction": "ham",
  "confidence": 0.98,
  "model_version": "v1.2.3",
  "timestamp": "2025-12-09T10:30:15Z"
}

# Health check
curl http://localhost:8000/health
```

#### C. Test Drift Detection

```bash
# Calculate drift on new message batch
curl -X POST "http://localhost:8000/drift/calculate" \
  -H "Content-Type: application/json" \
  -d @test_data/new_messages.json

# Expected result:
{
  "vocabulary_drift": 0.23,
  "tfidf_drift": 0.18,
  "drift_detected": true,
  "threshold": 0.15,
  "new_spam_patterns": ["crypto", "nft", "metaverse"],
  "recommendation": "Consider retraining - new spam vocabulary detected"
}
#### D. Test Automated Retraining Logic

```bash
# Trigger retraining analysis
python src/monitor.py --check-now

# Monitor will output:
# * Current drift metrics
# * Model performance trends
# * Decision: RETRAIN / NO_ACTION / ALERT
# * Threshold comparisons (drift: 0.23 > 0.15 ✓ trigger)
``` Decision: RETRAIN / NO_ACTION / ALERT
# * Reasoning from LLM
```

#### E. End-to-End Integration Test

```bash
# Run full pipeline test
python tests/test_integration.py

# This will:
# 1. Train initial model
# 2. Deploy to API
# 3. Send predictions
# 4. Inject drift in data
# 5. Verify agent triggers retraining
# 6. Validate new model deployment
```

#### F. Test Using Swagger UI

1. Open `http://localhost:8000/docs`
2. Try the following endpoints:
   * `POST /predict` - Make predictions
   * `GET /models/current` - Get current model info
   * `GET /metrics/performance` - View performance metrics
   * `POST /drift/calculate` - Calculate drift
3. Check MLflow UI at `http://localhost:5000` for logged experiments

-----

## 🖼️ Project Views

Here will be the relevant screenshots of the project.

### 1\. MLflow Experiment Tracking

![Placeholder for screenshot of MLflow UI showing multiple experiment runs with metrics comparison (accuracy, precision, recall) and model versions.]

### 2\. Streamlit Dashboard

![Placeholder for screenshot of Streamlit dashboard showing:

* Current model performance metrics
* Drift score chart over time
* Retraining history timeline
* Agent decision logs
* Model version comparison table]

### 3\. FastAPI Swagger UI

![Placeholder for screenshot of FastAPI Swagger interface showing available endpoints:

* /predict (POST)
* /health (GET)
* /metrics/performance (GET)
* /drift/calculate (POST)
* /models/current (GET)]

### 4\. Docker Compose Architecture

![Placeholder for screenshot or diagram showing Docker Compose services:

* mlflow-server container
* fastapi-serving container
* streamlit-dashboard container
* agent-scheduler container
* Database volumes and networks]
### 5\. Automated Retraining Flow

![Placeholder for flow diagram showing:

1. Monitor checks drift metrics periodically
2. Queries MLflow for model performance
3. Evaluates thresholds (drift > 0.15 OR accuracy < 0.93)
4. If thresholds exceeded, triggers retraining pipeline
5. New model trained and logged to MLflow
6. System compares old vs new model performance
7. If improved (accuracy gain > 1%), deploys new model
8. Updates dashboard and sends alert notifications]

### 6\. Monitoring Service Output

![Placeholder for screenshot of monitoring console output showing:

* Drift analysis results (vocabulary: 0.23, TF-IDF: 0.18)
* Threshold comparison (0.23 > 0.15 ✓ TRIGGER)
* Current model accuracy: 94.2%
* Retraining decision: TRIGGERED
* Training pipeline status
* New model deployment confirmation]nfirmation
* New model deployment status]

-----

## 📦 Project Deliverables

### MVP (Week 2)

1. ✅ Working training script with MLflow tracking
2. ✅ Dockerized FastAPI prediction service
### Full Implementation (Week 4)

1. ✅ Automated retraining pipeline with scheduler
2. ✅ Rule-based monitoring service for automated retraining triggers
3. ✅ Enhanced monitoring dashboard with historical trends
4. ✅ Alert system for retraining events (email/Slack)
5. ✅ Complete documentation with architecture diagrams
6. ✅ Docker Compose setup for easy deployment
7. ✅ Integration tests for end-to-end pipeline
8. ✅ Demo video (5-10 minutes) showing full workflowms
5. ✅ Docker Compose setup for easy deployment
6. ✅ Integration tests for end-to-end pipeline
7. ✅ Demo video (5-10 minutes) showing full workflow

-----

## 🎓 Learning Outcomes

Upon completing this project, engineers will be able to:

1. ✅ **Build MLOps Pipelines:** Design and implement end-to-end ML pipelines with training, versioning, and deployment
6. ✅ **Automate Workflows:** Use schedulers (APScheduler/Airflow) for automated retraining
7. ✅ **Implement Monitoring:** Build threshold-based monitoring systems that detect drift and performance degradation
8. ✅ **Create Dashboards:** Build monitoring interfaces with Streamlit for visualization
9. ✅ **Set Up Alerts:** Configure notification systems for critical events
10. ✅ **Apply Best Practices:** Implement version control, logging, error handling, and documentation
6. ✅ **Automate Workflows:** Use schedulers (APScheduler/Airflow) for automated retraining
7. ✅ **Build Agentic Systems:** Create LangChain agents that make intelligent decisions about model retraining
8. ✅ **Create Dashboards:** Build monitoring interfaces with Streamlit for visualization
9. ✅ **Apply Best Practices:** Implement version control, logging, error handling, and documentation

-----

## 🚀 Quick Start Commands Summary

```bash
# Setup
make setup              # Install dependencies and setup environment
make train              # Train initial model

# Run services
make serve              # Start FastAPI prediction API
make dashboard          # Launch Streamlit monitoring dashboard
# Automation
make schedule-training  # Start scheduled retraining
make monitor            # Start automated monitoring and retraining service
make run-agent          # Activate intelligent retraining agent

# Docker
make docker-build       # Build all Docker images
make docker-up          # Start all services with Docker Compose
make docker-down        # Stop all services

# Testing
make test               # Run all tests
make test-integration   # Run end-to-end integration tests
```

-----

## 📊 Project Success Metrics

| Metric | Target | Category |
|:-------|:-------|:---------|
| Training Time | < 2 minutes | Performance |
| API Response Time | p95 < 100ms | Performance |
| Text Preprocessing Time | < 50ms | Performance |
| Drift Detection Accuracy | > 85% | Reliability |
| Model Registry Access Time | < 2 seconds | Performance |
| Retraining Trigger Reliability | > 90% | Reliability |
| Dashboard Load Time | < 3 seconds | Performance |
| Container Startup Time | < 30 seconds | Performance |
| Alert Delivery Time | < 60 seconds | Performance |
| Model Accuracy | > 95% | Quality |
| Model F1-Score | > 90% | Quality |

-----

## 🔧 Dataset: SMS Spam Collection

This project uses the **UCI SMS Spam Collection Dataset** for training the spam detection model.

### Dataset Details

* **Source**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection)
* **Size**: 5,574 SMS messages
* **Distribution**:
  * Ham (legitimate): 4,827 messages (86.6%)
  * Spam: 747 messages (13.4%)
* **Format**: Tab-separated text file (label, message)
* **Language**: English
* **Task**: Binary text classification

### Dataset Characteristics

* **Real-world data**: Actual SMS messages from various sources
* **Class imbalance**: Realistic spam/ham ratio
* **Text variety**: Short messages with slang, abbreviations, URLs
* **Drift simulation potential**: Easy to inject new spam patterns (crypto scams, phishing, etc.)
* **Training speed**: Very fast (<2 minutes for full pipeline)

### Sample Messages

```text
ham: "Hey, are you free for dinner tonight?"
spam: "URGENT! You have won a $5000 prize. Call now to claim!"
ham: "Can you pick up milk on your way home?"
spam: "FREE entry in 2 a weekly comp to win FA Cup final tickets."
```

### Download Instructions

```bash
# Option 1: Direct download
wget https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip
unzip smsspamcollection.zip -d data/

# Option 2: Using provided script
python scripts/download_data.py
```
