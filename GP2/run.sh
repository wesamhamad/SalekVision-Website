docker stop gp-app
docker rm gp-app
docker build -t gp:latest .
docker run -d --name gp-app -p 5050:5050 gp