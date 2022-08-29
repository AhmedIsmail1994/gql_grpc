# gql_grpc

### run app:
docker-compose up
<br />

open: http://localhost:8082/graphql 

try this query: 
<br />

`query MyQuery{
  HelloWorld(input:"your name"){
    message
  }
}`
<br />
or 
<br />
`query myQuery{
  UserInfo(email: "test@nutrien.com"){
    first_name
    last_name
    phone
    country
  }
}`
