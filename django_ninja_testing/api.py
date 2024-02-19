from ninja import NinjaAPI, Schema
from pydantic import BaseModel, ConfigDict
import json

api = NinjaAPI()

class UserSchema(Schema):
    model_config = ConfigDict(extra='allow')
    username: str

class User(BaseModel):
    model_config = ConfigDict(extra='allow')

    username: str



@api.post("/hello", response={200: UserSchema})
def hello(request, body: UserSchema):
    print(body)
    print(body.__pydantic_extra__)
    request_body = json.loads(request.body)
    user_from_schema = UserSchema(**request_body)
    print(user_from_schema)
    user_pydantic = User(**request_body)
    print(user_pydantic)
    return 200, body