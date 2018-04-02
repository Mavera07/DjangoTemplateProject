docker build -f ./Dockerfile/Dockerfile-postgres -t djangotemplateproject_postgres_i ../../../djangotemplateproject

docker-compose -f ./docker-compose/docker-compose-run-postgres.yml up -d
