cd 04_task
python3 -m venv .venv

source .venv/bin/activate MacOS
.venv\Scripts\activate Для Windows

pip install colorama

pip freeze > requirements.txt
