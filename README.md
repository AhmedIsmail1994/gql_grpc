# gql_grpc

steps to run app:
docker-compose up

open: http://localhost:8082/graphql 

try this query: 

query MyQuery{
  HelloWorld(input:"your name"){
    message
  }
}
