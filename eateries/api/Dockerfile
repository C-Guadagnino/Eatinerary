FROM python:3.10-bullseye
RUN python -m pip install --upgrade pip
WORKDIR /app

# Copy the top-level files
COPY requirements.txt requirements.txt
COPY manage.py manage.py

# Copy the Django project and all Django apps
COPY eateries_project eateries_project
COPY eateries_rest eateries_rest
COPY common common

RUN pip install -r requirements.txt
CMD python manage.py migrate && gunicorn eateries_project.wsgi --bind 0.0.0.0:$PORT --log-file -
