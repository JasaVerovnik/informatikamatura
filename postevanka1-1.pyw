import random
import tkinter as tk
#globalna spremenljivka, ki je uporabljena za prenos vrednosti rezultatov
#od ustvarjenja (funkcija "refresh") do preverjanja rezultatov (funkcija "checkanscw")
rezultati = []
#funkcija ki se sproži ob pritisku na gumb "Osveži"
def refresh():
    #preverjanje stanja izbirnih polj (1-10)
    button_true_check = []
    stevila = []
    racun = []
    for i in range(1, 11):
        exec(f"button_true_check.append(valgumb{i}.get())")
    for f in range(10):
        if button_true_check[f] == 1:
            stevila.append(f + 1)
    #sestavljanje naključnih računov
    for i in range(10):
        racun.append(random.randint(1, int(koliko.get())))
        racun.append(random.choice(stevila))
    print(racun)
    #vsavljanje vrednosti računov v komponente tkinter, ki račune prikažejo
    for i in range(10):
        exec(f"racun{i+1}_tekst.set(str(racun[{i*2}]) + ' × ' + str(racun[{i*2+1}]) + ' = ?')")
    for j in range(10):
        racun.append(racun[0] * racun[1])
        racun.remove(racun[0])
        racun.remove(racun[0])
    global rezultati
    rezultati = racun
    #ponastavitev barve vnosnih polj
    for i in range(1, 11):
        exec(f"input{i}.configure(background=prazno)")
        exec(f"input{i}.delete(0, tk.END)")
#funkcija, ki preveri pravilnost rezultatov
def checkanscw(rez):
    odg = []
    #pridobivanje vnešenih vrednosti
    for i in range(1, 11):
        exec(f"odg.append(int(odg{i}.get()))")
    #primerjanje vnešenih vrednosti s pravilnimi rezultati
    for i in range(10):
        if odg[0] == rez[i]:
            odg.append(pravilno)
        else:
            odg.append(napacno)
        odg.remove(odg[0])
    #spreminjanje barve vnosnega polja glede na pravilnost
    for i in range(10):
        exec(f"input{i+1}.configure(background=odg[{i}])")
#prikaz in osnovne nastavitve okna
okno = tk.Tk()
okno.title('Poštevanka')
okno.configure(background = '#dfff69')
#okno se prikaže na sredini primarnega zaslona
sirina_zaslona = okno.winfo_screenwidth()
visina_zaslona = okno.winfo_screenheight()
x = (sirina_zaslona - 760) // 2
y = (visina_zaslona - 360) // 2
okno.geometry('%dx%d+%d+%d' % (760, 360, x, y))
okno.resizable(0, 0)
#postavitev kanvasa, na katerem so postavljene druge komponente
canvas = tk.Canvas(okno, width = 720, height = 340, bg = '#efefef')
canvas.pack(pady=20)
#spremenljivke za izbirna polja in postavitev na kanvas
for i in range(1, 11):
	exec(f"valgumb{i} = tk.IntVar()")
	exec(f"gumb{i} = tk.Checkbutton(canvas, text='{i}', variable=valgumb{i}, onvalue=1, offvalue=0)")
	exec(f"gumb{i}.grid(column=0, row={i-1}, sticky=tk.W, padx=2, pady=2)")
#tekst in vnosno polje "Do koliko?", ki določata prvi faktor računa
do_koliko_tekst = tk.Label(canvas, text='Prvi faktor?')
do_koliko_tekst.grid(column=1, row=2, sticky=tk.NS, padx=2, pady=2)
koliko = tk.StringVar()
do_koliko = tk.Entry(canvas, width=8, textvariable=koliko)
do_koliko.grid(column=1, row=3, sticky=tk.NS, padx=2, pady=2)
#gumb "Osveži", ki ob pritisku sproži funkcijo "refresh"
osvezi = tk.Button(canvas, text='Osveži', command=refresh)
osvezi.grid(column=1, row=5, rowspan=5, sticky=tk.NSEW, padx=2, pady=2)
#prazen prostor, ki ločuje račune od nastavtev
space = tk.Label(canvas, text='')
space.grid(column=2, row=0, rowspan=10, sticky=tk.NS, padx=50, pady=2)
#postavitev računov na kanvas
for i in range(1, 11):
	exec(f"racun{i}_tekst = tk.StringVar()")
	exec(f"racun{i}_tekst = tk.StringVar()")
	exec(f"racun{i} = tk.Label(canvas, textvariable=racun{i}_tekst, font=('TkDefaultFont', 12, 'bold'))")
	exec(f"racun{i}.grid(column=3, row={i-1}, sticky=tk.W, padx=2, pady=2)")
	exec(f"odg{i} = tk.StringVar()")
	exec(f"input{i} = tk.Entry(canvas, width=8, textvariable=odg{i})")
	exec(f"input{i}.grid(column=4, row={i-1}, sticky=tk.E, padx=2, pady=2)")
#nastavljanje začetne vrednosti računov na prazno polje
for i in range(1, 11):
    exec(f"racun{i}_tekst.set('')")
preveri = tk.Button(canvas, text='Preveri\nrezultate', command=lambda: checkanscw(rezultati))
preveri.grid(column=5, row=0, rowspan=10, sticky=tk.NSEW, padx=2, pady=2)
#definiranje barv za prazno, pravilno ali napačno izpolnjeno polje
prazno = '#ffffff'
napacno = '#ff8888'
pravilno = '#88ff88'
#mainloop da se okno ne zapre
okno.mainloop()
