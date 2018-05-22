SHELL = /bin/bash

HOST ?= localhost

.PHONY: init dev test deploy db db-stop

init:
	npm install
	pipenv install --dev

dev: db
	pipenv run sls wsgi serve --host "$(HOST)"

test: db
	pipenv run pytest

deploy:
	sls deploy --stage 'prod'

db: db.pid

db.pid:
	sls dynamodb start &> 'db.log' & echo "$$!" > 'db.pid'

db-stop: PID  = $(shell cat db.pid)
db-stop: PGID = $(shell ps -o pgid= $(PID))
db-stop:
	-kill -INT -$(PGID)
	-rm 'db.pid'
