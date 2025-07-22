from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and encoders
model = pickle.load(open('heart_failure_model.pkl', 'rb'))

try:
    encoders = pickle.load(open('encoders.pkl', 'rb'))
except:
    encoders = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = []
        def yesno(val):
            return 1 if val == 'yes' else 0
        # Get data from form and convert to numeric
        input_data.append(float(request.form['age']))
        input_data.append(int(request.form['anaemia']))
        input_data.append(float(request.form['creatinine_phosphokinase']))
        input_data.append(int(request.form['diabetes']))
        input_data.append(float(request.form['ejection_fraction']))
        input_data.append(int(request.form['high_blood_pressure']))
        input_data.append(float(request.form['platelets']))
        input_data.append(float(request.form['serum_creatinine']))
        input_data.append(float(request.form['serum_sodium']))
        input_data.append(int(request.form['sex']))
        input_data.append(int(request.form['smoking']))
        input_data.append(int(request.form['time']))

        # Predict
        pred = model.predict([np.array(input_data)])[0]
        result = "High Risk 😥" if pred == 1 else "Low Risk 😊"

        return render_template('index.html', prediction_text=f'Prediction: {result}')
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
