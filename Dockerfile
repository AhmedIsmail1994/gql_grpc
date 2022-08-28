FROM python:3.8

WORKDIR /src
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./protos ./protos
COPY ./gql ./gql
COPY ./Makefile .
COPY ./svc ./svc

# RUN make grpc-gen
# COPY ./protos/generated ./protos/generated

CMD uvicorn --port=80 --host=0.0.0.0 gql.api:app