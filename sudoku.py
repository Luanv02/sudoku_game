import random
import copy

def sudoku():

    tabuleiroVerdade = [[0 for i in range(9)] for i in range(9)]
    
    def naoRepetirNumeros(sudoku, linha, col, num):
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
            if naoRepetirNumeros(sudoku, linha, col, num):
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

    value = 'Médio'
    dificuldades = {'Fácil': 20, 'Médio': 35, 'Difícil': 50}
    dificuldade = dificuldades[value]

    posicoes = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(posicoes)

    for i in range(dificuldade):
        linha, col = posicoes[i]
        tabuleiroIncompleto[linha][col] = 0

    return tabuleiroVerdade, tabuleiroIncompleto