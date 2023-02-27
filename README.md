docker-compose down -v

docker-compose up -d --build

docker-compose exec app alembic revision --autogenerate

docker-compose exec app alembic upgrade head