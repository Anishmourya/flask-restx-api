# FLASK Restx API 

# Description 
Flask Restx api real world example that helps to create scalable rest api with swagger documentation in flask
https://github.com/python-restx/flask-restx
# Setup virtual env
``` 
$ python3 -m venv venv
$ . venv/bin/activate
```

# Docker build
``` 
$ docker build -t anishdhanka/flask_restx_api -f docker/Dockerfile .
```

# Docker run
``` 
$ docker run -d -p 5000:5000 --name flask_restx_api --restart=always -td anishdhanka/flask_restx_api
```

# Tests
``` 
$ export PYTHONPATH=$(pwd)
$ pytest  .
```


# Run
``` 
$ python3 run.py
```

# Endpoints
Swagger api docs
``` 
$ curl -i localhost:5000/v1/
```

# Cat namespace apis
``` 
$ curl -i localhost:5000/v1/cat/
$ curl -i localhost:5000/v1/cat/1
```

# Dog namespace apis
``` 
$ curl -i localhost:5000/v1/dog/
$ curl -i localhost:5000/v1/dog/1
```