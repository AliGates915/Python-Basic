from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
import pickle

# Create Flask app
app = Flask(__name__)

# --- Step 1: Prepare dataset ---
data = {
    'Area': ['Model Town', 'Model Town', 'Garden Town', 'Garden Town', 'Garden Town', 'Model Town', 'Garden Town', 'Garden Town', 'Garden Town', 'Garden Town', 'Model Town', 'Garden Town', 'Garden Town', 'Model Town'],
    'Dimensions': ['10 marla', '5 marla', '5 marla', '5 marla', '10 marla', '10 marla', '10 marla', '5 marla', '5 marla', '10 marla', '10 marla', '5 marla', '5 marla', '10 marla'],
    'Corner': ['No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No'],
    'Plot': ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No'],
    'Constructed': ['New', 'Used', 'Used', 'New', 'Used', 'New', 'Used', 'Used', 'New', 'Used', 'New', 'Used', 'New', 'New'],
    'Condition': ['New', 'Used', 'Used', 'New', 'Used', 'New', 'Used', 'Used', 'New', 'Used', 'New', 'Used', 'New', 'New'],
    'Prices': [136, 98, 91, 88, 116, 178, 122, 77, 56, 106, 109, 96, 91, 151]
}
df = pd.DataFrame(data)

# --- Step 2: Encode categorical features ---
le_area = LabelEncoder()
le_dimensions = LabelEncoder()
le_corner = LabelEncoder()
le_plot = LabelEncoder()
le_constructed = LabelEncoder()
le_condition = LabelEncoder()

df['Area'] = le_area.fit_transform(df['Area'])
df['Dimensions'] = le_dimensions.fit_transform(df['Dimensions'])
df['Corner'] = le_corner.fit_transform(df['Corner'])
df['Plot'] = le_plot.fit_transform(df['Plot'])
df['Constructed'] = le_constructed.fit_transform(df['Constructed'])
df['Condition'] = le_condition.fit_transform(df['Condition'])

# --- Step 3: Train model ---
X = df.drop('Prices', axis=1)
y = df['Prices']

model = LinearRegression()
model.fit(X, y)

# --- Step 4: Save model and encoders ---
pickle.dump(model, open('models/linear_regression_model.pkl', 'wb'))
pickle.dump(le_area, open('models/le_area.pkl', 'wb'))
pickle.dump(le_dimensions, open('models/le_dimensions.pkl', 'wb'))
pickle.dump(le_corner, open('models/le_corner.pkl', 'wb'))
pickle.dump(le_plot, open('models/le_plot.pkl', 'wb'))
pickle.dump(le_constructed, open('models/le_constructed.pkl', 'wb'))
pickle.dump(le_condition, open('models/le_condition.pkl', 'wb'))
