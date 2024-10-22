class Gomoku:
    TAMANHO_TABULEIRO = 2
    PONTOS_GANHAR = 1

    def __init__(self):
        self.tabuleiro = self.inicia_tabuleiro()
        self.jogador_atual = 'X'

    def inicia_tabuleiro(self):
        tabuleiro = [[' ' for _ in range(self.TAMANHO_TABULEIRO)] for _ in range(self.TAMANHO_TABULEIRO)]
        return tabuleiro

    def print_tabuleiro(self):
        print("\n     ", end="")
        for i in range(1, self.TAMANHO_TABULEIRO + 1):
            print(f"| {i:02} ", end="")
        print("|")
        
        print("    " + "+----" * self.TAMANHO_TABULEIRO + "+")

        for i in range(self.TAMANHO_TABULEIRO):
            print(f"{i + 1:02}  ", end="")
            for j in range(self.TAMANHO_TABULEIRO):
                print(f"|  {self.tabuleiro[i][j]} ", end="")
            print("|")
            
            print("    " + "+----" * self.TAMANHO_TABULEIRO + "+")

    def jogar(self, linha, coluna):
        if linha < 1 or linha > self.TAMANHO_TABULEIRO or coluna < 1 or coluna > self.TAMANHO_TABULEIRO:
            print("Jogada fora dos limites. Tente novamente.")
            return False

        if self.tabuleiro[linha - 1][coluna - 1] != ' ':
            print("Posição já ocupada. Tente novamente.")
            return False

        self.tabuleiro[linha - 1][coluna - 1] = self.jogador_atual
        self.jogador_atual = 'O' if self.jogador_atual == 'X' else 'X'
        return True

    def verificar_vencedor(self):
        tabuleiro_completo = True  # Assume que o tabuleiro está completo

        for i in range(self.TAMANHO_TABULEIRO):
            for j in range(self.TAMANHO_TABULEIRO):
                jogador = self.tabuleiro[i][j]
                if jogador == ' ':
                    tabuleiro_completo = False  # Encontrou uma posição vazia
                    continue

                if (self.verificar_direcao(i, j, 0, 1) or
                    self.verificar_direcao(i, j, 1, 0) or
                    self.verificar_direcao(i, j, 1, 1) or
                    self.verificar_direcao(i, j, 1, -1)):
                    self.print_tabuleiro()
                    print(f"Jogador {jogador} venceu!")
                    return True

        if tabuleiro_completo:
            self.print_tabuleiro()
            print("O jogo terminou em empate!")
            return True

        return False

    def verificar_direcao(self, linha, coluna, delta_linha, delta_coluna):
        jogador = self.tabuleiro[linha][coluna]
        contador = 0

        for k in range(self.PONTOS_GANHAR):
            nova_linha = linha + k * delta_linha
            nova_coluna = coluna + k * delta_coluna

            if nova_linha < 0 or nova_linha >= self.TAMANHO_TABULEIRO or nova_coluna < 0 or nova_coluna >= self.TAMANHO_TABULEIRO:
                return False

            if self.tabuleiro[nova_linha][nova_coluna] == jogador:
                contador += 1
            else:
                return False

        return contador == self.PONTOS_GANHAR

    def get_jogador_atual(self):
        return self.jogador_atual

def main():
    gomoku = Gomoku()

    while True:
        gomoku.print_tabuleiro()
        print(f"Jogador {gomoku.get_jogador_atual()}, faça sua jogada.")

        try:
            linha = int(input("Linha (1 a 15): "))
            coluna = int(input("Coluna (1 a 15): "))
        except ValueError:
            print("Entrada inválida. Por favor, insira números inteiros.")
            continue

        if gomoku.jogar(linha, coluna):
            if gomoku.verificar_vencedor():
                break

if __name__ == "__main__":
    main()
