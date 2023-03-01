# django_bem_simples
Projeto bem simples com python

Como rodar este projeto?
Primeiro clone esse repositório;
Depois crie um virtualenv com Python 3;
Ative o virtualenv;
Instale as dependências e
Rode as migrações.

git clone https://github.com/django_bem_simples.git
cd django_bem_simples
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate

Links
_______________________
djangoproject.com
Tutorial Django 2.2
