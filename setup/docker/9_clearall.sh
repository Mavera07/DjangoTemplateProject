docker rm -f $(docker ps -aq)
docker network prune -f
docker volume prune -f

DIR=$PWD/`dirname $0`
rm -rf $DIR/../../volumes/migrations
rm -rf $DIR/../../volumes/bower_components