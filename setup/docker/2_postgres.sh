DIR=$PWD/`dirname $0`

docker build -f $DIR/run/Dockerfile-postgres -t djangotemplateproject_postgres_i $DIR/../../../djangotemplateproject

docker-compose -f $DIR/run/docker-compose-run-postgres.yml up -d

sleep 10s