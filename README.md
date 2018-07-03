# WTTD-eventex

Repositório contendo a aplicação desenvolvida durante o cuso #WTTD.

[![Build Status](https://travis-ci.org/rvmoura96/wttd-eventex.svg?branch=master)](https://travis-ci.org/rvmoura96/wttd-eventex)
[![Code Health](https://landscape.io/github/rvmoura96/wttd-eventex/master/landscape.svg?style=flat)](https://landscape.io/github/rvmoura96/wttd-eventex/master)


## Como desenvolver?
* Clone o repositório.
* Crie um virtualenv com Python 3.6.5
* Ative o virtualenv.
* Instale as dependências.
* Configure a instância com o .env
* Execute os testes.
```console
git clone https://github.com/rvmoura96/wttd-eventex wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test

```

## Como fazer o deploy?
* Crie uma instência no heroku.
* Envie as configurações para o heroku.
* Defina uma SECRET_KEY segura para a instância.
* Defina DEBUG=False
* Configure o serviço de email.
* Envie o código para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY= `python contrib/secret_gen.py`
heroku config:set DEBUG=False
#configuro o email
git push heroku master
