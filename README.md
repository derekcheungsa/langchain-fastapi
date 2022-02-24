<p align="center">
  <a href="https://gitlab.com/juanesquintero/fastapi-template"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI"></a>
</p>

<h1 style="margin-top: -80px;" align="center">
<i> JQ </i> &nbsp; TEMPLATE
</h1>



---

**Source Code**: <a href="https://gitlab.com/juanesquintero/fastapi-template" target="_blank"> https://gitlab.com/juanesquintero/fastapi-template </a>

<br>

## Local Environment
This project can be run it on your local machine or in a docker container,
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

Python 3.10.2
https://www.python.org/downloads/release/python-3102/

FastAPI 0.73.0
https://fastapi.tiangolo.com/

Typer
https://typer.tiangolo.com/

SQLAlchemy 1.4.31
https://www.sqlalchemy.org/

<br>


## SetUp
  ###Local
  After install the local environment pyenv use the certain python version and upgrade pip and install the venv package.
  
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
  
  Create <b><i>.env</i></b> file with the environment variables

    DB_HOST=localhost 
    DB_PORT=3305
    DB_SCHEMA=academy
    DB_USER=root
    DB_PASSWORD=admin
<br>

## Folder Structure  


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
  The run.py file has dev env run parameters
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
