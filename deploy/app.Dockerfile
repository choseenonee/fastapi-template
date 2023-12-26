FROM python:3.10


WORKDIR /usr/src/app


COPY ../requirements.txt ./requirements.txt
COPY ../ ./


RUN pip install --no-cache-dir -r requirements.txt


CMD ["python3", "main.py"]