dockerfile-example/  
├── app.py              # Python-застосунок (підключення до PostgreSQL)  
├── requirements.txt    # Залежності (psycopg2-binary)  
├── Dockerfile          # Інструкції збірки образу  
└── .dockerignore       # Файли, що ігноруються при збірці  

Образ my-python-app:latest — 125 МБ (на базі python:3.13-slim).

Для запуску потрібен PostgreSQL. Наприклад:

# Запустити PostgreSQL
docker run -d --name postgres-dev \
-e POSTGRES_USER=postgres \
-e POSTGRES_PASSWORD=secret \
-e POSTGRES_DB=mydb \
-p 5432:5432 \
postgres:17

# Запустити застосунок
docker run --rm --network host \
-e DB_HOST=localhost \
-e DB_PASSWORD=secret \
my-python-app

## помилки

### The container name "/postgres-dev" is already in use by container
  ❯ docker run -d --name postgres-dev \
  ∙ -e POSTGRES_USER=postgres \
  ∙ -e POSTGRES_PASSWORD=secret \
  ∙ -e POSTGRES_DB=mydb \
  ∙ -p 5432:5432 \
  ∙ postgres:17
  docker: Error response from daemon: Conflict. The container name "/postgres-dev" is already in use by container "10a8953e865fc2a183021bf5eda7f97db5ec3acdfd6213b1e38f49384b4b7530". You have to
  remove (or rename) that container to be able to reuse that name. коли зроблений як правильно стартанути?

Контейнер postgres-dev вже існує з минулого разу. Перед запуском нового видаліть  
docker rm -f postgres-dev
