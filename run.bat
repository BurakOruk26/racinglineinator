docker compose down -t 1
docker-compose build
docker image prune -f
docker compose up -d