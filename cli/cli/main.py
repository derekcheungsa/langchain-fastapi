import typer
from os import system as shell

app = typer.Typer()

@app.command()
def run(env: str = 'dev'):
    '''
    Run app in different envs
    '''
    match env:
        case 'dev':
            shell('uvicorn app:app --reload')
        case 'prod':
            shell('uvicorn app:app --host 0.0.0.0 --port 80 --workers 5')
        case _:
            pass

@app.command()
def test(html: bool = False):
    '''
    Run pytest app tests
    & Generates html report
    '''
    if html:
        typer.echo('Running tests & generating html report...')
        shell('pytest -v --html=tests/report.html --self-contained-html tests/')
    else:
        typer.echo('Running tests...')
        shell('pytest -v tests/')

@app.command()
def coverage(html: bool = False):
    '''
    Shows test coverage
    & Generates html report
    '''
    if html:
        typer.echo('Generating coverage html report...')
        shell('pytest --cov-report html:tests/coverage --cov-report term-missing --cov=app tests/')
    else:
        typer.echo('Running test coverage...')
        shell('pytest --cov-report term-missing --cov=app tests/')
