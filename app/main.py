from fastapi import FastAPI, Depends
from config import APP_CONFIG, Settings
from app.shared.dependencies import get_settings
from app.routers import courses

app = FastAPI(**APP_CONFIG)

@app.get('/', tags=['root'])
async def root() -> dict:
    '''' Root path get function
    :return: {'api': 'FastAPI Template'}
    '''
    return {'api': 'FastAPI Template'}

@app.get('/log', tags=['root'])
async def settings(
        msg: str,
        settings: Settings = Depends(get_settings)
    ) -> dict:
    settings.info_logger.info(msg)
    return { 'msg': 'message logged successfully' }

app.include_router(courses)
