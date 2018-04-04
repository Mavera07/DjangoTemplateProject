docker build -f ./run/Dockerfile-postgres -t djangotemplateproject_postgres_i ../../../djangotemplateproject

docker-compose -f ./run/docker-compose-run-postgres.yml up -d
