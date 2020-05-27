from tkinter import*
root = Tk()
root.title("Hesap Makinesi")
e = Entry(root, width =48, borderwidth=2)
e.grid(row=0, column=0, columnspan=5, padx=13, pady=10)

#e.insert(0, "")

def button_click(sayi):
   # e.delete(0,END)
    girilen=e.get()
    e.delete(0,END)
    e.insert(0,str(girilen) + str(sayi))
def button_Temizle():
    e.delete(0,END)

def button_Topla():
    ilkSayi= e.get()
    global ilkS
    global math
    math = "toplam"
    ilkS = int(ilkSayi)
    e.delete(0,END)
def button_Cikart():
    ilkSayi = e.get()
    global ilkS
    global math
    math = "fark"
    ilkS = int(ilkSayi)
    e.delete(0, END)

def button_Carp():
    ilkSayi = e.get()
    global ilkS
    global math
    math = "çarpım"
    ilkS = int(ilkSayi)
    e.delete(0, END)

def button_Bol():
    ilkSayi = e.get()
    global ilkS
    global math
    math = "bölüm"
    ilkS = int(ilkSayi)
    e.delete(0, END)
def button_Esit():

    ikinciSayi = e.get()
    e.delete(0,END)

    if math== "toplam":
        e.insert(0,ilkS + int(ikinciSayi))

    if math== "fark":
        e.insert(0,ilkS - int(ikinciSayi))

    if math== "çarpım":
        e.insert(0,ilkS * int(ikinciSayi))

    if math== "bölüm":
        e.insert(0,ilkS / int(ikinciSayi))


button1 = Button(root, text="1", padx=40, pady=20, command=lambda:button_click(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda:button_click(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda:button_click(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda:button_click(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda:button_click(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda:button_click(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda:button_click(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda:button_click(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda:button_click(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda:button_click(0))
buttonTopla = Button(root, text="+", padx=40, pady=20, command=button_Topla)
buttonEsittir = Button(root, text="=", padx=210, pady=20, command=button_Esit)
buttonCikart = Button(root, text="-", padx=40, pady=20, command=button_Cikart)
buttonBol = Button(root, text="/", padx=40, pady=20, command=button_Bol)
buttonCarp = Button(root, text="x", padx=40, pady=20, command=button_Carp)
buttonTemizle = Button(root, text="C", padx=98, pady=20, command=button_Temizle)


button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)
buttonTemizle.grid(row=4,column=1, columnspan=2)
buttonEsittir.grid(row=5,column=0, columnspan=20)
buttonCarp.grid(row=3,column=3)
buttonCikart.grid(row=2,column=3)
buttonBol.grid(row=1,column=3)
buttonTopla.grid(row=4,column=3)


root.mainloop()