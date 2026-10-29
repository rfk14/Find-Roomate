# 🏠 Roommate Matchmaker AI

An AI-powered roommate matching engine that combines strict hard-rule filtering with soft preference scoring and calibrated compatibility predictions.

---

## 🌟 Key Features

* **Interactive Web Application (`app.py`):** Multi-tab Streamlit interface featuring a top control toolbar, live candidate scoring, progress bars, head-to-head candidate comparisons, and raw data exploration.
* **Two-Tier Matching System:**
  * **Tier 1 (Hard Rules):** Eliminates incompatible candidates based on fundamental criteria (`Work Shift` and `Sleep Habit`).
  * **Tier 2 (Soft Scoring):** Ranks candidate compatibility based on weighted user preferences (`Cleanliness`, `Noise Level`, and `Pet Preferences`).
* **Calibrated Scoring Engine:** Linear regression model calibrated against ground-truth training pairs.
* **Interactive Notebook (`data_demo.ipynb`):** Step-by-step data processing, model training, and diagnostic validation plots (MAE = 8.43%, r = 0.814).

---

## 🚀 Quick Start & Installation

### 1. Requirements
Ensure you have Python installed, then install the dependencies:

```bash
pip install pandas numpy matplotlib streamlit --break-system-packages