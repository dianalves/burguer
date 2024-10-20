FROM python:3.11.0-slim-buster

RUN pip install poetry

EXPOSE 5000

WORKDIR /opt/burger
COPY . .
RUN poetry install
RUN poetry update package
# RUN poetry run python -m seeds.seed

# RUN python seeds/seed.py

CMD ["poetry", "run", "python", "-m", "flask", "run", "app.py", "--host=0.0.0"]