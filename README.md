# O que é RPC?

RPC significa "Remote Procedure Call" (Chamada de Procedimento Remoto). É um protocolo que permite que um programa execute uma função ou procedimento em outro endereço de espaço (geralmente em outro servidor) como se fosse uma chamada local.
Em outras palavras, permite que você chame métodos em um servidor remoto como se estivesse chamando métodos locais.

# Instalar a biblioteca gRPC

pip install grpcio grpcio-tools

# Gerar arquivos a partir do .proto

python -m grpc_tools.protoc -I=protos --python_out=. --grpc_python_out=. protos/gomoku.proto

# Primeiro rodar o servidor

python server.py

# Segundo rodas os clientes

python client_X.py
python client_0.py
