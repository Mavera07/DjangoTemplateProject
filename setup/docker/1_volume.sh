DIR=$PWD/`dirname $0`

docker volume create --name djangotemplateproject_postgresql-volume
docker volume create --name djangotemplateproject_migrations-volume


docker build -f $DIR/init/Dockerfile-init-postgres -t djangotemplateproject_init_postgres_i $DIR/../../../djangotemplateproject
docker build -f $DIR/init/Dockerfile-init-django -t djangotemplateproject_init_django_i $DIR/../../../djangotemplateproject


docker-compose -f $DIR/init/docker-compose-init-postgres.yml up -d
echo "Wait for 10s"
sleep 10s
docker-compose -f $DIR/init/docker-compose-init-django.yml up -d
echo "Wait for 10s"
sleep 10s


docker rm -f djangotemplateproject_django_c
docker rm -f djangotemplateproject_postgres_c


docker network rm init_default


rm -rf $DIR/../../volumes/migrations
cp -r /var/lib/docker/volumes/djangotemplateproject_migrations-volume/_data $DIR/../../volumes/migrations
docker volume rm -f djangotemplateproject_migrations-volume