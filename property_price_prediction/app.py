from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model
model = joblib.load('models/linear_regression_model.pkl')

# Load encoders
le_area = joblib.load('models/le_area.pkl')
le_dimensions = joblib.load('models/le_dimensions.pkl')
le_corner = joblib.load('models/le_corner.pkl')
le_plot = joblib.load('models/le_plot.pkl')
le_constructed = joblib.load('models/le_constructed.pkl')
le_condition = joblib.load('models/le_condition.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get form data
        area = request.form['area']
        dimensions = request.form['dimensions']
        corner = request.form['corner']
        plot = request.form['plot']
        constructed = request.form['constructed']
        condition = request.form['condition']

        # Encode data using respective encoders
        area = le_area.transform([area])[0]
        dimensions = le_dimensions.transform([dimensions])[0]
        corner = le_corner.transform([corner])[0]
        plot = le_plot.transform([plot])[0]
        constructed = le_constructed.transform([constructed])[0]
        condition = le_condition.transform([condition])[0]

        # Make feature array
        features = np.array([[area, dimensions, corner, plot, constructed, condition]])

        # Prediction
        pred = model.predict(features)[0]

        return render_template('result.html', prediction=pred)

if __name__ == '__main__':
    app.run(debug=True)
