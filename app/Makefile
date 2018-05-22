SHELL = /bin/bash
PATH := node_modules/.bin:$(PATH)

GP_HOST  ?= localhost
GP_STAGE ?= prod

.PHONY: init dev build deploy

init:
	npm install
	pipenv install --dev

dev:
	webpack-dev-server --inline --progress --config build/webpack.dev.conf.js

build:
	node build/build.js

# Lookup deploy parameters
define ssm
pipenv run \
aws ssm get-parameter \
  --name "/galpi/$(GP_STAGE)/$(1)" \
  --query 'Parameter.Value' \
  --output text
endef

deploy: BUCKET          := $(shell $(call ssm,bucket))
deploy: DISTRIBUTION_ID := $(shell $(call ssm,distribution_id))
deploy: build
	pipenv run aws s3 sync "dist" "s3://$(BUCKET)" \
        --exact-timestamps \
        --delete
	pipenv run aws cloudfront create-invalidation \
       --distribution-id "$(DISTRIBUTION_ID)" \
       --paths '/*'
