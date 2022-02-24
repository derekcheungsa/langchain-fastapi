from fastapi import FastAPI

from config import APP_CONFIG
from app.routers import courses

app = FastAPI(**APP_CONFIG)

@app.get('/', tags=['root'])
async def root() -> dict:
    '''' Root path get function
    :return: {'api': 'FastAPI Template'}
    '''
    return {'api': 'FastAPI Template'}

app.include_router(courses)
