docker rm -f djangotemplateproject_django_c
docker rm -f djangotemplateproject_postgres_c

docker volume rm djangotemplateproject_postgresql-volume
docker volume rm djangotemplateproject_bower-volume
docker volume rm djangotemplateproject_migrations-volume
