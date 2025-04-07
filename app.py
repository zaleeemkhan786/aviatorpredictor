from flask import Flask, render_template
import requests  # API se data fetch karne ke liye

app = Flask(__name__)

@app.route('/')
def home():
    # Yahan actual API endpoint daalein
    response = requests.get('https://api.example.com/aviator-predictor')
    prediction = response.json().get('prediction', 'N/A')
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
