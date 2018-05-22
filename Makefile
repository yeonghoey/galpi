SHELL = /bin/bash

.PHONY = init deploy

init deploy:
	$(MAKE) --directory='api' $@
	$(MAKE) --directory='app' $@
