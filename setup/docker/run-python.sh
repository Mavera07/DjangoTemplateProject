docker build -f ./Dockerfile/Dockerfile-python -t djangotemplateproject_i ../../../djangotemplateproject

docker-compose -f ./docker-compose/docker-compose-run-python.yml up -d
