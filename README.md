<!-- Source: https://www.youtube.com/watch?v=S--SD4QbGps -->
## Training
Building docker
```
docker build -t "text_clasisfication" .
```
Running docker
```
docker run -it --rm --name text_clasisfication -p 8888:8888  -v /home/atseng/storage/ml-deployment/docker-flask/ml-dev/data:/data text_clasisfication /bin/bash
```
Training with a jupyter notebook

```
jupyter notebook --ip 0.0.0.0 --port 8888 --allow-root
```

# local testing without docker
### terminal 1
```
# activate conda or venv first
python app.py
```
### terminal 2
```
curl -X POST -H "Content-Type: application/json" -d '{"text": "May the Force be with you."}' 0.0.0.0:5000/predict
```

# local testing with docker

### terminal 1
Build container and run image
```
cd app/api/
docker compose up --build
```
Optional storing and pulling image from docker hub
```
# Store image on docker hub
docker compose push
# test pull image from docker hub
docker run -p 5000:5000 someone_random_guy/mlapp
```

### terminal 2
```
curl -X POST -H "Content-Type: application/json" -d '{"text": "May the Force be with you."}' 0.0.0.0:5000/predict
```