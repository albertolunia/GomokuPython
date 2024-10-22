# Instalar a biblioteca gRPC

pip install grpcio grpcio-tools

# Gerar arquivos a partir do .proto

python -m grpc_tools.protoc -I=protos --python_out=. --grpc_python_out=. protos/gomoku.proto

# Primeiro rodar o servidor

python server.py

# Segundo rodas os clientes

python client_X.py
python client_0.py
