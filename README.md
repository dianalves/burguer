## Instruções para rodar o projeto

## Instalar o Python
Python: https://www.python.org/downloads/
## Instalar as dependências do Python
Django: https://www.djangoproject.com/start/
## Instalar as dependências do Projeto
pip install -r requirements.txt
## Copiar o .env_sample
Mude o nome deste novo arquivo para .env e altere as configurações de acordo com o seu ambiente
## Realizar a inserção dos Seeds
Somente na primeira vez, rodar o seguinte comando: python seeds/seed.py

Este comando irá criar os burgers no banco de dados
## Iniciar o projeto
python app.py runserver