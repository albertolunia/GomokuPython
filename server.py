from concurrent import futures
import grpc
import gomoku_pb2
import gomoku_pb2_grpc
from gomoku_game import Gomoku

class GomokuService(gomoku_pb2_grpc.GomokuServicer):
    def __init__(self):
        self.gomoku = Gomoku()

    def Jogar(self, request, context):
        if request.jogador != self.gomoku.get_jogador_atual():
            return gomoku_pb2.JogadaResponse(sucesso=False)

        sucesso = self.gomoku.jogar(request.linha, request.coluna)
        return gomoku_pb2.JogadaResponse(sucesso=sucesso)

    def VerificarVencedor(self, request, context):
        vencedor = self.gomoku.verificar_vencedor()
        return gomoku_pb2.VencedorResponse(vencedor=vencedor if vencedor else "")
    
    def GetTabuleiro(self, request, context):
        tabuleiro = ["".join(linha) for linha in self.gomoku.tabuleiro]
        return gomoku_pb2.TabuleiroResponse(linhas=tabuleiro)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gomoku_pb2_grpc.add_GomokuServicer_to_server(GomokuService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor rodando na porta 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
