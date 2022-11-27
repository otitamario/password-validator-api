import strawberry
from enum import Enum
import re
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from typing import List, Union, Optional
from strawberry.scalars import JSON
from services import rules_modules

@strawberry.type
class Result:
    verify: bool
    noMatch: List[str]
    

@strawberry.type
class Query:
    @strawberry.field
    def verify(self, password: str, rules: List[JSON]) -> Result:
        result=rules_modules.return_verify(password, rules)
        return Result(verify=result["verify"],noMatch=result["noMatch"])



schema = strawberry.Schema(Query)


graphql_app = GraphQLRouter(schema)


app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

