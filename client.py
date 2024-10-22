import grpc
import gomoku_pb2
import gomoku_pb2_grpc

def print_tabuleiro(stub):
    response = stub.GetTabuleiro(gomoku_pb2.Vazio())
    for linha in response.linhas:
        print(linha)

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = gomoku_pb2_grpc.GomokuStub(channel)

        while True:
            
            print_tabuleiro(stub)

            linha = int(input("Linha (1 a 15): "))
            coluna = int(input("Coluna (1 a 15): "))
            jogador = input("Jogador (X ou O): ")

            response = stub.Jogar(gomoku_pb2.JogadaRequest(linha=linha, coluna=coluna, jogador=jogador))
            if response.sucesso:
                print("Jogada realizada com sucesso!")
            else:
                print("Jogada inválida. Tente novamente.")

            vencedor_response = stub.VerificarVencedor(gomoku_pb2.Vazio())
            if vencedor_response.vencedor:
                print_tabuleiro(stub)
                print(f"O vencedor é: {vencedor_response.vencedor}")
                break

if __name__ == '__main__':
    run()
