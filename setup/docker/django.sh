docker build -f ./run/Dockerfile-django -t djangotemplateproject_django_i ../../../djangotemplateproject

docker-compose -f ./run/docker-compose-run-django.yml up -d
