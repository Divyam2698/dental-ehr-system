# Dental EHR System

This is a web-based Dental Electronic Health Records (EHR) system developed using Python, Flask, and SQLite. The system allows clinics to manage patient records, including personal details, medical history, and contact information. It is designed for educational purposes and can be extended for real-world use.

## Features
- **Add Patient**: Allows adding new patients to the system with their name, date of birth, contact details, and medical history.
- **View Patients**: Lists all the patients stored in the database.
- **Basic CRUD functionality**: Create, Read, Update, Delete patient records (features for update and delete can be added as enhancements).

## Technologies Used
- **Python**: Programming language used for developing the application.
- **Flask**: Web framework for Python.
- **SQLAlchemy**: ORM (Object Relational Mapping) tool for handling database operations.
- **SQLite**: Lightweight database used to store patient data.

## Installation

### Requirements
- Python 3.x or later
- Flask
- Flask-SQLAlchemy

### Steps to run the application

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/dental_ehr_system.git
    cd dental_ehr_system
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the application:
    ```bash
    python app.py
    ```

6. Open your browser and go to `http://127.0.0.1:5000/` to view the application.

## Directory Structure
