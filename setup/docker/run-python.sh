docker build -f ./run/Dockerfile-python -t djangotemplateproject_i ../../../djangotemplateproject

docker-compose -f ./run/docker-compose-run-python.yml up -d
