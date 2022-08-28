
import os
from pathlib import Path

from ariadne import QueryType, load_schema_from_path
from ariadne.asgi import GraphQL
from ariadne.contrib.federation import make_federated_schema

query = QueryType()

@query.field("HelloWorld")
def hello_world(self, info, input):
    return {
        "message": f'Hello ${input}!'
    }

type_defs = load_schema_from_path(
    Path(Path(__file__).parent, "schema.graphql").__fspath__()
)


schema = make_federated_schema(type_defs, query)

app = GraphQL(schema)
    
    