command = "venv/bin/gunicorn"
pythonpath = "venv"
bind = "127.0.0.1:8000"
workers = 2
raw_env = ["VARIABLE_HERE=VARIABLE_VALUE_HERE"]
wsgi_app = "project.wsgi"
