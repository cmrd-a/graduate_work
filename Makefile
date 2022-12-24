black:
	black . --line-length 120

prod_up:
	docker compose -f docker-compose-databases.yml -f docker-compose-services.yml up -d --build

prod_down:
	docker compose -f docker-compose-databases.yml -f docker-compose-elk.yml -f docker-compose-services.yml down

tests_up:
	docker compose -f tests/functional/docker-compose.yml up

tests_down:
	docker compose -f tests/functional/docker-compose.yml down

analytics_up:
	docker compose -f docker-compose-analytics.yml up -d

analytics_down:
	docker compose -f docker-compose-analytics.yml down

auth_debug:
	flask --app auth/src/Auth.app --debug run


dev_up:
	docker compose -f docker-compose-services.yml -f docker-compose-databases.yml -f docker-compose-dev.yml up loyalty pg_loyalty -d

dev_down:
	docker compose -f docker-compose-services.yml -f docker-compose-databases.yml -f docker-compose-dev.yml down