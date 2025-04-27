## file to start the calculator project

from tkinter import *
from tkinter import ttk


#colors
cor1 = "#1e1f1e" #black
cor2 = "#feffff" #white 
cor3 = "#38576b" #Blue/grey
cor4 = "#ECEFF1" #grey
cor5 = "#FFAB40" #orange



janela = Tk()
janela.title("Calculator")
janela.geometry("400x570")
janela.config(bg=cor3)

frame_tela = Frame(janela, width=400, height=150)
frame_tela.grid(row=0, column=0)


janela.mainloop()