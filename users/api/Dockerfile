FROM python:3.10-bullseye
RUN python -m pip install --upgrade pip
WORKDIR /app

# Copy the top-level files
COPY requirements.txt requirements.txt
COPY manage.py manage.py

# Copy the Django project and all Django apps
COPY users_project users_project
COPY users_rest users_rest
COPY common common

RUN pip install -r requirements.txt
CMD python manage.py migrate && gunicorn users_project.wsgi --bind 0.0.0.0:$PORT --log-file -
