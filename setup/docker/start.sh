docker volume create --name DjangoTemplateProject_postgresql-volume
docker build -f ./Dockerfile-postgres -t DjangoTemplateProject_postgres_i ../../../DjangoTemplateProject

docker build -f ./Dockerfile-python -t DjangoTemplateProject_i ../../../DjangoTemplateProject

docker-compose up -d
