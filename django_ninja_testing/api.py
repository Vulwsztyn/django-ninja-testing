from ninja import NinjaAPI, Schema
from pydantic import BaseModel, ConfigDict

api = NinjaAPI()

class UserSchema(Schema):
    model_config = ConfigDict(extra='allow')
    username: str

@api.post("/hello", response={200: UserSchema})
def hello(request, body: UserSchema):
    print(body)
    print(body.__pydantic_extra__)
    return 200, body