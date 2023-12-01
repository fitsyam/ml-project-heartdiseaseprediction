from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import joblib

app = Flask(__name__)

# Menggunakan joblib untuk memuat model
model = joblib.load('models/model1.pkl')

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/input")
def input():
    return render_template("input.html")

@app.route("/check_yourself")
def check_yourself():
    return redirect(url_for('input'))

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == "POST":
        # Dapatkan data input dari formulir
        age = float(request.form['age'])
        sex = int(request.form['sex'])
        chest_pain = float(request.form['chest_pain'])
        blood_pressure = float(request.form['blood_pressure'])
        cholesterol = float(request.form['cholesterol'])
        fbs_over_20 = int(request.form['fbs_over_20'])
        ekg_results = float(request.form['ekg_results'])
        max_hr = float(request.form['max_hr'])
        exercise_angina = int(request.form['exercise_angina'])
        st_depression = float(request.form['st_depression'])
        slope_of_st = float(request.form['slope_of_st'])
        num_vessel_fluro = float(request.form['num_vessel_fluro'])
        thallium = float(request.form['thallium'])

        # Lakukan prediksi menggunakan model yang dimuat
        input_data = np.array([[age, sex, chest_pain, blood_pressure, cholesterol, fbs_over_20, ekg_results, max_hr, exercise_angina, st_depression, slope_of_st, num_vessel_fluro, thallium]])
        prediction_result = model.predict(input_data)
        if prediction_result[0] == 0:
            prediction = "Anda tidak memiliki kemungkinan terkena penyakit jantung"
        else:
            prediction = "Anda memiliki kemungkinan terkena penyakit jantung"


        # Tampilkan hasilnya di halaman baru
        return render_template('result.html', prediction=prediction)

    return render_template("input.html")

@app.route('/result')
def result():
    # Logika untuk menampilkan result.html ada di sini
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
