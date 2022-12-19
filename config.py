import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    db_name: str = 'pwd-manager-db'


app_description = '''
Password Manager API with FastAPI helps you do awesome stuff. 🚀

### Cards

* You can **read cards**.
* You can **create cards**.
* You can **update cards**.
* You can **delete cards**.
'''

APP_CONFIG = dict(
    title='FastAPI Template',
    version='0.0.1',
    description=app_description,
    contact={
        'name': 'Juan Quintero',
        'url': 'https://www.linkedin.com/in/juanes-quintero/',
        'email': 'juanestquintero@gmail.com',
    },
    license_info={
        'name': 'Apache 2.0',
        'url': 'https://www.apache.org/licenses/LICENSE-2.0.html',
    },
    openapi_tags=[
        {
            'name': 'cards',
            'description': 'Operations with cards.',
            'externalDocs': {
                'description': 'Cards external docs',
                'url': 'https://fastapi.tiangolo.com/',
            },
        },
    ]
)
