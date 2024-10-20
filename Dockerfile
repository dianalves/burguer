FROM python:3.11.0-slim-buster

RUN pip install poetry

EXPOSE 5000

WORKDIR /opt/burger
COPY . .
RUN poetry install

# RUN python seeds/seed.py

CMD ["flask", "run", "app.py"]