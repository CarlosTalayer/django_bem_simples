#!/usr/bin/env python

"""
Gerador Django SECRET_KEY.
"""
from django.utils.crypto import get_random_string


chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

CONFIG_STRING = """
DEBUG=True
SECRET_KEY=%s
ALLOWED_HOSTS=127.0.0.1, .localhost
""".strip() % get_random_string(50, chars)

# Escrevendo nosso arquivo de configuração para '.env'
with open('.env', 'w') as configfile:
    configfile.write(CONFIG_STRING)
