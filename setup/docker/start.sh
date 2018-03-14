docker volume create --name djangotemplateproject_postgresql-volume
docker build -f ./Dockerfile-postgres -t djangotemplateproject_postgres_i ../../../djangotemplateproject

docker build -f ./Dockerfile-python -t djangotemplateproject_i ../../../djangotemplateproject

docker-compose up -d
