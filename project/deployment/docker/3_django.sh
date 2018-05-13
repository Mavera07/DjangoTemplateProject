DIR=$PWD/`dirname $0`

docker build -f $DIR/run/Dockerfile-django -t djangotemplateproject_django_i $DIR/../../../../djangotemplateproject

docker-compose -f $DIR/run/docker-compose-run-django.yml up -d
