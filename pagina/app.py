from flask import Flask, jsonify, request
import tensorflow as tf
from joblib import load
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from sklearn.metrics import auc
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load your model and scaler
model = tf.keras.models.load_model('./NUEVO2.h5')
scaler_X = load('./minmax_scaler_X.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract parameters from the request
    data = request.json
    volume_fraction = data['volumeFraction']
    radius = data['radius']
    film_thickness = data['filmThickness']
    wavelength_range = data['wavelengthRange']

    # Set up wavelength ranges and titles
    wavelength_ranges = {
        'uv': (300, 400, "Ultraviolet"),
        'visible': (400, 700, "Visible Light"),
        'ir': (700, 900, "Infrared")
    }

    start_wavelength, end_wavelength, range_title = wavelength_ranges.get(wavelength_range, (400, 700, "Visible Light"))

    longitud_de_onda = list(range(301, 901))
    df_data = {
        "Wavelength": longitud_de_onda,
        "Fracvol": [volume_fraction] * len(longitud_de_onda),
        "Radius (nm)": [radius] * len(longitud_de_onda),
        "Film Thickness (nm)": [film_thickness] * len(longitud_de_onda)
    }

    df = pd.DataFrame.from_dict(df_data)
    values = df.values
    normalized_values = scaler_X.transform(values)
    predictions = model.predict(normalized_values)
    df['Absorption Index'] = predictions.flatten()

    # Filter based on the selected wavelength range
    filtered_df = df[(df['Wavelength'] >= start_wavelength) & (df['Wavelength'] <= end_wavelength)]
    auc_value = auc(filtered_df['Wavelength'], filtered_df['Absorption Index'])

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(df['Wavelength'], df['Absorption Index'], color='blue')
    plt.xlabel('Wavelength')
    plt.ylabel('Absorption Index')
    plt.title(f'{range_title}, AUC: {auc_value:.5f}')
    plt.grid(True)

    # Save plot to a bytes buffer and encode to base64
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()

    return jsonify({'image': image_base64, 'auc': auc_value})

if __name__ == '__main__':
    app.run(debug=True)