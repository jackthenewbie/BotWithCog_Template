docker build . -f Dockerfile_update -t discord-bot:root
docker compose up -d --force-recreate --build