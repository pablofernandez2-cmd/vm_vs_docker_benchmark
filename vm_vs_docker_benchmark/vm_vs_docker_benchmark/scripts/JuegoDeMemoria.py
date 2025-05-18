import tkinter as tk
import random
from functools import partial

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Memoria 🧠")
        self.root.configure(bg="black")
        self.root.geometry("360x400")
        self.root.resizable(False, False)

        self.symbols = ['🍎', '🍌', '🍒', '🍇', '🍉', '🍋', '🥝', '🍑'] * 2
        random.shuffle(self.symbols)

        self.buttons = []
        self.first = None
        self.second = None
        self.matched = []

        self.create_grid()

    def create_grid(self):
        for i in range(4):
            for j in range(4):
                index = i * 4 + j
                btn = tk.Button(
                    self.root,
                    text="",
                    font=('Arial', 18),
                    width=4,
                    height=2,
                    bg="white",
                    fg="black",
                    relief="solid",
                    bd=1,
                    command=partial(self.reveal_symbol, index)
                )
                btn.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(btn)

    def reveal_symbol(self, index):
        if index in self.matched or self.first == index:
            return

        self.buttons[index].config(
            text=self.symbols[index],
            bg="lightblue"
        )

        if self.first is None:
            self.first = index
        elif self.second is None:
            self.second = index
            self.root.after(600, self.check_match)

    def check_match(self):
        if self.symbols[self.first] == self.symbols[self.second]:
            self.matched.extend([self.first, self.second])
            self.buttons[self.first].config(bg="lightgreen")
            self.buttons[self.second].config(bg="lightgreen")
        else:
            self.buttons[self.first].config(text="", bg="white")
            self.buttons[self.second].config(text="", bg="white")

        self.first = None
        self.second = None

        if len(self.matched) == len(self.symbols):
            self.show_victory_message()

    def show_victory_message(self):
        win = tk.Toplevel(self.root)
        win.title("¡Ganaste!")
        win.geometry("280x100")
        win.configure(bg="white")
        tk.Label(win, text="¡Has ganado! 🎉", bg="white", font=("Arial", 12)).pack(pady=10)
        tk.Button(win, text="Salir", command=self.root.quit).pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
