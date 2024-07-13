from ninja import Schema
from django.conf import settings


class Row(Schema):
    name: str
    age: int


user = {
    "name": "Mario",
    "age": 23,
}

r = Row(name=user["name"], age=user["age"])

print(r)
