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
janela.geometry("235x318")
janela.config(bg=cor1)

frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)


frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# Buttons

b_1 = Button(frame_corpo, text="C", width=11, height=2)
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo, text="%", width=2, height=2)
b_2.place(x=120, y=0)

b_3 = Button(frame_corpo, text="/", width=2, height=2)
b_3.place(x=180, y=0)

janela.mainloop()