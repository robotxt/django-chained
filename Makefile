CONTAINER := web


.PHONY: lint
lint:
	docker-compose run --rm --no-deps $(CONTAINER) black .

.PHONY: shell
shell:
	docker-compose run --rm --no-deps $(CONTAINER) \
		python manage.py shell_plus


.PHONY: seed
seed:
	docker-compose run --rm --no-deps $(CONTAINER) \
		python manage.py seeder


.PHONY: unseed
unseed:
	docker-compose run --rm --no-deps $(CONTAINER) \
		python manage.py unseed