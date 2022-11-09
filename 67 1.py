import tkinter # naimportuje to tkinter
canvas = tkinter.Canvas() # vytvorí to plátno
canvas.pack() # vykreslí to plátno

entry = tkinter.Entry() # vytvori to pole do ktorého sa dá písať
entry.get() # zapisujú sa do toho informácie z pola
entry.pack() # vykreslí to pole

def klik(suradnice): # funkcia klik
    x= suradnice.x # premenná x
    y= suradnice.y # premenná y
    canvas.create_oval(x+20, y, x, y+20) # vytvorí to krúžok na nejakých súradniciach
    canvas.create_rectangle(x+20, y+30, x, y+20) # vytovrí to obdĺžnik na nejakých suradniciach
    canvas.create_text(x+10, y+40, text=entry.get()) # vytovrí to nejaký text ktorý to zoberie z toho pola entry

canvas.bind('<Button-1>', klik) # bind na tlačítko na myši
