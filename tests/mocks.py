from dotmap import DotMap
from app.db.database import get_db
from fastapi import Depends

_mocks: dict = {
    'db': Depends(get_db),
    'card_id': '61d21fdc00988e6ca9284474',
    'card_insertion': {'hours': 1, 'price': 87.0, 'title': 'Card updated', 'description': ''}
}
MOCKS = DotMap(_mocks)

