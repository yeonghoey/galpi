SHELL = /bin/bash
HOST ?= localhost

.PHONY: init dev db server test deploy

init:
	npm install
	pipenv install --dev

dev:
	$(MAKE) --jobs 'db' 'server'

db:
	sls dynamodb start

server:
	pipenv run sls wsgi serve --host "$(HOST)"

test:
	pipenv run pytest

deploy:
	sls deploy --stage 'prod'
