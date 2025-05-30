up:
	docker compose -f docker-compose.dev.yml up

down:
	docker compose -f docker-compose.dev.yml down

build:
	docker compose -f docker-compose.dev.yml build

makemigrations:
	docker compose -f docker-compose.dev.yml exec -it app sh -c 'python src/manage.py makemigrations'

migrate:
	docker compose -f docker-compose.dev.yml exec -it app sh -c 'python src/manage.py migrate'