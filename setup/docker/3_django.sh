DIR=$PWD/`dirname $0`

docker build -f $DIR/run/Dockerfile-django -t djangotemplateproject_django_i $DIR/../../../djangotemplateproject

docker rm -f djangotemplateproject_django_c
docker volume rm -f djangotemplateproject_development-volume || true
docker volume create --name djangotemplateproject_development-volume

docker-compose -f $DIR/run/docker-compose-run-django.yml up -d
