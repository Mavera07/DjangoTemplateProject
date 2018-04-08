DIR=$PWD/`dirname $0`

docker volume create --name djangotemplateproject_postgresql-volume
docker volume create --name djangotemplateproject_migrations-volume
docker volume create --name djangotemplateproject_bower-volume


docker build -f $DIR/init/Dockerfile-init-postgres -t djangotemplateproject_init_postgres_i $DIR/../../../djangotemplateproject
docker build -f $DIR/init/Dockerfile-init-django -t djangotemplateproject_init_django_i $DIR/../../../djangotemplateproject
docker build -f $DIR/init/Dockerfile-init-bower -t djangotemplateproject_init_bower_i $DIR/../../../djangotemplateproject


docker-compose -f $DIR/init/docker-compose-init-postgres.yml up -d
sleep 5s
docker-compose -f $DIR/init/docker-compose-init-django.yml up -d
sleep 5s
docker-compose -f $DIR/init/docker-compose-init-bower.yml up -d


docker rm -f djangotemplateproject_bower_c
docker rm -f djangotemplateproject_django_c
docker rm -f djangotemplateproject_postgres_c

docker network rm init_default