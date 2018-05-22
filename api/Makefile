SHELL = /bin/sh
HOST ?= localhost

.PHONY: init dev db server test

init:
	pipenv install --dev

dev:
	$(MAKE) --jobs 'db' 'server'

db:
	sls dynamodb start --seed

server:
	pipenv run sls wsgi serve --host "$(HOST)"

test:
	pipenv run pytest
