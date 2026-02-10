# MLOps Fundamentals: Part 2 - Monitoring & Automation (Drift Detection & Scheduled Retraining)

## 🎯 Project Overview

**Part 2: Monitoring & Automation** is the second module in the 3-part iterative MLOps capstone series. Building on Part 1's foundation, this module adds **intelligent monitoring and automated retraining**: detecting data drift, triggering retraining on schedule, and visualizing system health.

### What You'll Build (Beyond Part 1)
- ✅ Drift detection system for text data (vocabulary & TF-IDF distribution)
- ✅ Scheduled retraining using APScheduler
- ✅ Rule-based monitoring service for automated triggers
- ✅ Streamlit dashboard for visualization
- ✅ Performance comparison for model deployment decisions

### Prerequisites
- ✅ Completion of **Part 1: Foundations** (model training, API serving, MLflow)
- ✅ Understanding of: ML pipelines, MLflow, Docker, FastAPI

### Timeline
- **Duration:** 2 weeks part-time
- **Complexity:** ⭐⭐ Intermediate
- **Next Step:** Part 3 (Advanced Intelligence & Agents)

---

## 🧠 Core Concepts Covered

| Concept | What You'll Learn |
|---------|------------------|
| **Data Drift Detection** | Identify when new data differs from training data using statistical methods |
| **Scheduled Tasks** | Use APScheduler to automate retraining at regular intervals |
| **Performance Monitoring** | Track model accuracy, precision, recall over time |
| **Threshold-Based Logic** | Define rules for automatic retraining triggers |
| **Dashboard Design** | Build interactive Streamlit dashboards for observability |
| **Model Comparison** | Compare old vs new models before deployment |
| **Retraining Pipelines** | Automated end-to-end retraining workflows |
| **Logging & Observability** | Track system events and decisions in real-time |

---

## 📋 Functional Requirements

| ID | Requirement | Description |
|----|-------------|-------------|
| **FR06** | Text Drift Detection | Calculate vocabulary drift and TF-IDF distribution shifts |
| **FR07** | Drift Metrics | Compute drift scores with statistical thresholds (>0.15 triggers alert) |
| **FR08** | Scheduled Retraining | Implement daily/weekly automated training using APScheduler |
| **FR09** | Monitoring Service | Rule-based system checking: drift > 0.15 OR accuracy < 93% |
| **FR10** | Model Comparison | Compare new model vs production model on test set |
| **FR11** | Conditional Deployment | Deploy new model only if accuracy improves >1% |
| **FR12** | Dashboard Metrics | Display: current metrics, drift scores, retraining history, model versions |
| **FR13** | Alert Triggers** | Log retraining decisions with timestamps and reasoning |
| **FR14** | Historical Tracking | Store retraining history for analysis and auditing |

---

## 🚀 Implementation & Execution

### Prerequisites
```bash
# From Part 1 + new dependencies:
- Part 1 fully completed and tested
- APScheduler for task scheduling
- Streamlit for dashboards
- Evidently or custom drift detection
- sqlalchemy for metadata storage
```

### How to Build

```bash
# 1. Continue from Part 1 repository (or clone with Part 1 completed)
cd MLOps-Fundamentals-Capstone-Part1-Foundations

# 2. Update dependencies (add Part 2 packages)
pip install -r requirements.txt

# 3. Set up SQLite for retraining history
python scripts/setup_database.py

# 4. Verify Part 1 is working
python -c "import src.train; import src.serve; print('✓ Part 1 verified')"
```

### How to Run

#### Option A: Quick Start (Make Commands)
```bash
# From Part 1 setup:
make train              # Train baseline model
make serve              # Start API in terminal 1

# New commands for Part 2:
make monitor            # Start monitoring service (terminal 2)
make dashboard          # Start Streamlit dashboard (terminal 3)
```

#### Option B: Manual
```bash
# Terminal 1: MLflow and FastAPI (from Part 1)
mlflow server --host 0.0.0.0 --port 5000
# (separate terminal)
uvicorn src.serve:app --host 0.0.0.0 --port 8000 --reload

# Terminal 2: Monitoring service (NEW)
python src/monitor.py

# Terminal 3: Streamlit dashboard (NEW)
streamlit run src/dashboard.py --server.port 8501
```

#### Option C: Docker Compose (Recommended)
```bash
# Single command to start everything
docker-compose up --build

# Services available at:
# - MLflow UI: http://localhost:5000
# - FastAPI: http://localhost:8000
# - Streamlit: http://localhost:8501
```

---

## 🧪 How to Test

### A. Test Drift Detection
```bash
# Simulate new messages with drift (crypto scams, phishing)
python tests/test_drift.py

# Expected output:
# Vocabulary Drift: 0.23 (> 0.15 threshold) ✓ DRIFT DETECTED
# TF-IDF Drift: 0.18 (> 0.15 threshold) ✓ DRIFT DETECTED
# New patterns detected: ['crypto', 'nft', 'metaverse', 'blockchain']
# Recommendation: RETRAIN
```

### B. Test Scheduled Retraining
```bash
# Trigger retraining immediately (for testing)
python src/monitor.py --check-now

# Expected output:
# [2025-12-09 10:30:15] Monitoring cycle started
# [2025-12-09 10:30:16] Drift metrics: vocab=0.23, tfidf=0.18
# [2025-12-09 10:30:17] Current model accuracy: 94.2%
# [2025-12-09 10:30:18] Decision: RETRAIN (drift > 0.15)
# [2025-12-09 10:30:19] Training new model...
# [2025-12-09 10:30:45] New model accuracy: 95.1% (↑0.9%)
# [2025-12-09 10:30:46] Deployment decision: DEPLOY (accuracy improved)
# [2025-12-09 10:30:47] New model deployed as production version
```

### C. Test Monitoring Service API
```bash
# Get current drift metrics
curl http://localhost:8000/metrics/drift

# Expected response:
{
  "vocabulary_drift": 0.23,
  "tfidf_drift": 0.18,
  "drift_detected": true,
  "threshold": 0.15,
  "timestamp": "2025-12-09T10:30:00Z",
  "new_patterns": ["crypto", "nft"]
}

# Get model comparison
curl http://localhost:8000/models/comparison

# Expected response:
{
  "current_model": {
    "version": "v1.2.3",
    "accuracy": 0.942,
    "f1_score": 0.91
  },
  "previous_model": {
    "version": "v1.1.0",
    "accuracy": 0.937,
    "f1_score": 0.90
  },
  "improvement": 0.005
}

# Get retraining history
curl http://localhost:8000/retraining/history?limit=10
```

### D. Test Dashboard
```bash
# Open dashboard in browser
open http://localhost:8501

# Expected views:
# 1. Current metrics card (accuracy, F1, precision)
# 2. Drift score chart (time series)
# 3. Retraining history timeline
# 4. Model version comparison table
# 5. Performance trend chart
```

### E. Automated Testing
```bash
pytest tests/test_monitor.py -v
pytest tests/test_dashboard.py -v
pytest tests/test_drift.py -v
```

---

## 📁 Project Structure (Part 1 + Part 2)

```
MLOps-Fundamentals-Capstone-Part1-Foundations/
├── README.md                          # Part 1 README
├── Makefile                           # Includes Part 1 & 2 commands
├── requirements.txt                   # Part 1 + Part 2 dependencies
├── docker-compose.yml                 # Multi-container orchestration (NEW)
├── src/
│   ├── train.py                       # From Part 1
│   ├── serve.py                       # From Part 1 + new endpoints
│   ├── preprocessing.py               # From Part 1
│   ├── monitor.py                     # NEW: Monitoring & retraining logic
│   ├── drift_detection.py             # NEW: Drift calculation
│   ├── dashboard.py                   # NEW: Streamlit visualization
│   ├── model_comparison.py            # NEW: Model comparison logic
│   ├── database.py                    # NEW: SQLAlchemy models
│   └── config.py                      # Updated config
├── scripts/
│   ├── download_data.py               # From Part 1
│   ├── setup_database.py              # NEW: Initialize SQLite
│   └── inject_drift.py                # NEW: Simulate data drift
├── tests/
│   ├── test_train.py                  # From Part 1
│   ├── test_serve.py                  # From Part 1
│   ├── test_drift.py                  # NEW: Drift detection tests
│   ├── test_monitor.py                # NEW: Monitoring tests
│   ├── test_dashboard.py              # NEW: Dashboard tests
│   └── conftest.py                    # Updated pytest config
└── data/
    ├── smsspamcollection.csv          # Training dataset
    └── retraining_history.db          # NEW: SQLite database
```

---

## 📊 Success Metrics (Part 1 + Part 2)

| Metric | Target | Status |
|--------|--------|--------|
| Drift Detection Accuracy | > 85% | `PENDING` |
| Retraining Trigger Reliability | > 90% | `PENDING` |
| Dashboard Load Time | < 3 seconds | `PENDING` |
| Scheduled Trigger Precision | > 95% | `PENDING` |
| Model Comparison Accuracy | 100% | `PENDING` |
| Historical Data Retention | Complete audit trail | `PENDING` |

---

## 🎓 Learning Outcomes (Part 1 + Part 2)

After completing Part 2, you will:

1. ✅ **Detect Data Drift:** Implement statistical methods to identify when data changes
2. ✅ **Automate Retraining:** Schedule and execute automated model retraining
3. ✅ **Monitor Performance:** Track model metrics over time
4. ✅ **Build Dashboards:** Create interactive visualizations with Streamlit
5. ✅ **Make Deployment Decisions:** Compare models and deploy conditionally
6. ✅ **Implement Observability:** Log and track all system decisions

---

## 🔗 Progression Path

```
Part 1: Foundations ✓
   ↓
Part 2: Monitoring & Automation (YOU ARE HERE)
   ↓
Part 3: Advanced Intelligence
   - Adds LangChain agent for intelligent decisions
   - Adds email/Slack alerts
   - Adds A/B testing capabilities
```

---

## 📚 New Technologies (Part 2)

```
Scheduling:       APScheduler
Dashboards:       Streamlit
Drift Detection:  Evidently, custom statistical methods
Databases:        SQLAlchemy, SQLite
Time Series:      pandas, numpy
Visualization:    plotly, matplotlib
```

---

## 🚀 New Commands for Part 2

```bash
make monitor            # Start monitoring service
make dashboard          # Start Streamlit dashboard
make test-drift         # Test drift detection
make test-monitor       # Test monitoring logic
make setup-database     # Initialize SQLite database
make docker-compose-up  # Start all services
```

---

## 📋 Deliverables (Part 1 + Part 2)

From Part 1:
- ✅ Working training script with model persistence
- ✅ MLflow experiment tracking
- ✅ FastAPI prediction service
- ✅ Docker containerization

New in Part 2:
- ✅ Drift detection module with statistical analysis
- ✅ Scheduled retraining system using APScheduler
- ✅ Rule-based monitoring service
- ✅ Streamlit monitoring dashboard
- ✅ Model comparison logic
- ✅ Retraining history database
- ✅ Extended test suite (>80% coverage)

---

## 🔄 Integration with Part 1

This module **extends** Part 1, not replaces it. You need:
1. Part 1 trained model in MLflow ✓
2. Part 1 FastAPI serving endpoint ✓
3. Part 1 Docker setup ✓

Part 2 adds monitoring on top of these foundations.

---

## 🤔 Troubleshooting

### Drift Metrics Not Updating
```bash
# Ensure monitoring service is running
python src/monitor.py --check-now
# Check logs for errors
tail -f logs/monitor.log
```

### Dashboard Not Loading
```bash
# Reinstall Streamlit and dependencies
pip install --upgrade streamlit plotly
streamlit run src/dashboard.py --logger.level=debug
```

### Retraining Not Triggering
```bash
# Check APScheduler logs
grep "APScheduler" logs/monitor.log
# Verify thresholds in config
cat src/config.py | grep THRESHOLD
```

---

## 📞 Next Steps

After Part 2 is complete:
- Review drift detection accuracy
- Validate retraining decisions
- Check dashboard responsiveness
- Analyze retraining history

**Ready for Part 3?** See `../MLOps-Fundamentals-Capstone-Part3-Advanced/README.md`

---

## 📖 References

- [APScheduler Documentation](https://apscheduler.readthedocs.io/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Evidently AI - Drift Detection](https://docs.evidentlyai.com/)
- [MLflow Model Registry](https://mlflow.org/docs/latest/model-registry.html)
- [FastAPI Advanced Features](https://fastapi.tiangolo.com/advanced/)
