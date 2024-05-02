import random

def criar_labirinto_manual():
    labirinto = [
        [2, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 1, 1, 0],
        [3, 0, 0, 0, 0]
    ]
    return labirinto

def criar_labirinto_random():
    labirinto = [[random.randint(0, 1) for _ in range(5)] for _ in range(5)]
    labirinto[0][0] = 2 
    borda = random.choice([0, 4]) 
    labirinto[borda][random.randint(0, 4)] = 3 
    return labirinto
