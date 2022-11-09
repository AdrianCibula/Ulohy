import tkinter # naimportuje to tkinter
import random # naimportuje to knižnicu random
canvas = tkinter.Canvas(width=1000, height=500) # vytvorí to plátno
canvas.pack() # vykreslí to plátno

def striga(): # funkcia striga
        global x,y # globálna premenná x a y
        global x1,y1 # globálna premenná x1 a y1
        speed1 = random.randint(0,11) # vyberá to random čísla od 0 po 11
        speed2 = random.randint(0,11) # vyberá to random čisla od 0 po 11
        first = 0 # premenná first ktorá je nastavená na 0
        canvas.delete = ('all') # vymaže to všetko čo je nakreslené

        #príkazy ktoré vykreslia strigy a jej veci
        canvas.create_line(x-30,y,x-30,y,width=3)
        canvas.create_line(x-40,y-20,x-30,y, width=2)
        canvas.create_line(x-40,y-15,x-30,y,width=2)
        canvas.create_line(x-40,y-10,x-30,y,width=2)
        canvas.create_line(x-40,y-5,y-30,y,width=2)
        canvas.create_line(x-40,y-0,y-30,y,width=2)
        canvas.create_line(x-40,y+5,y-30,y,width=2)
        canvas.create_line(x-40,y+10,y-30,y,width=2)
        canvas.create_line(x-40,y+15,y-30,y,width=2)
        canvas.create_line(x-40,y+20,y-30,y,width=2)
        canvas.create_rectangle(x-5,y-15,x+5,y+10, width=2)
        canvas.create_oval(x-5,y-25,x+5,y-15,width=2)
        canvas.create_line(x1-30, y1, x1+30, y1, width=3, fill='brown')
        canvas.create_line(x1-40, y1-20, x1+30, y1, width=2, fill='brown')
        canvas.create_line(x1-40, y1-15, x1+30, y1, width=2, fill='brown')
        canvas.create_line(x1-40, y1-10, x1+30, y1, width=2, fill='brown')
        canvas.create_line(x1-40, y1-5, x1+30, y1, width=2, fill='brown')
        canvas.create_line(x1-40, y1-0, x1+30, y1, width=2, fill='brown')
        canvas.create_line(x1-40, y1+5, x1+30, y1, width=2, fill='brown')
        canvas.create_line(x1-40, y1+10, x1+30, y1, width=2, fill='brown')
        canvas.create_line(x1-40, y1+15, x1+30, y1, width=2, fill='brown')
        canvas.create_line(x1-40, y1+20, x1+30, y1, width=2, fill='brown')
        canvas.create_rectangle(x1-5, y1-15, x1+5, y1+10, width=2, fill='red')
        canvas.create_oval(x-5, y1-25, x1+5, y1-15, width=2, fill='red')

        y = y+speed1 # premenná y a y+speed1
        y1 = y1+speed2 # premenná y1 a y1+speed2

        if y > 500: # ak y je väčšia ako 500
                first += 1 # tak do premennej first sa pridá 1
        if y1 > 500: # ak y1 je väčšia ako 500
                first -= 1 # tak do premennej first sa odčita 1

        if go == 1: # ak go sa rovná 1
                canvas.after(100, striga) # tak as funkcia striga obnový každých 100ms
        if first == 1: # ak first sa rovná 1
                canvas.create_text(500, 200, text='Čierna', font='Arial') # tak sa napíše text: Čierna
        if first == -1: # ak first sa rovná -1
                canvas.create_text(500, 200, text='Červená', fill='red', font='Arial') # tak sa napíše červený text: Červená


go = 1 # premenná go ktorá je nastavená na 1
x = 200 # premenná x ktorá je nastavená na 200
y = 100 # premenná y ktorá je nastavená na 100
x1 = 600 # premenná x1 ktorá je nastavená na 600
y1 = 100 # premenná y1 ktorá je nastavená na 100
striga() # vykreslí to funkciu striga
