################
# Utilities

################
# Environment variables

################
# Exported variables

################
# Standard targets

.PHONY: api/run
api/run: api/.env api/.depend.secondary api/.migrate.secondary api/.static.secondary
	$(load-env) && \
	source api/venv/bin/activate && \
	api/venv/bin/uwsgi --ini api/uwsgi.ini

.PHONY: api/depend
api/depend: api/.depend.secondary

.PHONY: api/check
api/check:

.PHONY: api/clean
api/clean:

################
# Application specific targets

.PHONY: api/migrate
api/migrate: api/.migrate.secondary

################
# Source transformations

api/venv:
	python3 -m virtualenv $@

.SECONDARY: api/.depend.secondary
api/.depend.secondary: api/.env api/requirements.txt | api/venv
	$(load-env) && \
	source api/venv/bin/activate && \
	python -m pip install -r $(word 2,$^) && \
	touch $@

.SECONDARY: api/.migrate.secondary
api/.migrate.secondary: api/.env api/.depend.secondary \
                        $(wildcard api/api/*/models.py) api/api/settings.py
	$(load-env) && \
	source api/venv/bin/activate && \
	python api/manage.py makemigrations --no-input && \
	python api/manage.py migrate --no-input && \
	touch $@

.SECONDARY: api/.static.secondary
api/.static.secondary: api/.env api/.depend.secondary \
                       $(wildcard api/api/*/static/**/*) api/api/settings.py
	$(load-env) && \
	source api/venv/bin/activate && \
	python api/manage.py collectstatic --no-input && \
	touch $@

api/.env: api/.env.template .env
	$(make-env)
