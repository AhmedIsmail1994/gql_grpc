GENERATED_SOURCES = ./protos/generated

install:
	./run pip install -r requirements.txt

grpc-gen:
	@mkdir -p $(GENERATED_SOURCES)
	@touch $(GENERATED_SOURCES)/__init__.py
	@python3 -m grpc_tools.protoc \
			-I ./protos \
			--python_out=$(GENERATED_SOURCES) \
			--grpc_python_out=$(GENERATED_SOURCES) \
			`find ./protos -type f -name '*.proto'`