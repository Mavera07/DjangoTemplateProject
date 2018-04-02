docker volume create --name djangotemplateproject_postgresql-volume
docker volume create --name djangotemplateproject_migrations-volume
docker volume create --name djangotemplateproject_bower-volume

docker build -f ./Dockerfile/Dockerfile-init-postgres -t djangotemplateproject_init_postgres_i ../../../djangotemplateproject
docker build -f ./Dockerfile/Dockerfile-init-bower -t djangotemplateproject_init_bower_i ../../../djangotemplateproject
docker build -f ./Dockerfile/Dockerfile-init-django -t djangotemplateproject_init_django_i ../../../djangotemplateproject

docker-compose -f ./docker-compose/docker-compose-init.yml up -d

docker rm -f djangotemplateproject_init_bower_c
docker rm -f djangotemplateproject_init_django_c
docker rm -f djangotemplateproject_postgres_c