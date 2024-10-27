FROM python:3.11.0-slim-buster

RUN pip install poetry

EXPOSE 5000

WORKDIR /opt/burger
COPY . .
# RUN apt-get install openssh-client -y
RUN poetry config virtualenvs.create false --local
RUN poetry install
RUN poetry update package
# RUN poetry run python -m seeds.seed

# RUN python seeds/seed.py

CMD ["poetry", "run", "python", "-m", "flask", "run", "app.py", "--host=0.0.0"]
