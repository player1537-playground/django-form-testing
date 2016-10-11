MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := all
.DELETE_ON_ERROR:
.SUFFIXES:

################
# Utilities

# Used for backups
date := $(shell date +%Y%m%d%H%M%S)

# Used for debugging
.PHONY: echo.%
echo.%:
	@echo $*=$($*)

# Used to make specific .env files
make-env = ./scripts/env.bash subst < $< > $@

# Used to load specific .env files
load-env = set -o allexport && unset $$(./scripts/env.bash variables) && source $< && set +o allexport

################
# Environment variables

ifndef ENTR_BIN
ENTR_BIN := $(firstword $(shell which entr scripts/entr.bash 2>/dev/null))
endif

################
# Sanity checks and local variables

################
# Exported variables

export DATE := $(date)

################
# Includes

-include .env.makefile
include api/Makefile
include frontend/Makefile
include nginx/Makefile

################
# Standard targets

.PHONY: all
all: run

.PHONY: run
run:
	+$(MAKE) -j 3 \
		api/run \
		nginx/run \
		frontend/run

.PHONY: depend
depend: api/depend frontend/depend nginx/depend

.PHONY: check
check:
	./scripts/env.bash diff

.PHONY: clean
clean:
	find . -name '*~' -print -delete

################
# Application specific targets

.PHONY: print-url
print-url: .env
	@echo http://$(NGINX_HOST):$(NGINX_PORT)

################
# Source transformations

shared shared/static:
	mkdir -p $@

.env: .env.base
	touch $@
	cp $@ $@.$(date)
	./scripts/env.bash merge $@.$(date) $< > $@

.env.makefile: .env
	./scripts/env.bash to-makefile > $@
