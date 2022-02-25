<div align="center">
  
<img height="100" width="110" style="margin-bottom: -55px" alt="FastAPI Template" src="https://gitlab.com/uploads/-/system/project/avatar/33491624/fastapi.png"> 

<br>    

#FastAPI &nbsp;TEMPLATE

</div>

<br>


**Source Code**: <a href="https://gitlab.com/juanesquintero/fastapi-template" target="_blank"> https://gitlab.com/juanesquintero/fastapi-template </a>

## About
This project is a template or scaffolding for FastAPI framework with Python 3.10, to easily start your project without wasting time on basic  big project implementations like:
  - Development Guidelines
  - Clean folder tree
  - FastAPI advanced config & features
  - Application CLI
  - Dockerization
  - SQL database connection
  - Unit Testing
  - Coverage report
  - Linting
  - Git hooks
  
## Local Environment
This template can be run it on your local machine or in a docker container,
so you can install just Docker or Pyenv and virtualenv.

  <b>Pyenv</b> <br>
  https://help.dreamhost.com/hc/en-us/articles/216137637 <br>
  https://realpython.com/intro-to-pyenv/
  https://github.com/pyenv/pyenv#installation
  
  <b>venv</b> <br>
  https://docs.python.org/es/3/library/venv.html

  <b>Docker</b> <br>
  https://www.docker.com/resources/what-container
   

<br>

## Requirements

<i>Python</i> 3.10.2
https://www.python.org/downloads/release/python-3102/

<i>MySQL</i> 8.0 
https://dev.mysql.com/doc/relnotes/mysql/8.0/en/

<i>FastAPI</i> 0.73.0
https://fastapi.tiangolo.com/

<i>Typer</i>
https://typer.tiangolo.com/

<i>SQLAlchemy</i> 1.4.31
https://www.sqlalchemy.org/

<br>


## SetUp

  Create <b><i>.env</i></b> file with the environment variables

    DB_HOST=localhost 
    DB_PORT=3305
    DB_SCHEMA=academy
    DB_USER=root
    DB_PASSWORD=admin

  ### Locally

  After install the local environment with pyenv use the certain python version and upgrade pip.
  
  ````console
  $ pyenv shell 3.10.2
  $ python -m pip install --upgrade pip
  ````

  Create a <b><i>virtual environment</i></b> with python virtualenv
  https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

  ````console
  $ python -m pip install virtualenv 
  $ python -m venv venv
  ````

  Activate the <b><i>virtual environment</i></b>

  ````console
  $ source venv/bin/activate
  (venv)$ which python
  ````
  
  ### Containerized

  After install Docker & docker-compose, create the images & instance the containers.
  
  ````console
  $ docker-compose up
  ````

The fastapi app now is running on http://localhost:8001 and the mysql database on localhost:3305

### Database
You can rather install MySQL engine locally or simply use the docker container created above.
Just remember to change the .env connection variables.
In the <i>app/db</i> folder you will find the needed DDL & DML scripts for the proper database setup.



---

<br>

## Folder Structure  
    📦fastapi-template
     ┣ 📂app
     ┃ ┣ 📂db
     ┃ ┣ 📂models
     ┃ ┣ 📂routers
     ┃ ┣ 📂schemas
     ┃ ┣ 📂shared
     ┃ ┣ 📜__init__.py
     ┃ ┗ 📜main.py
     ┣ 📂cli
     ┣ 📂tests
     ┣ 📜.dockerignore
     ┣ 📜.env
     ┣ 📜.gitignore
     ┣ 📜.pre-commit-config.yaml
     ┣ 📜.python-version
     ┣ 📜DEVGUIDE.md
     ┣ 📜Dockerfile
     ┣ 📜README.md
     ┣ 📜config.py
     ┣ 📜docker-compose.yml
     ┣ 📜requirements-dev.txt
     ┣ 📜requirements.txt
     ┗ 📜run.py

<br>

## Installation
<div class="termy">

```console
(venv)$ pip install requirements.txt

---> 100%
```

</div>

If you are in dev mode use:

<div class="termy">

```console
(venv)$ pip install requirements-dev.txt

---> 100%
```

</div>


### Run
  The <b><i>run.py</i></b> file has dev environment parameters to run the application.
  ```console
  python run.py
  ```
  

### Check it

Open your browser at <a href="http://127.0.0.1:8000/" class="external-link" target="_blank"> http://127.0.0.1:8000/ </a>

You will see the JSON response as:

```JSON
{"api": "FastAPI Template"}
```

<br>

## CLI
This template counts with a custom CLI to execute clear and simple commands instead long tedious native commands. 
https://typer.tiangolo.com/tutorial/package/

Setting up running the following command in the path cli/cli/
```console
  (venv)$ poetry install
 ```
  
  Show available commands
  ```console
  (venv)$ app-cli --help
  ```

  Run or start api server <small>(Dev mode by default)</small>
  ```console
  (venv)$ app-cli start

  (venv)$ app-cli start --env=prod
  
  (venv)$ app-cli start --help
  ```

To change the application CLI command just modify the following line on the  <b><i>cli/cli/pyproject.toml</i></b> file.
```TOML
[tool.poetry.scripts]
app-cli = "cli.main:app"
```

<br>

## Testing 

  Run tests 
  ```console
  pytest -v tests/
  ```
  Tests report 
  ```console  
  pytest --html=tests/report.html --self-contained-html
  ```
  Coverage Report
  ```console
  pytest --cov=app tests/
  ```
  Coverage HTML Report
  ```console
  pytest --cov=app tests/ --cov-report html:tests/.coverage
  ```

<br>

## API Docs

### Swagger - OpenAPI

Now go to <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank"> http://127.0.0.1:8000/docs </a>

You will see the automatic interactive API documentation (provided by <a href="https://github.com/swagger-api/swagger-ui" class="external-link" target="_blank">Swagger UI</a>):

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)

### ReDoc

And now, go to <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc </a>

You will see the alternative automatic documentation (provided by <a href="https://github.com/Rebilly/ReDoc" class="external-link" target="_blank">ReDoc</a>):

![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)


<br> 

## Optional Dependencies


* <a href="https://github.com/esnme/ultrajson" target="_blank"><code>ujson</code></a> - for faster JSON <abbr title="converting the string that comes from an HTTP request into Python data">"parsing"</abbr>.
* <a href="https://github.com/JoshData/python-email-validator" target="_blank"><code>email_validator</code></a> - for email validation.


* <a href="https://requests.readthedocs.io" target="_blank"><code>requests</code></a> - Required if you want to use the `TestClient`.
* <a href="https://jinja.palletsprojects.com" target="_blank"><code>jinja2</code></a> - Required if you want to use the default template configuration.
* <a href="https://andrew-d.github.io/python-multipart/" target="_blank"><code>python-multipart</code></a> - Required if you want to support form <abbr title="converting the string that comes from an HTTP request into Python data">"parsing"</abbr>, with `request.form()`.
* <a href="https://pythonhosted.org/itsdangerous/" target="_blank"><code>itsdangerous</code></a> - Required for `SessionMiddleware` support.
* <a href="https://pyyaml.org/wiki/PyYAMLDocumentation" target="_blank"><code>pyyaml</code></a> - Required for Starlette's `SchemaGenerator` support (you probably don't need it with FastAPI).
* <a href="https://github.com/esnme/ultrajson" target="_blank"><code>ujson</code></a> - Required if you want to use `UJSONResponse`.


* <a href="https://www.uvicorn.org" target="_blank"><code>uvicorn</code></a> - for the server that loads and serves your application.
* <a href="https://github.com/ijl/orjson" target="_blank"><code>orjson</code></a> - Required if you want to use `ORJSONResponse`.



## License

This project is licensed under the terms of the MIT license.
