apt-get install openssh-client -y
git config --global --add safe.directory /worspaces/
poetry install
poetry update package
poetry run python -m seeds.seed
