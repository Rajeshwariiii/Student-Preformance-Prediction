#  Student Score Predictor

A web-based application that predicts student exam scores based on input factors such as hours studied, attendance, and previous scores. Built using Flask, this project leverages machine learning for educational performance forecasting.

---

##  Project Overview

This project helps visualize and predict a student's final exam score using various input features. It uses a trained regression model and offers a simple user interface for input and result viewing.

---

## 🛠️ Tech Stack

- Python
- Flask
- Pandas, NumPy
- Scikit-learn (for model training)
- HTML/CSS (via Flask templates)
- Excel/CSV dataset

---

##  Project Structure
```
Student-score-predictor/
│
├── static/ # Static assets (CSS, JS)
├── templates/ # HTML templates (UI)
├── app.py # Main Flask application
├── model.pkl # Trained ML model (pickle file)
├── model_train.py # Script for training the model
├── requirements.txt # Python dependencies
├── pccoe_CSE_DivA&B_google_form_dataset.xlsx # Input dataset
└── README.md # Project documentation
```

---

## ⚙️ Installation & Setup

### Step 1: Clone the repository
```bash
git clone https://github.com/your-username/student-score-predictor.git
cd student-score-predictor
```
### Step 2: Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

## 🔧 How to Use
▶ To train the model:
```bash
python model_train.py
```
▶ To run the Flask app:
```bash
python app.py
```
