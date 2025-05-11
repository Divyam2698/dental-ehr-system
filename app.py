from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dental_ehr.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.String(20), nullable=False)
    contact = db.Column(db.String(50), nullable=False)
    medical_history = db.Column(db.Text)

@app.route('/')
def index():
    patients = Patient.query.all()
    return render_template('index.html', patients=patients)

@app.route('/add', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
        contact = request.form['contact']
        medical_history = request.form['medical_history']

        patient = Patient(name=name, dob=dob, contact=contact, medical_history=medical_history)
        db.session.add(patient)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add_patient.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
