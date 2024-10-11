from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

# Mendapatkan path absolut dari direktori saat ini
current_dir = os.path.dirname(os.path.abspath(__file__))

# Memuat model, encoder, dan scaler menggunakan path absolut
model = joblib.load(os.path.join(current_dir, 'xgb_model_ujicoba.pkl'))
occupation_encoder = joblib.load(os.path.join(current_dir, 'Occupation_label_encoder.pkl'))
scaler = joblib.load(os.path.join(current_dir, 'minmax_scaler_split.1.pkl'))

# Fungsi untuk memprediksi sleep disorder
def predict_sleep_disorder(features):
    try:
        prediction = model.predict(features.reshape(1, -1))
        return prediction[0]
    except ValueError as e:
        return str(e)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            # Mendapatkan data dari form
            age = int(request.form['age'])
            occupation = request.form['occupation']
            sleep_duration = float(request.form['sleep_duration'])
            physical_activity_level = int(request.form['physical_activity_level'])
            stress_level = int(request.form['stress_level'])
            heart_rate = int(request.form['heart_rate'])
            daily_steps = int(request.form['daily_steps'])
            systolic = float(request.form['systolic'])
            diastolic = float(request.form['diastolic'])

            # Encode variabel kategori (occupation)
            occupation_num = occupation_encoder.transform([occupation])[0]

            # Daftar fitur numerik untuk scaling (9 elemen)
            numerical_features = [
                age, sleep_duration, physical_activity_level,
                stress_level, heart_rate, daily_steps, systolic, diastolic, occupation_num
            ]

            # Menyusun array fitur untuk scaling
            features_array = np.array(numerical_features).reshape(1, -1)

            # Melakukan scaling pada fitur numerik
            scaled_features = scaler.transform(features_array).flatten()

            # Melakukan prediksi
            prediction = predict_sleep_disorder(scaled_features)
            
            # Mapping hasil prediksi ke label
            if prediction == 0:
                prediction = 'Insomnia'
            elif prediction == 1:
                prediction = 'Normal'
            elif prediction == 2:
                prediction = 'Sleep Apnea'
            else:
                prediction = 'Tidak diketahui'

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
