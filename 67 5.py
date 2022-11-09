import tkinter # naimportuje to tkinter
canvas = tkinter.Canvas(width=400, heigh=400) # vytovrí to plátno
canvas.pack() # vykreslí to plátno

canvas.create_rectangle(150, 50, 250, 350, fill='black') # vykreslí to čierny obdĺžnik

canvas.create_oval(155, 55, 245, 140, fill='red') # vykreslí to červený kruh
canvas.create_oval(155, 145, 245, 240, fill='yellow') # vykreslí to žltý kruh
canvas.create_oval(155, 245, 245, 340, fill='green') # vykreslí to zelený kruh
