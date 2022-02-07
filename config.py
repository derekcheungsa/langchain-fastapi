app_description = '''
FastAPI Quickstart API helps you do awesome stuff. 🚀

### Courses

* You can **read courses**.
* You can **create courses**.
* You can **update courses**.
* You can **delete courses**.

### Users

You will be able to:
* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
'''
APP_CONFIG = dict(
    title='FastAPI Quickstart',
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
            'name': 'courses',
            'description': 'Operations with courses.',
            'externalDocs': {
                'description': 'Courses external docs',
                'url': 'https://fastapi.tiangolo.com/',
            },
        },
        {
            'name': 'users',
            'description': 'Operations with users. The **login** logic is also here.',
        },
        {
            'name': 'items',
            'description': 'Manage items. So _fancy_ they have their own docs.',
        },
    ]
)
