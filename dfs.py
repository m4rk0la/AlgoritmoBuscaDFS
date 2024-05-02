from criarLabirinto import criar_labirinto_manual, criar_labirinto_random

def dfs(labirinto, linha, coluna, visitados):
    if not posicao(labirinto, linha, coluna) or (linha, coluna) in visitados:
        return None

    visitados.append((linha, coluna))

    if labirinto[linha][coluna] == 3:
        return [(linha, coluna)]
    
    movimentos = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for movimento in movimentos:
        nova_linha = linha + movimento[0]
        nova_coluna = coluna + movimento [1]
        caminho = dfs(labirinto, nova_linha, nova_coluna, visitados)
        if caminho is not None:
            return [(linha, coluna)] + caminho

    visitados.pop()
    return None
    

def posicao(labirinto, linha, coluna):
    num_linhas = len(labirinto)
    num_colunas = len(labirinto[0])
    limite_dentro = 0<= linha < num_linhas and 0<= coluna < num_colunas
    if not limite_dentro:
        return False
    if labirinto[linha][coluna] == 1:
        return False
    return True


labirinto_random = criar_labirinto_random()
labirinto_manual = criar_labirinto_manual()
visitados_manual = []
saida_encontradaManual = dfs(labirinto_manual, 0, 0, visitados_manual)
if saida_encontradaManual:
    print("Saída encontrada do labirinto manual!")
else:
    print("Não há caminhos para a saída do labirinto manual!")

visitados_random = []
saida_encontradaRandom = dfs(labirinto_random, 0, 0, visitados_random)
if saida_encontradaRandom:
    print("Saída encontrada do labirinto Random!")
else:
    print("Não há caminhos para a saída do labirinto random!")