from ninja import NinjaAPI, Schema

api = NinjaAPI()

class UserSchema(Schema):
    """
    This is the description of the schema that should be visible in swagger
    """
    username: str
    email: str
    first_name: str
    last_name: str

class Error(Schema):
    """
    This is the description of the schema that should be visible in swagger ERROR
    """
    message: str


@api.post("/hello", response={200: UserSchema, 403: Error})
def hello(request, body: UserSchema):
    if body.username == 'error':
        return 403, Error(message='error')
    return 200, body