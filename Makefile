SHELL = /bin/bash

.PHONY = init deploy

init:
	$(MAKE) --directory='api' init
	$(MAKE) --directory='app' init

deploy:
	$(MAKE) --directory='api' deploy
	$(MAKE) --directory='app' deploy
