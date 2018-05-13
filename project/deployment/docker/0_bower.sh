DIR=$PWD/`dirname $0`


docker volume create --name djangotemplateproject_bower-volume


docker build -f $DIR/init/Dockerfile-init-bower -t djangotemplateproject_init_bower_i $DIR/../../../djangotemplateproject
docker-compose -f $DIR/init/docker-compose-init-bower.yml up -d


docker rm -f djangotemplateproject_bower_c
docker network rm init_default


rm -rf $DIR/../../volumes/bower_components
cp -r /var/lib/docker/volumes/djangotemplateproject_bower-volume/_data $DIR/../../volumes/bower_components
docker volume rm -f djangotemplateproject_bower-volume