import tkinter # naiportuje to tkinter
from random import * # naiportuje to knižnicu random
canvas = tkinter.Canvas() # vytvorí to plátno
canvas.pack() # vykreslí to plátno

def bomba(): # funkcia odpocet
    canvas.delete('all')
    global cas # globálna premenná
    cas = 60 # premenná cas
    if cas>0: # ak je cas väčší ako 0
        cas=cas-1 # stále pokiaľ je premenná cas väčšia ako 0 tak sa odpočita 1 (nefunguje neviem prečo)
        canvas.create_rectangle(10, 10, 370, 200, fill='white') # vykreslí to bielu kocku na danných súradniciach
        canvas.create_text(190, 100, text=cas, font=('Arial','120','bold'), fill='red') # vykreslí to číslo v strede obdĺžnika ktoré sa bude odpočítavať
    else: # inak
        canvas.create_rectangle(10, 10, 370, 200, fill='white') # vykreslí to bielu kocku na danných súradniciach
        canvas.create_text(190, 100, text='Bomba vybuchla', font=('Arial', '30','bold')) # pokiaľ je cas menší ako 0 tak to napíše text: Bomba Vybuchla
    canvas.after(1000, bomba) # opakuje to každých 500ms všetko čo je vo funkcii

button1=tkinter.Button(text="Modrý káblik") # vytovrí to tlačitko na ktorom bude napísané Rovnaké čisla
button1.pack() # vykreslí to tlačitko

button2=tkinter.Button(text="Červený káblik") # vytovrí to tlačitko na ktorom bude napísané Rovnaké čisla
button2.pack() # vykreslí to tlačitko

button3=tkinter.Button(text="Žltý káblik") # vytovrí to tlačitko na ktorom bude napísané Rovnaké čisla
button3.pack() # vykreslí to tlačitko

button4=tkinter.Button(text="Zelený káblik") # vytovrí to tlačitko na ktorom bude napísané Rovnaké čisla
button4.pack() # vykreslí to tlačitko

bomba()

