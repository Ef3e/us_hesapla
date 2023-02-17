from tkinter import *
from tkinter import messagebox
import tkinter as tk
window = Tk()
window.geometry("250x150+500+100")
window.title("üs hesapla")
window.resizable(height=False,width=False)
window.configure(background="#F0BAF5")

sayi_label = Label(window,text="taban sayı",font="bold 9",background="#F0BAF5").place(x=20,y=20)
us_label = Label(window,text="üs sayı",font="bold 9",background="#F0BAF5").place(x=180,y=20)

taban_sayi_al = Entry(bg="white",width=10)
taban_sayi_al.place(x = 10,y=40)

us_sayi_al = Entry(bg="white",width=10)
us_sayi_al.place(x = 180,y=40)

entr1 = Entry(font="bold 12",bg="#F0BAF5",
        fg="red")
entr1.place(x=35,y = 95)
def us_hesapla():
    entr1.delete(0,tk.END)
    sonuc = 1
    try:  
        taban = taban_sayi_al.get()
        us = us_sayi_al.get()
        taban = int(taban)
        us = int(us)
        for u in range(us):
            sonuc = sonuc * taban
        entr1.insert(0,sonuc)
    except:
        messagebox.showwarning("HATA","HATA : LÜTFEN SAYI GİRİNİZ ")
hesapla = Button(window,text="hesapla",bg = "red",command=us_hesapla).pack()

window.mainloop()
