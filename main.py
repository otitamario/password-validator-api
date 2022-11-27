import strawberry
from enum import Enum
import re
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from typing import List, Union, Optional
from strawberry.scalars import JSON
from services import rules
'''
@strawberry.enum
class RuleKey(Enum):
    minSize = 1
    minUppercase = 2
    minLowercase = 3
    minDigit = 4
    minSpecialChars = 5
    noRepeted = 6

@strawberry.type
class Rule:
    rule: RuleKey
    value: int
'''
@strawberry.type
class Result:
    verify: bool
    noMatch: List[str]

def returnMinSize(password,value):
        size=len(password)
        return {"teste": size >= value}
    

@strawberry.type
class Query:
    @strawberry.field
    def verify(self, password: str, rules: List[JSON]) -> Result:
        for rule in rules:
            if rule["rule"]=="minSize":
                value=rule["value"]
                break
        teste=returnMinSize(password,value)
        return Result(verify=teste["teste"],noMatch=["minSize","minUppercase"])



schema = strawberry.Schema(Query)


graphql_app = GraphQLRouter(schema)


app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")


'''

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"


schema = strawberry.Schema(Query)


graphql_app = GraphQLRouter(schema)


app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

'''