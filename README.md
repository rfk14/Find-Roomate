# Find Roommate — AI Matching Engine & Benchmark Evaluation

An intelligent, two-tier roommate matching system built in Python. The project uses a hybrid filtering and soft-scoring approach to evaluate candidate compatibility, calibrated against ground-truth pairwise preferences.

---

## 🛠️ System Architecture

The matching engine uses a **Two-Tier Pipeline**:

1. **Tier 1: Hard-Rule Filter Engine**
   - Filters candidate profiles based on strict lifestyle deal-breakers: **Work Shift** (`Night`, `Morning`, `Evening`) and **Sleep Type** (`Heavy Sleeper`, `Light Sleeper`).
   - Includes automatic fallback safety if no exact match is found.

2. **Tier 2: Soft Scoring Engine**
   - Evaluates retained candidates across weighted lifestyle preferences: **Cleanliness**, **Noise Tolerance**, and **Pet Compatibility**.
   - Computes a normalized similarity score ($0.0 - 100.0\%$) and outputs ranked top candidate recommendations with plain-language matching drivers.

---

## 📊 Datasets & Schema

- **`profiles1.csv`** (750 candidates, 15 attributes)
  - Primary candidate pool used for interactive matching and soft scoring.
  - Features key lifestyle attributes including work shift, sleep habits, cleanliness levels, and pet rules.

- **`training_data.csv`** (1,333 pairwise evaluation rows, 31 columns)
  - Pairwise student ratings used to benchmark and calibrate the core similarity logic.

---

## 📈 Benchmark Evaluation & Performance

The soft scoring model was validated against 1,333 ground-truth profile pairs using an 80/20 train/test split (`random_state=42`):

- **Train / Test Split:** 1,066 training pairs / 267 testing pairs
- **Linear Calibration Equation:** $\text{score} = 0.66 \times \text{raw} + 25.40$
- **Uncalibrated MAE:** $10.53$
- **Calibrated MAE:** $8.43$
- **Predict-the-Mean Baseline MAE:** $14.41$
- **Pearson Correlation ($r$):** $0.814$

*The calibrated model achieves a significant error reduction over the baseline, demonstrating strong linear correlation with human compatibility ratings.*

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/rfk14/Find-Roomate.git](https://github.com/rfk14/Find-Roomate.git)
   cd Find-Roomate