

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "secret123")
er = EmergencyRoom()

@app.route("/")
def index():
    return render_template("index.html", 
                         patients=er.get_waiting_list(),
                         treated_count=len(er.get_treated_history()))

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
        if severity not in [1, 2, 3, 4, 5]:
            raise ValueError
    except ValueError:
        flash("Age and severity must be valid numbers. Severity must be 1, 2, 3, 4 or 5.", "error")
        return redirect(url_for("index"))

    patient = Patient(name, age, symptom, severity)
    er.add_patient(patient)
    flash(f"Patient {name} added to queue!", "success")
    return redirect(url_for("index"))

@app.route("/treat", methods=["POST"])
def treat_patient():
    patient = er.treat_patient()
    if patient:
        flash(f"Treated: {patient.name} - {patient.symptom}", "info")
    else:
        flash("No patients in the queue.", "warning")
    return redirect(url_for("index"))

@app.route("/export_csv")
def export_csv():
    treated_history = er.get_treated_history()
    
    if not treated_history:
        flash("No treated patients to export.", "warning")
        return redirect(url_for("index"))
    
    # Create CSV content
    output = StringIO()
    writer = csv.writer(output)
    
    # Write header
    writer.writerow(['Name', 'Age', 'Symptom', 'Severity', 'Arrival Time', 'Treatment Time'])
    
    # Write patient data
    for patient in treated_history:
        writer.writerow([
            patient.name,
            patient.age,
            patient.symptom,
            patient.severity,
            patient.arrival_time.strftime('%Y-%m-%d %H:%M:%S'),
            patient.treatment_time.strftime('%Y-%m-%d %H:%M:%S')
        ])
    
    # Create response
    response = make_response(output.getvalue())
    response.headers['Content-Type'] = 'text/csv'
    response.headers['Content-Disposition'] = f'attachment; filename=treated_patients_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
    
    return response

@app.route("/history")
def view_history():
    treated_history = er.get_treated_history()
    return render_template("history.html", treated_patients=treated_history)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
