git clone https://github.com/KPfromSainP/best_social_media

cd best_social_media

ren .env.example .env

docker-compose up -d --build

docker-compose exec app alembic revision --autogenerate

docker-compose exec app alembic upgrade head
