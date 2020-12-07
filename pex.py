import random
from os import listdir, chdir, mkdir
import tkinter as tk
from tkinter import NORMAL, CENTER, LEFT, NO, NORMAL, W, E, N, S, StringVar, ttk, DISABLED
from time import sleep
import tkinter.messagebox

adresar = "C:/Pexeso/"
try:
    chdir(adresar)
except FileNotFoundError:
    mkdir(adresar)
    mkdir(adresar + "Barvy")
    mkdir(adresar + "Auta")
    mkdir(adresar + "Znacky")
    mkdir(adresar + "Kytky")


class pexeso:

    def __init__(self):
        self.obrazky = []
        self.cesta = "D:/Python/Projekty_Python/Pex/"
        self.volba = ""
        self.sedy_obrazek = "D:/Python/Projekty_Python/Pex/Barvy/vychozi.gif"
        self.obr = []
        self.c_tlacitka = []


    def zamichat(self, cesta, volba):
        cesta_k_obrazkum = cesta + volba + "/"
        nactene_obrazky = listdir(cesta_k_obrazkum) * 2  # načte názvy všech souborů do proměnné jako řetězec
        # funguje
        for zamichat in range(1001):
            random.shuffle(nactene_obrazky)
        self.obrazky = nactene_obrazky




class pexesoGUI(tk.Frame):

    def __init__(self, parent, pexeso):
        super().__init__(parent)
        self.parent = parent
        self.pexeso = pexeso
        self.parent.title("Pexeso")
        self.sirka = 20
        self.vyska = 7
        self.parent.protocol("WM_DELETE_WINDOW", self.on_close)
        self.create_widgets()

    def create_widgets(self):
        self.auta = tk.Button(text="Auta", width=self.sirka, background="green", state=NORMAL, height=2, command=self.auta)
        self.auta.grid(row=0, column=1)
        self.znacky = tk.Button(text="Značky", width=self.sirka, background="green", state=NORMAL, height=2, command=self.znacky)
        self.znacky.grid(row=0, column=2)
        self.kytky = tk.Button(text="Kytky", width=self.sirka, background="green", state=NORMAL, height=2, command=self.kytky)
        self.kytky.grid(row=0, column=3)
        self.barvy = tk.Button(text="Barvy", width=self.sirka, background="green", state=NORMAL, height=2, command=self.barvy)
        self.barvy.grid(row=0, column=4)

        self.button1 = tk.Button(text="1", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T1)
        self.button1.grid(row=1, column=0)
        self.button2 = tk.Button(text="2", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T2)
        self.button2.grid(row=1, column=1)
        self.button3 = tk.Button(text="3", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T3)
        self.button3.grid(row=1, column=2)
        self.button4 = tk.Button(text="4", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T4)
        self.button4.grid(row=1, column=3)
        self.button5 = tk.Button(text="5", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T5)
        self.button5.grid(row=1, column=4)
        self.button6 = tk.Button(text="6", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T6)
        self.button6.grid(row=1, column=5)

        self.obrazek1 = tk.PhotoImage(file=self.pexeso.sedy_obrazek)
        self.image1 = tk.Label(image=self.obrazek1)
        self.image1.grid(row=1, column=7)

        self.button7 = tk.Button(text="7", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T7)
        self.button7.grid(row=2, column=0)
        self.button8 = tk.Button(text="8", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T8)
        self.button8.grid(row=2, column=1)
        self.button9 = tk.Button(text="9", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T9)
        self.button9.grid(row=2, column=2)
        self.button10 = tk.Button(text="10", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T10)
        self.button10.grid(row=2, column=3)
        self.button11 = tk.Button(text="11", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T11)
        self.button11.grid(row=2, column=4)
        self.button12 = tk.Button(text="12", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T12)
        self.button12.grid(row=2, column=5)
        self.skore1 = tk.Label(text="6", font="Arial 40", padx=90, pady=self.vyska)
        self.skore1.grid(row=2, column=7)

        self.button13 = tk.Button(text="13", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T13)
        self.button13.grid(row=3, column=0)
        self.button14 = tk.Button(text="14", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T14)
        self.button14.grid(row=3, column=1)
        self.button15 = tk.Button(text="15", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T15)
        self.button15.grid(row=3, column=2)
        self.button16 = tk.Button(text="16", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T16)
        self.button16.grid(row=3, column=3)
        self.button17 = tk.Button(text="17", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T17)
        self.button17.grid(row=3, column=4)
        self.button18 = tk.Button(text="18", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T18)
        self.button18.grid(row=3, column=5)
        self.zkouska = tk.Button(text="Vyhodnoť", width=self.sirka, state=NORMAL, height=self.vyska, command=self.vyhodnot_karty)
        self.zkouska.grid(row=3, column=7, rowspan=2, sticky=W+E+N+S,)


        self.button19 = tk.Button(text="19", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T19)
        self.button19.grid(row=4, column=0)
        self.button20 = tk.Button(text="20", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T20)
        self.button20.grid(row=4, column=1)
        self.button21 = tk.Button(text="21", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T21)
        self.button21.grid(row=4, column=2)
        self.button22 = tk.Button(text="22", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T22)
        self.button22.grid(row=4, column=3)
        self.button23 = tk.Button(text="23", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T23)
        self.button23.grid(row=4, column=4)
        self.button24 = tk.Button(text="24", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T24)
        self.button24.grid(row=4, column=5)

        self.button25 = tk.Button(text="25", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T25)
        self.button25.grid(row=5, column=0)
        self.button26 = tk.Button(text="26", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T26)
        self.button26.grid(row=5, column=1)
        self.button27 = tk.Button(text="27", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T27)
        self.button27.grid(row=5, column=2)
        self.button28 = tk.Button(text="28", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T28)
        self.button28.grid(row=5, column=3)
        self.button29 = tk.Button(text="29", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T29)
        self.button29.grid(row=5, column=4)
        self.button30 = tk.Button(text="30",width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T30)
        self.button30.grid(row=5, column=5)
        self.skore2 = tk.Label(text="4", font="Arial 40", padx=90, pady=self.vyska)
        self.skore2.grid(row=5, column=7)

        self.button31 = tk.Button(text="31", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T31)
        self.button31.grid(row=6, column=0)
        self.button32 = tk.Button(text="32", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T32)
        self.button32.grid(row=6, column=1)
        self.button33 = tk.Button(text="33", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T33)
        self.button33.grid(row=6, column=2)
        self.button34 = tk.Button(text="34", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T34)
        self.button34.grid(row=6, column=3)
        self.button35 = tk.Button(text="35", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T35)
        self.button35.grid(row=6, column=4)
        self.button36 = tk.Button(text="36", width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T36)
        self.button36.grid(row=6, column=5)

        self.obrazek2 = tk.PhotoImage(file=self.pexeso.sedy_obrazek)
        self.image2 = tk.Label(image=self.obrazek2)
        self.image2.grid(row=6, column=7)

    def vyhodnot_karty(self):
        if self.pexeso.obr[0] == self.pexeso.obr[1]:
            self.pexeso.obr = []
            print("Super a dopiš skore.")
        else:
            self.obrazek1.config(file=self.pexeso.sedy_obrazek)
            self.obrazek2.config(file=self.pexeso.sedy_obrazek)
            for tlacitko in self.pexeso.c_tlacitka:
                if tlacitko == 1:
                    self.button1.config(state=NORMAL)
                    self.button1.config(background="grey")
                elif tlacitko == 2:
                    self.button2.config(state=NORMAL)
                    self.button2.config(background="grey")
                elif tlacitko == 3:
                    self.button3.config(state=NORMAL)
                    self.button3.config(background="grey")
                elif tlacitko == 4:
                    self.button4.config(state=NORMAL)
                    self.button4.config(background="grey")
                elif tlacitko == 5:
                    self.button5.config(state=NORMAL)
                    self.button5.config(background="grey")
                elif tlacitko == 6:
                    self.button6.config(state=NORMAL)
                    self.button6.config(background="grey")
                elif tlacitko == 7:
                    self.button7.config(state=NORMAL)
                    self.button7.config(background="grey")
                elif tlacitko == 8:
                    self.button8.config(state=NORMAL)
                    self.button8.config(background="grey")
                elif tlacitko == 9:
                    self.button9.config(state=NORMAL)
                    self.button9.config(background="grey")
                elif tlacitko == 10:
                    self.button10.config(state=NORMAL)
                    self.button10.config(background="grey")
                elif tlacitko == 11:
                    self.button11.config(state=NORMAL)
                    self.button11.config(background="grey")
                elif tlacitko == 12:
                    self.button12.config(state=NORMAL)
                    self.button12.config(background="grey")
                elif tlacitko == 13:
                    self.button13.config(state=NORMAL)
                    self.button13.config(background="grey")
                elif tlacitko == 14:
                    self.button14.config(state=NORMAL)
                    self.button14.config(background="grey")
                elif tlacitko == 15:
                    self.button15.config(state=NORMAL)
                    self.button15.config(background="grey")
                elif tlacitko == 16:
                    self.button16.config(state=NORMAL)
                    self.button16.config(background="grey")
                elif tlacitko == 17:
                    self.button17.config(state=NORMAL)
                    self.button17.config(background="grey")
                elif tlacitko == 18:
                    self.button18.config(state=NORMAL)
                    self.button18.config(background="grey")
                elif tlacitko == 19:
                    self.button19.config(state=NORMAL)
                    self.button19.config(background="grey")
                elif tlacitko == 20:
                    self.button20.config(state=NORMAL)
                    self.button20.config(background="grey")
                elif tlacitko == 21:
                    self.button21.config(state=NORMAL)
                    self.button21.config(background="grey")
                elif tlacitko == 22:
                    self.button22.config(state=NORMAL)
                    self.button22.config(background="grey")
                elif tlacitko == 23:
                    self.button23.config(state=NORMAL)
                    self.button23.config(background="grey")
                elif tlacitko == 24:
                    self.button24.config(state=NORMAL)
                    self.button24.config(background="grey")
                elif tlacitko == 25:
                    self.button25.config(state=NORMAL)
                    self.button25.config(background="grey")
                elif tlacitko == 26:
                    self.button26.config(state=NORMAL)
                    self.button26.config(background="grey")
                elif tlacitko == 27:
                    self.button27.config(state=NORMAL)
                    self.button27.config(background="grey")
                elif tlacitko == 28:
                    self.button28.config(state=NORMAL)
                    self.button28.config(background="grey")
                elif tlacitko == 29:
                    self.button29.config(state=NORMAL)
                    self.button29.config(background="grey")
                elif tlacitko == 30:
                    self.button30.config(state=NORMAL)
                    self.button30.config(background="grey")
                elif tlacitko == 31:
                    self.button31.config(state=NORMAL)
                    self.button31.config(background="grey")
                elif tlacitko == 32:
                    self.button32.config(state=NORMAL)
                    self.button32.config(background="grey")
                elif tlacitko == 33:
                    self.button33.config(state=NORMAL)
                    self.button33.config(background="grey")
                elif tlacitko == 34:
                    self.button34.config(state=NORMAL)
                    self.button34.config(background="grey")
                elif tlacitko == 35:
                    self.button35.config(state=NORMAL)
                    self.button35.config(background="grey")
                elif tlacitko == 36:
                    self.button36.config(state=NORMAL)
                    self.button36.config(background="grey")
            self.pexeso.obr = []
        return

        
    def auta(self):
        ...
        """
        self.pexeso.volba = ""
        self.pexeso.volba = "Auta"
        self.pexeso.zamichat(self.pexeso.cesta, self.pexeso.volba)
        """

    def znacky(self):
        ...
        """
        self.pexeso.volba = ""
        self.pexeso.volba = "Znacky"
        self.pexeso.zamichat(self.pexeso.cesta, self.pexeso.volba)
        """

    def kytky(self):
        ...
        """
        self.pexeso.volba = ""
        self.pexeso.volba = "Kytky"
        self.pexeso.zamichat(self.pexeso.cesta, self.pexeso.volba)
        """

    def barvy(self):
        self.pexeso.volba = ""
        self.pexeso.volba = "Barvy"
        self.pexeso.zamichat(self.pexeso.cesta, self.pexeso.volba)

    def T1(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button1.config(background="blue")
            self.button1.config(state=DISABLED)
            self.pexeso.obr.append(self.pexeso.obrazky[0]) # přespsat o číslo více
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[0]) # přespsat o číslo více
            self.pexeso.c_tlacitka.append(1)
        elif len(self.pexeso.obr) == 1:
            self.button1.config(background="blue")
            self.pexeso.obr.append(self.pexeso.obrazky[0]) # přespsat o číslo více
            self.button1.config(state=DISABLED)
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[0]) # přespsat o číslo více
            self.pexeso.c_tlacitka.append(1)

        
    def T2(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button2.config(background="blue")
            self.button2.config(state=DISABLED)
            self.pexeso.obr.append(self.pexeso.obrazky[1]) # přespsat o číslo více
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[1]) # přespsat o číslo více
            self.pexeso.c_tlacitka.append(2)  # v závorve je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button2.config(background="blue")
            self.pexeso.obr.append(self.pexeso.obrazky[1]) # přespsat o číslo více
            self.button2.config(state=DISABLED)
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[1]) # přespsat o číslo více
            self.pexeso.c_tlacitka.append(2) # v závorve je číslo tlačítka



    def T3(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button3.config(background="blue") # přepsat číslo tlačítka
            self.button3.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[2]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[2]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(3)  # v závorve je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button3.config(background="blue") # přepsat číslo tlačítka
            self.button3.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[2]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[2]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(3)  # v závorve je číslo tlačítka
        

    def T4(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button4.config(background="blue") # přepsat číslo tlačítka
            self.button4.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[3]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[3]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(4)  # v závorve je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button4.config(background="blue") # přepsat číslo tlačítka
            self.button4.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[3]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[3]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(4)  # v závorve je číslo tlačítka
       

    def T5(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button5.config(background="blue") # přepsat číslo tlačítka
            self.button5.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[4]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[4]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(5)  # v závorve je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button5.config(background="blue") # přepsat číslo tlačítka
            self.button5.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[4]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[4]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(5)  # v závorve je číslo tlačítka
       

    def T6(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button6.config(background="blue") # přepsat číslo tlačítka
            self.button6.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[5]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[5]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(6)  # v závorve je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button6.config(background="blue") # přepsat číslo tlačítka
            self.button6.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[5]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[5]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(6)  # v závorve je číslo tlačítka
        

    def T7(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button7.config(background="blue") # přepsat číslo tlačítka
            self.button7.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[6]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[6]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(7)  # v závorve je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button7.config(background="blue") # přepsat číslo tlačítka
            self.button7.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[6]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[6]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(7)  # v závorve je číslo tlačítka
        

    def T8(self):
        ...
       

    def T9(self):
        ...
       

    def T10(self):
        ...
        

    def T11(self):
        ...
        

    def T12(self):
        ...
        

    def T13(self):
        ...
        

    def T14(self):
        ...
        

    def T15(self):
        ...
       

    def T16(self):
        ...
       

    def T17(self):
        ...
       

    def T18(self):
        ...
        

    def T19(self):
        ...
        

    def T20(self):
        ...
        

    def T21(self):
        ...
        

    def T22(self):
        ...
        

    def T23(self):
        ...
        

    def T24(self):
        ...
        

    def T25(self):
        ...
        

    def T26(self):
        ...
        

    def T27(self):
        ...
        

    def T28(self):
        ...
        

    def T29(self):
        ...
        

    def T30(self):
        ...
        

    def T31(self):
        ...
        

    def T32(self):
        ...
        

    def T33(self):
        ...
       

    def T34(self):
        ...
       

    def T35(self):
        ...
        

    def T36(self):
        ...
        

    def on_close(self):
       self.parent.destroy()


    
if __name__ == '__main__':
    root = tk.Tk()
    pexeso = pexeso()
    app = pexesoGUI(root, pexeso)
    app.mainloop()