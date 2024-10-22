import grpc
import gomoku_pb2
import gomoku_pb2_grpc

def print_tabuleiro(stub):
    response = stub.GetTabuleiro(gomoku_pb2.Vazio())
    
    print("\n     ", end="")
    for i in range(1, len(response.linhas) + 1):
        print(f"| {i:02} ", end="")
    print("|")
    
    print("    " + "+----" * len(response.linhas) + "+")
    
    for i, linha in enumerate(response.linhas):
        print(f"{i + 1:02}  ", end="")
        for celula in linha:
            print(f"|  {celula} ", end="")
        print("|")

        print("    " + "+----" * len(response.linhas) + "+")


def run():
    with grpc.insecure_channel('192.168.0.6:50051') as channel:
        stub = gomoku_pb2_grpc.GomokuStub(channel)

        jogador = 'X'
        while True:
            print_tabuleiro(stub)  # Exibe o tabuleiro no início de cada rodada

            print(f"Jogador {jogador}, faça sua jogada:")
            linha = int(input("Linha (1 a 15): "))
            coluna = int(input("Coluna (1 a 15): "))

            response = stub.Jogar(gomoku_pb2.JogadaRequest(linha=linha, coluna=coluna, jogador=jogador))
            if response.sucesso:
                print("Jogada realizada com sucesso!")
            else:
                print("Jogada inválida. Tente novamente.")

            vencedor_response = stub.VerificarVencedor(gomoku_pb2.Vazio())
            if vencedor_response.vencedor:
                print_tabuleiro(stub)  # Exibe o tabuleiro no final
                print(f"O vencedor é: {vencedor_response.vencedor}")
                break

if __name__ == "__main__":
    run()
