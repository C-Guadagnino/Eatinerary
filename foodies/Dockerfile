FROM python:3.10-bullseye
RUN python -m pip install --upgrade pip
WORKDIR /app

# Copy the top-level files
COPY poll/requirements.txt requirements.txt
COPY poll/poller.py poller.py

# Copy the Django project and all Django apps
COPY api/foodies_project foodies_project
COPY api/foodies_rest foodies_rest
COPY api/common common

RUN pip install -r requirements.txt
CMD python poller.py
