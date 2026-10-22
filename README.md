# 🏠 Roommate Finder Agent

An AI-driven roommate matching system that uses interactive questionnaire preferences and hard-rule filtering to find optimal roommate candidates.

## 📁 Repository Contents

- **`data_demo.ipynb`**: Interactive Jupyter Notebook featuring the user questionnaire form and candidate filtering pipeline.
- **`profiles1.csv`**: Synthetic dataset containing 750 candidate roommate profiles across 15 behavioral and lifestyle attributes.
- **`Data_Card.md`**: Detailed documentation covering the dataset schema, attributes, and data scope.

## 🚀 How to Run the Demo

1. Open `data_demo.ipynb` in VS Code or Jupyter Notebook.
2. Run **Cell 1** to load the dataset (`profiles1.csv`).
3. Run **Cell 2** to display the interactive questionnaire and submit your preferences.
4. Run **Cell 3** to apply hard-rule filtering and view your matched candidate pool.

## 🛠️ Requirements

- Python 3.x
- `pandas`
- `ipywidgets`