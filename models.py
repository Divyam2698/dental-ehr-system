from app import db

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.String(20), nullable=False)
    contact = db.Column(db.String(50), nullable=False)
    medical_history = db.Column(db.Text)
