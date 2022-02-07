from fastapi import Header, HTTPException
from app.db.database import get_db

get_db = get_db
async def get_jwt(token: str = Header(...)):
    if token != 'fake-super-secret-token':
        raise HTTPException(status_code=400, detail='X-Token header invalid')

