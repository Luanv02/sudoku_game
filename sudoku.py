import random
import copy

def sudoku():

    tabuleiroVerdade = [[0 for _ in range(9)] for _ in range(9)]
    
    def verificacao(sudoku, linha, col, num):
        for x in range(9):
            if sudoku[linha][x] == num:
                return False
            
        for x in range(9):
            if sudoku[x][col] == num:
                return False
        
        bloco_linhas = (linha // 3) * 3
        bloco_colunas = (col // 3) * 3  
        for i in range(3):
            for j in range(3):
                if sudoku[bloco_linhas + i][bloco_colunas + j] == num:
                    return False
                
        return True
    
    def valueTabuleiro(sudoku, linha = 0, col = 0):
        if col == 9:
            col = 0
            linha += 1
            if linha == 9:
                return True
            
        numeros = list(range(1, 10))
        random.shuffle(numeros)
        for num in numeros:
            if verificacao(sudoku, linha, col, num):
                sudoku[linha][col] = num
                if valueTabuleiro(sudoku, linha, col + 1):
                    return True
                sudoku[linha][col] = 0

        return False
    
    valueTabuleiro(tabuleiroVerdade)
    return tabuleiroVerdade

def sudokuIncompleto():
    tabuleiroVerdade = sudoku()
    tabuleiroIncompleto = copy.deepcopy(tabuleiroVerdade)

    dificuldades = {'Fácil': 20, 'Médio': 40, 'Difícil': 60}
    dificuldade = dificuldades['Médio']

    posicoes = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(posicoes)

    for i in range(dificuldade):
        linha, col = posicoes[i]
        tabuleiroIncompleto[linha][col] = 0

    return tabuleiroIncompleto

# tabuleiroVerdade, tabuleiroIncompleto = sudokuIncompleto()
# print("Tabuleiro Completo:")
# for linha in tabuleiroVerdade:
#     print(linha)
# print("\nTabuleiro Incompleto:")
# for linha in tabuleiroIncompleto:
#     print(linha)