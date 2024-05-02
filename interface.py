import tkinter as tk
from criarLabirinto import criar_labirinto_manual, criar_labirinto_random
from dfs import dfs

class LabirintoGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Labirintos")

        self.frame_manual = tk.Frame(self.root)
        self.frame_manual.pack(side=tk.LEFT)
        self.label_manual = tk.Label(self.frame_manual, text="Labirinto Manual")
        self.label_manual.pack()
        self.canvas_manual = tk.Canvas(self.frame_manual, width=250, height=250)
        self.canvas_manual.pack()

        self.frame_random = tk.Frame(self.root)
        self.frame_random.pack(side=tk.RIGHT)
        self.label_random = tk.Label(self.frame_random, text="Labirinto Aleatório")
        self.label_random.pack()
        self.canvas_random = tk.Canvas(self.frame_random, width=250, height=250)
        self.canvas_random.pack()

        self.botao_reiniciar = tk.Button(self.root, text="Gerar Outro", command=self.reiniciar_labirinto)
        self.botao_reiniciar.pack()

        self.gerar_labirintos()

        self.root.mainloop()

    def gerar_labirintos(self):
        self.labirinto_manual = criar_labirinto_manual()
        self.labirinto_random = criar_labirinto_random()

        self.desenhar_labirinto(self.labirinto_manual, self.canvas_manual)
        self.desenhar_labirinto(self.labirinto_random, self.canvas_random)

    def desenhar_labirinto(self, labirinto, canvas):
        caminho = dfs(labirinto, 0, 0, [])
        for linha in range(len(labirinto)):
            for coluna in range(len(labirinto[0])):
                cor = "black" if labirinto[linha][coluna] == 1 else "white"
                if labirinto[linha][coluna] == 2:
                    cor = "blue"  # Cor para a posição inicial
                elif labirinto[linha][coluna] == 3:
                    cor = "red"  # Cor para a posição final
                canvas.create_rectangle(coluna * 50, linha * 50, (coluna + 1) * 50, (linha + 1) * 50, fill=cor)
                if caminho and (linha, coluna) in caminho:
                    canvas.create_oval(coluna * 50 + 10, linha * 50 + 10, (coluna + 1) * 50 - 10, (linha + 1) * 50 - 10, fill="yellow")

    def reiniciar_labirinto(self):
        self.gerar_labirintos()

LabirintoGUI()
