FROM python:3.10-bullseye
RUN python -m pip install --upgrade pip
WORKDIR /app

# Copy the top-level files
COPY requirements.txt requirements.txt
COPY manage.py manage.py

# Copy the Django project and all Django apps
COPY foodies_project foodies_project
COPY foodies_rest foodies_rest
COPY common common

RUN pip install -r requirements.txt
CMD python manage.py migrate && gunicorn foodies_project.wsgi --bind 0.0.0.0:$PORT --log-file -
