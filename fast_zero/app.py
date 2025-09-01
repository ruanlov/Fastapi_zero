from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message, UserDB, UserPublic, UserSchema

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'ola mundo'}


@app.get('/rota', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def rota2():
    return """
    <html>
        <head>
            <title>meu ola mundo</title>
        </head>
        <body>
            <h1>Ola mundo</h1>
        </body>
    </html>"""


database = []


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)

    database.append(user_with_id)

    return user_with_id
