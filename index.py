import random; import os; import time as tm; import tkinter as tk

def sorteio():
    moeda = list([0, 1])
    sorteio = random.choice(moeda)
    if sorteio == 0: resultado = "cara"
    else: resultado = "coroa"
    tk.Label(home, text=f'\n\nO resultado do sorteio foi -> {resultado}\t\t\t\t', font=('Montserrat', 18)).place(x=30, y=200)

home = tk.Tk()
home.geometry('600x300')
home.wm_iconbitmap('moedas.ico')
home.resizable(False, False)
home.title("MOEDAS | HOME")
tk.Label(font=('Montserrat', 20), text="SORTEIO DE MOEDAS").place(x=150, y=10)
fazerSORTEIO = tk.Button(master=home, font=('Montserrat', 14), text="SORTEIO DA MOEDA", fg='white', background='red', command=sorteio); fazerSORTEIO.place(x=200, y=120)
home.mainloop()