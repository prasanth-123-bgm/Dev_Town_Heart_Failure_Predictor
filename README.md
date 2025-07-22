# 💓 Heart Failure Risk Prediction App

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-2.0%2B-lightgrey)](https://flask.palletsprojects.com/)

A modern, interactive web app to predict the risk of heart failure using machine learning. Built with Flask, styled with CSS animations, and ready for 1-click deployment on Render.

---

## 🚀 Features
- Predicts heart failure risk based on clinical parameters
- Animated, responsive UI with heart pulse and arrival effects
- Retains user input after prediction for easy re-tries
- Ready for cloud deployment (Render, Heroku, etc.)

---

## 🖥 Screenshots

> Add your screenshots here!

---

## 🛠 Setup (Local)

1. *Clone the repo:*
   bash
   git clone https://github.com/yourusername/heart-failure-predictor.git
   cd heart-failure-predictor
   
2. *Install dependencies:*
   bash
   pip install -r requirements.txt
   
3. *Add model files:*
   - Place heart_failure_model.pkl and encoders.pkl in the project root.
4. *Run the app:*
   bash
   python app.py
   
5. *Visit:*
   - Open [http://localhost:5010](http://localhost:5010) in your browser.

---

## 🌐 Deploy on Render

1. Click the button below to deploy instantly:
   
   [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

2. Set up the following:
   - *Build Command:* pip install -r requirements.txt
   - *Start Command:* gunicorn app:app
   - *Python Version:* 3.8+
   - Upload your model files (heart_failure_model.pkl, encoders.pkl) to the root directory.

---

## 📄 Project Structure

├── app.py
├── requirements.txt
├── heart_failure_model.pkl
├── encoders.pkl
├── static/
│   └── style.css
├── templates/
│   └── index.html


---

## 🤝 Credits
- UI/UX: Inspired by modern medical dashboards
- Model: Your trained ML model
- Built with [Flask](https://flask.palletsprojects.com/)

---

## 📬 Contact
For questions or feedback, open an issue or contact [your-email@example.com](mailto:your-email@example.com)
