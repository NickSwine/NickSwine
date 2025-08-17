@echo off

echo === Activating virtual environment ===
call .venv\Scripts\activate.bat

echo === Installing dependencies ===
pip install --upgrade pip
pip install -r requirements.txt

echo === Starting Flask app ===
python app.py

echo === Deactivating virtual environment ===
deactivate