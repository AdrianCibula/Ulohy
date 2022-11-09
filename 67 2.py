import tkinter # naimportuje to tkinter
canvas = tkinter.Canvas(width=400, heigh=400) # vytvori to plátno
canvas.pack() # vykreslí to plátno

canvas.create_rectangle(0, 250, 400, 400, fill='blue') # vykreslí to modrý obdĺžnik

def klik(suradnice): #funkcia klik
    x= suradnice.x # premenná x
    y= suradnice.y # premenná y

    if 0<x<400 and 0<y<200: # ak je x väčšie ako 0 alebo menšie ako 400 a y je väčšie ako 0 a menšie ako 200
        canvas.create_oval(x+20, y, x, y+20) # vytovrí to krúžok
        canvas.create_line(x+5, y+20, x+10, y+40) # vytvorí to čiaru
        canvas.create_line(x+15, y+20, x+10, y+40) # vytvorí to čiaru
        canvas.create_rectangle(x+20, y+50, x, y+40) # vytovrí to obdĺžnik
    else: # inak
        canvas.create_rectangle(x+30, y+25, x, y+15) # vytvorí to obdĺžnik
        canvas.create_line(x+20, y, x+20, y+15) # vytvorí to čiaru
        canvas.create_line(x+20, y, x+25, y+2) # vytvorí to čiaru
        canvas.create_line(x+25, y+2, x+20, y+5) # vytvorí to čiaru

canvas.bind('<Button-1>', klik) # bind na tlačítko na myši
