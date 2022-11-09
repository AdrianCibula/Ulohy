import tkinter # naiportuje to tkinter
from random import * # naiportuje to knižnicu random
canvas = tkinter.Canvas() # vytvorí to plátno
canvas.pack() # vykreslí to plátno

def timer1(): # funkcia timer1
    canvas.delete('all') # vymaže to všetko čo bolo nakreslené
    global jedna # globálna premenná
    global dva # globálna premenná
    jedna = randint(1, 6) # premenná ktorá vyberá random čisla od 1 po 6
    dva = randint(1, 6) # premenná ktorá vyberá random čisla od 1 po 6
    canvas.create_rectangle(20, 50, 150, 180, fill='white') # vykreslí to bielu kocku na danných súradniciach
    canvas.create_rectangle(220, 50, 350, 180, fill='white') # vykreslí to bielu kocku na danných súradniciach
    canvas.create_text(80, 110, text=jedna, font=('Arial','50','bold')) # vykreslí to číslo v strede kocky ktoré sa bude random generovať
    canvas.create_text(285, 110, text=dva, font=('Arial','50','bold')) # vykreslí to číslo v strede kocky ktoré sa bude random generovať
    canvas.create_text(100, 10, text='Počet bodov:') # vykreslí to text s nápisom Počet bodov:
    canvas.create_text(200, 10, text=body) # vykreslí to text v ktorom sa budú ukazovať koľko má hráč bodov
    canvas.after(500, timer1) # opakuje to každých 500ms všetko čo je vo funkcii

def tlacitko(): # funkcia tlacitko
    global body # globálna premenná
    if jedna==dva: # funkcia ak sa premmenná jedna rovná premennej dva tak
        body = body +2 # zapíše to +2 bodov do premennej body
    else: # inak
        body = body -1 # to zapíše -1 bod do premennej body

button=tkinter.Button(text="Rovnaké čísla", command=tlacitko) # vytovrí to tlačitko na ktorom bude napísané Rovnaké čisla
button.place(x=140, y=230) # tlačitko bude na suradniciach x=140 a y=230
button.pack() # vykreslí to tlačitko

body = 0 # premenná body je na začiatku 0
timer1() # opakovanie funkcie timer1
