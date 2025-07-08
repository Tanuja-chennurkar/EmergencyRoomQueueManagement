from flask import Flask, render_template, request, redirect, url_for, flash
from hospital_queue import Patient, EmergencyRoom

app = Flask(__name__)
app.secret_key = "secret123"
er = EmergencyRoom()

@app.route("/")
def index():
    return render_template("index.html", patients=er.get_waiting_list())

@app.route("/add", methods=["POST"])
def add_patient():
    name = request.form["name"]
    age = request.form["age"]
    symptom = request.form["symptom"]
    severity = request.form["severity"]

    if not (name and age and symptom and severity):
        flash("All fields are required.", "error")
        return redirect(url_for("index"))

    try:
        age = int(age)
        severity = int(severity)
        if severity not in [1, 2, 3,4,5]:
            raise ValueError
    except ValueError:
        flash("Age and severity must be valid numbers. Severity must be 1, 2,3,4 or5.", "error")
        return redirect(url_for("index"))

    patient = Patient(name, age, symptom, severity)
    er.add_patient(patient)
    flash(f"Patient {name} added!", "success")
    return redirect(url_for("index"))

@app.route("/treat", methods=["POST"])
def treat_patient():
    patient = er.treat_patient()
    if patient:
        flash(f"Treated: {patient}", "info")
    else:
        flash("No patients in the queue.", "warning")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
