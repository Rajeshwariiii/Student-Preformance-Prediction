from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    hours = float(request.form['hours'])
    prev_score = float(request.form['prev_score'])
    attendance = float(request.form['attendance'])

    motivation_score = hours * attendance

    # Derive study pattern
    if hours > 5:
        consistent, crammer = 0, 1
    elif hours >= 2:
        consistent, crammer = 1, 0
    else:
        consistent, crammer = 0, 0

    data = np.array([[hours, prev_score, attendance, motivation_score, consistent, crammer]])
    prediction = model.predict(data)[0]

    # Feedback
    if prediction >= 85:
        feedback = "Excellent! Keep up the great work."
    elif prediction >= 65:
        feedback = "Good job. Try to be more consistent to score higher."
    else:
        feedback = "Needs improvement. Consider increasing study hours and regularity."

    return render_template('result.html', score=round(prediction, 2), feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)
