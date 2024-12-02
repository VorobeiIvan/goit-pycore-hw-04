python3 -m venv .venv

source .venv/bin/activate MacOS
.venv\Scripts\activate Для Windows

pip install colorama

cd 03_task
python main.py .

pip freeze > requirements.txt
