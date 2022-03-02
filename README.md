<div align="center"> 
<img height="100" width="110" style="margin-bottom: -70px" alt="FastAPI Template" src="https://gitlab.com/uploads/-/system/project/avatar/33491624/fastapi.png">
<br>
<h1 align="center" style="text-decoration: none;"> FastAPI &nbsp;TEMPLATE </h1>
</div>

<br>
<br>

**Source Code**: <a href="https://gitlab.com/juanesquintero/fastapi-template" target="_blank"> https://gitlab.com/juanesquintero/fastapi-template </a>

---

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
  
---

<br>

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

---

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

---

<br>

## SetUp

  Create <b><i>.env</i></b> file with the environment variables

  ```dosini
  DB_HOST=localhost 
  DB_PORT=3305
  DB_SCHEMA=academy
  DB_USER=root
  DB_PASSWORD=admin
  ```
    

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
```

</div>

If you are in dev mode use:

<div class="termy">

```console
(venv)$ pip install requirements-dev.txt
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
This template counts with a custom CLI to execute clear and simple commands instead long and tedious native commands. 
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
  (venv)$ app-cli test
  ```
  <small>pytest -v tests/</small>

  Run tests & generate html report 
  ```console  
  (venv)$ app-cli test --html
  ```
  <small>pytest -v --html=tests/report.html --self-contained-html tests/</small>

  Run coverage
  ```console
  (venv)$ app-cli coverage
  ```
  <small>pytest --cov-report term-missing --cov=app tests/</small>

  Run coverage & generate html Report
  ```console
  (venv)$ app-cli coverage --html
  ```
  <small>pytest --cov-report html:tests/coverage --cov-report term-missing --cov=app tests/</small>

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

## Other Dependencies

#### Core
[python-dotenv](https://pypi.org/project/python-dotenv/) <br>
[cryptography](https://pypi.org/project/cryptography/)

#### Database
[SQLAlchemy](https://www.sqlalchemy.org/) <br>
[PyMySQL](https://pymysql.readthedocs.io/en/latest/)

#### Utils
[pydash](https://pydash.readthedocs.io/en/latest/) <br>
[dotmap](https://pypi.org/project/dotmap/)

#### App CLI
poetry==1.1.13 <br>
poetry-core==1.0.7

#### Testing
requests==2.27.1 <br>
pytest==7.0.0 <br>
pytest-html==3.1.1 <br>
coverage==6.3.1 <br>
pytest-cov==3.0.0 <br>

#### Linting
pylint==2.5.0 <br>
pylint-plugin-utils==0.6 <br>
autopep8==1.5.6 <br>

### Git
enforce-git-message==1.0.1 <br>
pre-commit==2.15.0


## License

This project is licensed under the terms of the MIT license.
