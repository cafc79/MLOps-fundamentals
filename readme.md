# MLOps Fundamentals: Part 1 - Foundations (Model Training & Versioning)

## 🎯 Project Overview

**Part 1: Foundations** is the first module in a 3-part iterative MLOps capstone project series. This module focuses on building the **core ML pipeline**: training models, versioning them with MLflow, and deploying them as a simple API.

### What You'll Build
- ✅ Text classification model for SMS spam detection
- ✅ MLflow experiment tracking and model registry
- ✅ Docker containerization for reproducible deployments
- ✅ FastAPI serving endpoint for predictions

### Timeline
- **Duration:** 2 weeks part-time
- **Complexity:** ⭐ Beginner/Intermediate
- **Next Step:** Part 2 (Monitoring & Automated Retraining)

---

## 🧠 Core Concepts Covered

| Concept | What You'll Learn |
|---------|------------------|
| **Model Training** | Build scikit-learn models (Naive Bayes, Logistic Regression, SVM) with hyperparameter tuning |
| **Experiment Tracking** | Use MLflow to log metrics, parameters, and artifacts for reproducible science |
| **Model Versioning** | Manage model versions in MLflow registry with staging control |
| **Text Feature Engineering** | TF-IDF vectorization and text preprocessing with NLTK |
| **Containerization** | Package code and dependencies in Docker for consistent environments |
| **API Serving** | Create FastAPI endpoints for model inference |
| **Version Control** | Git best practices for ML projects |

---

## 📋 Functional Requirements

| ID | Requirement | Description |
|----|-------------|-------------|
| **FR01** | Model Training Script | Train spam detection models using Naive Bayes, Logistic Regression, and SVM with TF-IDF features |
| **FR02** | Hyperparameter Tuning | Grid search for optimal hyperparameters across 3+ model variants |
| **FR03** | MLflow Integration | Log all experiments with metrics (accuracy, precision, recall, F1), parameters, and model artifacts |
| **FR04** | Model Registry | Store and version models in MLflow registry with proper lineage tracking |
| **FR05** | Docker Containerization | Package training and serving code in Docker containers |
| **FR06** | FastAPI Prediction API | Create REST API endpoint for spam/ham predictions with confidence scores |
| **FR07** | Text Preprocessing | Implement NLTK-based text cleaning (lowercase, tokenization, stopword removal) |
| **FR08** | Model Persistence | Save trained models and vectorizers as artifacts |

---

## 🚀 Implementation & Execution

### Prerequisites
```bash
# Required installations
- Python 3.9+
- Docker & Docker Compose
- Git
```

### How to Build

```bash
# 1. Clone and setup repository
git clone https://github.com/YOUR_USERNAME/MLOps-Fundamentals-Capstone-Part1-Foundations
cd MLOps-Fundamentals-Capstone-Part1-Foundations

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .\.venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Download dataset
python scripts/download_data.py
```

### How to Run

#### Option A: Quick Start (Make Commands)
```bash
make setup              # First-time setup
make train              # Train initial model
make serve              # Start prediction API
```

#### Option B: Manual
```bash
# 1. Start MLflow tracking server
mlflow server --host 0.0.0.0 --port 5000

# 2. Train model (new terminal)
python src/train.py --experiment-name "initial_training"

# 3. Start FastAPI server (new terminal)
uvicorn src.serve:app --host 0.0.0.0 --port 8000 --reload
```

#### Option C: Docker
```bash
# Build and run
docker build -t spam-detector:v1 .
docker run -p 8000:8000 spam-detector:v1
```

---

## 🧪 How to Test

### A. Test Model Training
```bash
python src/train.py --experiment-name "test_run"

# Expected output:
# ✓ Model trained and saved
# ✓ Metrics logged to MLflow
# ✓ Run ID: abc123def456
```

### B. Test Prediction API
```bash
# Test spam message
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"message": "Congratulations! You have won a $1000 gift card. Click here to claim now!"}'

# Expected response:
{
  "prediction": "spam",
  "confidence": 0.94,
  "model_version": "v1.0.0",
  "timestamp": "2025-12-09T10:30:00Z",
  "top_features": ["won", "claim", "click"]
}

# Test legitimate message
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"message": "Hey, are we still meeting for lunch?"}'

# Expected response:
{
  "prediction": "ham",
  "confidence": 0.98,
  "model_version": "v1.0.0"
}

# Health check
curl http://localhost:8000/health
```

### C. Test via Swagger UI
1. Open `http://localhost:8000/docs`
2. Test the `/predict` endpoint
3. Check `http://localhost:5000` for MLflow UI

### D. Unit Tests
```bash
pytest tests/test_train.py -v
pytest tests/test_serve.py -v
```

---

## 📁 Project Structure

```
MLOps-Fundamentals-Capstone-Part1-Foundations/
├── README.md                          # This file
├── Makefile                           # Quick commands
├── requirements.txt                   # Python dependencies
├── Dockerfile                         # Container definition
├── .env.example                       # Environment variables
├── data/
│   └── smsspamcollection.csv         # Dataset (after download)
├── src/
│   ├── __init__.py
│   ├── train.py                      # Model training pipeline
│   ├── serve.py                      # FastAPI application
│   ├── preprocessing.py              # Text preprocessing utilities
│   ├── models.py                     # Model definitions
│   └── config.py                     # Configuration management
├── scripts/
│   └── download_data.py              # Dataset download script
├── tests/
│   ├── test_train.py                 # Training tests
│   ├── test_serve.py                 # API tests
│   ├── test_preprocessing.py         # Preprocessing tests
│   └── conftest.py                   # Pytest configuration
└── mlruns/                           # MLflow tracking (auto-created)
```

---

## 📊 Success Metrics (Part 1)

| Metric | Target | Status |
|--------|--------|--------|
| Training Time | < 2 minutes | `PENDING` |
| API Response Time | < 100ms | `PENDING` |
| Model Accuracy | > 95% | `PENDING` |
| Model F1-Score | > 90% | `PENDING` |
| Code Coverage | > 80% | `PENDING` |
| Docker Build Time | < 5 minutes | `PENDING` |

---

## 🎓 Learning Outcomes

After completing Part 1, you will:

1. ✅ **Understand ML Pipelines:** Build end-to-end training workflows
2. ✅ **Master MLflow:** Track experiments, log models, manage versions
3. ✅ **Implement APIs:** Serve ML models via REST endpoints
4. ✅ **Use Docker:** Containerize ML applications for deployment
5. ✅ **Write Tests:** Test ML code and API endpoints
6. ✅ **Apply Best Practices:** Logging, error handling, documentation

---

## 🔗 Progression Path

```
Part 1: Foundations (YOU ARE HERE)
   ↓
Part 2: Monitoring & Automation
   - Adds drift detection
   - Adds scheduled retraining
   - Adds monitoring dashboard
   ↓
Part 3: Advanced Intelligence
   - Adds LangChain agent
   - Adds alert systems
   - Adds full orchestration
```

---

## 📚 Key Technologies

```
Data Processing:  pandas, numpy, scikit-learn
NLP:              TfidfVectorizer, NLTK
ML Framework:     scikit-learn (Naive Bayes, Logistic Regression, SVM)
ML Ops:           MLflow
API:              FastAPI, uvicorn
Containerization: Docker
Testing:          pytest
Utilities:        python-dotenv, requests
```

---

## 🚀 Quick Start Commands

```bash
make setup              # Install dependencies
make train              # Train model
make serve              # Start API server
make test               # Run tests
make docker-build       # Build Docker image
make docker-run         # Run in Docker
make mlflow-ui          # Open MLflow UI
```

---

## 📋 Deliverables (Part 1)

- ✅ Working training script with model persistence
- ✅ MLflow experiment tracking and model registry
- ✅ FastAPI prediction service with documentation
- ✅ Docker containerization for reproducible deployment
- ✅ Comprehensive test suite (>80% coverage)
- ✅ Complete documentation (README, inline comments, examples)
- ✅ Demo: Training → Serving workflow

---

## 🤔 Troubleshooting

### MLflow Server Won't Start
```bash
# Clear old MLflow data
rm -rf mlruns/
mlflow server --host 0.0.0.0 --port 5000
```

### Docker Build Issues
```bash
# Clear cache and rebuild
docker system prune
docker build --no-cache -t spam-detector:v1 .
```

### Import Errors
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

---

## 📞 Support & Next Steps

Once Part 1 is complete:
- Review the MLflow model registry
- Test the API thoroughly with various messages
- Prepare for Part 2 by understanding drift detection concepts
- Consider optimizing model performance

**Ready for Part 2?** See `../MLOps-Fundamentals-Capstone-Part2-Monitoring/README.md`

---

## 📖 References

- [MLflow Documentation](https://mlflow.org/docs/latest/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [scikit-learn Models](https://scikit-learn.org/)
- [SMS Spam Dataset](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection)
- [Docker Best Practices for ML](https://docs.docker.com/)
