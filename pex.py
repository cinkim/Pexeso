import random

from os import listdir, chdir, mkdir

import tkinter as tk
from tkinter import NORMAL, CENTER, LEFT, NO, NORMAL, W, E, N, S, StringVar, ttk, DISABLED
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
        self.cesta = "C:/Pexeso/"
        self.volba = ""
        self.sedy_obrazek = "C:/Pexeso/vychozi.gif"
        self.obr = []
        self.c_tlacitka = []
        self.score_1 = 0
        self.score_2 = 0
        self.hr_c = 1


    def zamichat(self, cesta, volba):
        cesta_k_obrazkum = cesta + volba + "/"
        nactene_obrazky = listdir(cesta_k_obrazkum) * 2  # načte názvy všech souborů do proměnné seznam
        if len(nactene_obrazky) != 36:
            tk.messagebox.showwarning("ERROR", "Špatný počet hracích karet.")
            return False
        else:
            for zamichat in range(1001):
                random.shuffle(nactene_obrazky)
            self.obrazky = nactene_obrazky
            return True


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

        self.button1 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T1)
        self.button1.grid(row=1, column=0)
        self.button2 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T2)
        self.button2.grid(row=1, column=1)
        self.button3 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T3)
        self.button3.grid(row=1, column=2)
        self.button4 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T4)
        self.button4.grid(row=1, column=3)
        self.button5 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T5)
        self.button5.grid(row=1, column=4)
        self.button6 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T6)
        self.button6.grid(row=1, column=5)

        self.obrazek1 = tk.PhotoImage(file=self.pexeso.sedy_obrazek)
        self.image1 = tk.Label(image=self.obrazek1)
        self.image1.grid(row=1, column=7)

        self.button7 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T7)
        self.button7.grid(row=2, column=0)
        self.button8 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T8)
        self.button8.grid(row=2, column=1)
        self.button9 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T9)
        self.button9.grid(row=2, column=2)
        self.button10 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T10)
        self.button10.grid(row=2, column=3)
        self.button11 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T11)
        self.button11.grid(row=2, column=4)
        self.button12 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T12)
        self.button12.grid(row=2, column=5)
        self.skore1 = tk.Label(text=self.pexeso.score_1, font="Arial 40", background="blue", padx=90, pady=self.vyska)
        self.skore1.grid(row=2, column=7)

        self.button13 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T13)
        self.button13.grid(row=3, column=0)
        self.button14 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T14)
        self.button14.grid(row=3, column=1)
        self.button15 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T15)
        self.button15.grid(row=3, column=2)
        self.button16 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T16)
        self.button16.grid(row=3, column=3)
        self.button17 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T17)
        self.button17.grid(row=3, column=4)
        self.button18 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T18)
        self.button18.grid(row=3, column=5)
        self.zkouska = tk.Button(text="Vyhodnoť", font="Arial 17", width=self.sirka, state=NORMAL, height=self.vyska, command=self.vyhodnot_karty)
        self.zkouska.grid(row=3, column=7, rowspan=2, sticky=N+S)


        self.button19 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T19)
        self.button19.grid(row=4, column=0)
        self.button20 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T20)
        self.button20.grid(row=4, column=1)
        self.button21 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T21)
        self.button21.grid(row=4, column=2)
        self.button22 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T22)
        self.button22.grid(row=4, column=3)
        self.button23 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T23)
        self.button23.grid(row=4, column=4)
        self.button24 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T24)
        self.button24.grid(row=4, column=5)

        self.button25 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T25)
        self.button25.grid(row=5, column=0)
        self.button26 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T26)
        self.button26.grid(row=5, column=1)
        self.button27 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T27)
        self.button27.grid(row=5, column=2)
        self.button28 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T28)
        self.button28.grid(row=5, column=3)
        self.button29 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T29)
        self.button29.grid(row=5, column=4)
        self.button30 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T30)
        self.button30.grid(row=5, column=5)
        self.skore2 = tk.Label(text=self.pexeso.score_2, font="Arial 40", background="white", padx=90, pady=self.vyska)
        self.skore2.grid(row=5, column=7)

        self.button31 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T31)
        self.button31.grid(row=6, column=0)
        self.button32 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T32)
        self.button32.grid(row=6, column=1)
        self.button33 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T33)
        self.button33.grid(row=6, column=2)
        self.button34 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T34)
        self.button34.grid(row=6, column=3)
        self.button35 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T35)
        self.button35.grid(row=6, column=4)
        self.button36 = tk.Button(width=self.sirka, background="grey", state=NORMAL, height=self.vyska, command=self.T36)
        self.button36.grid(row=6, column=5)

        self.obrazek2 = tk.PhotoImage(file=self.pexeso.sedy_obrazek)
        self.image2 = tk.Label(image=self.obrazek2)
        self.image2.grid(row=6, column=7)

    def vyhodnot_karty(self):
        try:
            if self.pexeso.obr[0] == self.pexeso.obr[1]:
                self.obrazek1.config(file=self.pexeso.sedy_obrazek)
                self.obrazek2.config(file=self.pexeso.sedy_obrazek)
                for tlacitko in self.pexeso.c_tlacitka:
                    if tlacitko == 1:
                        self.button1.config(background="white")
                    elif tlacitko == 2:
                        self.button2.config(background="white")
                    elif tlacitko == 3:
                        self.button3.config(background="white")
                    elif tlacitko == 4:
                        self.button4.config(background="white")
                    elif tlacitko == 5:
                        self.button5.config(background="white")
                    elif tlacitko == 6:
                        self.button6.config(background="white")
                    elif tlacitko == 7:
                        self.button7.config(background="white")
                    elif tlacitko == 8:
                        self.button8.config(background="white")
                    elif tlacitko == 9:
                        self.button9.config(background="white")
                    elif tlacitko == 10:
                        self.button10.config(background="white")
                    elif tlacitko == 11:
                        self.button11.config(background="white")
                    elif tlacitko == 12:
                        self.button12.config(background="white")
                    elif tlacitko == 13:
                        self.button13.config(background="white")
                    elif tlacitko == 14:
                        self.button14.config(background="white")
                    elif tlacitko == 15:
                        self.button15.config(background="white")
                    elif tlacitko == 16:
                        self.button16.config(background="white")
                    elif tlacitko == 17:
                        self.button17.config(background="white")
                    elif tlacitko == 18:
                        self.button18.config(background="white")
                    elif tlacitko == 19:
                        self.button19.config(background="white")
                    elif tlacitko == 20:
                        self.button20.config(background="white")
                    elif tlacitko == 21:
                        self.button21.config(background="white")
                    elif tlacitko == 22:
                        self.button22.config(background="white")
                    elif tlacitko == 23:
                        self.button23.config(background="white")
                    elif tlacitko == 24:
                        self.button24.config(background="white")
                    elif tlacitko == 25:
                        self.button25.config(background="white")
                    elif tlacitko == 26:
                        self.button26.config(background="white")
                    elif tlacitko == 27:
                        self.button27.config(background="white")
                    elif tlacitko == 28:
                        self.button28.config(background="white")
                    elif tlacitko == 29:
                        self.button29.config(background="white")
                    elif tlacitko == 30:
                        self.button30.config(background="white")
                    elif tlacitko == 31:
                        self.button31.config(background="white")
                    elif tlacitko == 32:
                        self.button32.config(background="white")
                    elif tlacitko == 33:
                        self.button33.config(background="white")
                    elif tlacitko == 34:
                        self.button34.config(background="white")
                    elif tlacitko == 35:
                        self.button35.config(background="white")
                    elif tlacitko == 36:
                        self.button36.config(background="white")
                self.pexeso.obr = []
                self.pexeso.c_tlacitka = []
                tk.messagebox.showwarning("SUPER", "Výborně, hraješ ještě jednou.")
                if self.pexeso.hr_c == 1:
                    self.pexeso.score_1 += 1
                    self.skore1.config(text=self.pexeso.score_1)
                elif self.pexeso.hr_c == 2:
                    self.pexeso.score_2 += 1
                    self.skore2.config(text=self.pexeso.score_2)


                if self.pexeso.score_1 + self.pexeso.score_2 == 18:
                    self.auta.config(state=NORMAL)
                    self.znacky.config(state=NORMAL)
                    self.kytky.config(state=NORMAL)
                    self.barvy.config(state=NORMAL)
                    self.button1.config(state=NORMAL, background="grey")
                    self.button2.config(state=NORMAL, background="grey")
                    self.button3.config(state=NORMAL, background="grey")
                    self.button4.config(state=NORMAL, background="grey")
                    self.button5.config(state=NORMAL, background="grey")
                    self.button6.config(state=NORMAL, background="grey")
                    self.button7.config(state=NORMAL, background="grey")
                    self.button8.config(state=NORMAL, background="grey")
                    self.button9.config(state=NORMAL, background="grey")
                    self.button10.config(state=NORMAL, background="grey")
                    self.button11.config(state=NORMAL, background="grey")
                    self.button12.config(state=NORMAL, background="grey")
                    self.button13.config(state=NORMAL, background="grey")
                    self.button14.config(state=NORMAL, background="grey")
                    self.button15.config(state=NORMAL, background="grey")
                    self.button16.config(state=NORMAL, background="grey")
                    self.button17.config(state=NORMAL, background="grey")
                    self.button18.config(state=NORMAL, background="grey")
                    self.button19.config(state=NORMAL, background="grey")
                    self.button20.config(state=NORMAL, background="grey")
                    self.button21.config(state=NORMAL, background="grey")
                    self.button22.config(state=NORMAL, background="grey")
                    self.button23.config(state=NORMAL, background="grey")
                    self.button24.config(state=NORMAL, background="grey")
                    self.button25.config(state=NORMAL, background="grey")
                    self.button26.config(state=NORMAL, background="grey")
                    self.button27.config(state=NORMAL, background="grey")
                    self.button28.config(state=NORMAL, background="grey")
                    self.button29.config(state=NORMAL, background="grey")
                    self.button30.config(state=NORMAL, background="grey")
                    self.button31.config(state=NORMAL, background="grey")
                    self.button32.config(state=NORMAL, background="grey")
                    self.button33.config(state=NORMAL, background="grey")
                    self.button34.config(state=NORMAL, background="grey")
                    self.button35.config(state=NORMAL, background="grey")
                    self.button36.config(state=NORMAL, background="grey")
                else:
                    pass

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
                self.pexeso.c_tlacitka = []
                if self.pexeso.hr_c == 1:
                    self.skore1.config(background="white")
                    self.skore2.config(background="blue")
                    self.pexeso.hr_c = 2
                elif self.pexeso.hr_c == 2:
                    self.skore1.config(background="blue")
                    self.skore2.config(background="white")
                    self.pexeso.hr_c = 1
        except IndexError:
            pass

        
    def auta(self):
        ...
        """
        self.pexeso.volba = ""
        self.pexeso.volba = "Auta"
        if self.pexeso.zamichat(self.pexeso.cesta, self.pexeso.volba) == True:
            self.auta.config(state=DISABLED)
            self.znacky.config(state=DISABLED)
            self.kytky.config(state=DISABLED)
            self.barvy.config(state=DISABLED)
        else:
            pass
"""

    def znacky(self):
        self.pexeso.volba = ""
        self.pexeso.volba = "Znacky"
        if self.pexeso.zamichat(self.pexeso.cesta, self.pexeso.volba) == True:
            self.auta.config(state=DISABLED)
            self.znacky.config(state=DISABLED)
            self.kytky.config(state=DISABLED)
            self.barvy.config(state=DISABLED)
        else:
            pass

    def kytky(self):
        ...
        """
        self.pexeso.volba = ""
        self.pexeso.volba = "Kytky"
        if self.pexeso.zamichat(self.pexeso.cesta, self.pexeso.volba) == True:
            self.auta.config(state=DISABLED)
            self.znacky.config(state=DISABLED)
            self.kytky.config(state=DISABLED)
            self.barvy.config(state=DISABLED)
        else:
            pass
        """

    def barvy(self):
        self.pexeso.volba = ""
        self.pexeso.volba = "Barvy"
        if self.pexeso.zamichat(self.pexeso.cesta, self.pexeso.volba) == True:
            self.auta.config(state=DISABLED)
            self.znacky.config(state=DISABLED)
            self.kytky.config(state=DISABLED)
            self.barvy.config(state=DISABLED)
        else:
            pass

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
            self.pexeso.c_tlacitka.append(2)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button2.config(background="blue")
            self.pexeso.obr.append(self.pexeso.obrazky[1]) # přespsat o číslo více
            self.button2.config(state=DISABLED)
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[1]) # přespsat o číslo více
            self.pexeso.c_tlacitka.append(2) # v závorce je číslo tlačítka

    def T3(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button3.config(background="blue") # přepsat číslo tlačítka
            self.button3.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[2]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[2]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(3)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button3.config(background="blue") # přepsat číslo tlačítka
            self.button3.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[2]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[2]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(3)  # v závorce je číslo tlačítka
        
    def T4(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button4.config(background="blue") # přepsat číslo tlačítka
            self.button4.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[3]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[3]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(4)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button4.config(background="blue") # přepsat číslo tlačítka
            self.button4.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[3]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[3]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(4)  # v závorce je číslo tlačítka
       
    def T5(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button5.config(background="blue") # přepsat číslo tlačítka
            self.button5.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[4]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[4]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(5)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button5.config(background="blue") # přepsat číslo tlačítka
            self.button5.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[4]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[4]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(5)  # v závorce je číslo tlačítka
       
    def T6(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button6.config(background="blue") # přepsat číslo tlačítka
            self.button6.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[5]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[5]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(6)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button6.config(background="blue") # přepsat číslo tlačítka
            self.button6.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[5]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[5]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(6)  # v závorce je číslo tlačítka
        
    def T7(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button7.config(background="blue") # přepsat číslo tlačítka
            self.button7.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[6]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[6]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(7)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button7.config(background="blue") # přepsat číslo tlačítka
            self.button7.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[6]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[6]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(7)  # v závorce je číslo tlačítka
        
    def T8(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button8.config(background="blue") # přepsat číslo tlačítka
            self.button8.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[7]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[7]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(8)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button8.config(background="blue") # přepsat číslo tlačítka
            self.button8.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[7]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[7]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(8)  # v závorce je číslo tlačítka
       
    def T9(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button9.config(background="blue") # přepsat číslo tlačítka
            self.button9.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[8]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[8]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(9)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button9.config(background="blue") # přepsat číslo tlačítka
            self.button9.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[8]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[8]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(9)  # v závorce je číslo tlačítka
       
    def T10(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button10.config(background="blue") # přepsat číslo tlačítka
            self.button10.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[9]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[9]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(10)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button10.config(background="blue") # přepsat číslo tlačítka
            self.button10.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[9]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[9]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(10)  # v závorce je číslo tlačítka
        
    def T11(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button11.config(background="blue") # přepsat číslo tlačítka
            self.button11.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[10]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[10]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(11)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button11.config(background="blue") # přepsat číslo tlačítka
            self.button11.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[10]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[10]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(11)  # v závorce je číslo tlačítka
        
    def T12(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button12.config(background="blue") # přepsat číslo tlačítka
            self.button12.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[11]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[11]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(12)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button12.config(background="blue") # přepsat číslo tlačítka
            self.button12.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[11]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[11]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(12)  # v závorce je číslo tlačítka
        
    def T13(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button13.config(background="blue") # přepsat číslo tlačítka
            self.button13.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[12]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[12]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(13)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button13.config(background="blue") # přepsat číslo tlačítka
            self.button13.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[12]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[12]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(13)  # v závorce je číslo tlačítka
        
    def T14(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button14.config(background="blue") # přepsat číslo tlačítka
            self.button14.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[13]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[13]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(14)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button14.config(background="blue") # přepsat číslo tlačítka
            self.button14.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[13]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[13]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(14)  # v závorce je číslo tlačítka
        
    def T15(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button15.config(background="blue") # přepsat číslo tlačítka
            self.button15.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[14]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[14]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(15)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button15.config(background="blue") # přepsat číslo tlačítka
            self.button15.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[14]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[14]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(15)  # v závorce je číslo tlačítka
       
    def T16(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button16.config(background="blue") # přepsat číslo tlačítka
            self.button16.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[15]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[15]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(16)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button16.config(background="blue") # přepsat číslo tlačítka
            self.button16.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[15]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[15]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(16)  # v závorce je číslo tlačítka
       
    def T17(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button17.config(background="blue") # přepsat číslo tlačítka
            self.button17.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[16]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[16]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(17)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button17.config(background="blue") # přepsat číslo tlačítka
            self.button17.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[16]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[16]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(17)  # v závorce je číslo tlačítka
       
    def T18(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button18.config(background="blue") # přepsat číslo tlačítka
            self.button18.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[17]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[17]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(18)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button18.config(background="blue") # přepsat číslo tlačítka
            self.button18.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[17]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[17]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(18)  # v závorce je číslo tlačítka
        
    def T19(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button19.config(background="blue") # přepsat číslo tlačítka
            self.button19.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[18]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[18]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(19)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button19.config(background="blue") # přepsat číslo tlačítka
            self.button19.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[18]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[18]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(19)  # v závorce je číslo tlačítka
        
    def T20(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button20.config(background="blue") # přepsat číslo tlačítka
            self.button20.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[19]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[19]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(20)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button20.config(background="blue") # přepsat číslo tlačítka
            self.button20.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[19]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[19]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(20)  # v závorce je číslo tlačítka
        
    def T21(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button21.config(background="blue") # přepsat číslo tlačítka
            self.button21.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[20]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[20]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(21)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button21.config(background="blue") # přepsat číslo tlačítka
            self.button21.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[20]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[20]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(21)  # v závorce je číslo tlačítka
        
    def T22(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button22.config(background="blue") # přepsat číslo tlačítka
            self.button22.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[21]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[21]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(22)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button22.config(background="blue") # přepsat číslo tlačítka
            self.button22.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[21]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[21]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(22)  # v závorce je číslo tlačítka
        
    def T23(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button23.config(background="blue") # přepsat číslo tlačítka
            self.button23.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[22]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[22]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(23)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button23.config(background="blue") # přepsat číslo tlačítka
            self.button23.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[22]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[22]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(23)  # v závorce je číslo tlačítka
        
    def T24(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button24.config(background="blue") # přepsat číslo tlačítka
            self.button24.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[23]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[23]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(24)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button24.config(background="blue") # přepsat číslo tlačítka
            self.button24.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[23]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[23]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(24)  # v závorce je číslo tlačítka
        
    def T25(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button25.config(background="blue") # přepsat číslo tlačítka
            self.button25.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[24]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[24]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(25)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button25.config(background="blue") # přepsat číslo tlačítka
            self.button25.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[24]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[24]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(25)  # v závorce je číslo tlačítka
        
    def T26(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button26.config(background="blue") # přepsat číslo tlačítka
            self.button26.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[25]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[25]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(26)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button26.config(background="blue") # přepsat číslo tlačítka
            self.button26.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[25]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[25]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(26)  # v závorce je číslo tlačítka
        
    def T27(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button27.config(background="blue") # přepsat číslo tlačítka
            self.button27.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[26]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[26]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(27)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button27.config(background="blue") # přepsat číslo tlačítka
            self.button27.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[26]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[26]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(27)  # v závorce je číslo tlačítka
        
    def T28(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button28.config(background="blue") # přepsat číslo tlačítka
            self.button28.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[27]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[27]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(28)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button28.config(background="blue") # přepsat číslo tlačítka
            self.button28.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[27]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[27]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(28)  # v závorce je číslo tlačítka
        
    def T29(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button29.config(background="blue") # přepsat číslo tlačítka
            self.button29.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[28]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[28]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(29)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button29.config(background="blue") # přepsat číslo tlačítka
            self.button29.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[28]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[28]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(29)  # v závorce je číslo tlačítka
        
    def T30(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button30.config(background="blue") # přepsat číslo tlačítka
            self.button30.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[29]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[29]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(30)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button30.config(background="blue") # přepsat číslo tlačítka
            self.button30.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[29]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[29]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(30)  # v závorce je číslo tlačítka
        
    def T31(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button31.config(background="blue") # přepsat číslo tlačítka
            self.button31.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[30]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[30]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(31)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button31.config(background="blue") # přepsat číslo tlačítka
            self.button31.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[30]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[30]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(31)  # v závorce je číslo tlačítka
        
    def T32(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button32.config(background="blue") # přepsat číslo tlačítka
            self.button32.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[31]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[31]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(32)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button32.config(background="blue") # přepsat číslo tlačítka
            self.button32.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[31]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[31]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(32)  # v závorce je číslo tlačítka
        
    def T33(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button33.config(background="blue") # přepsat číslo tlačítka
            self.button33.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[32]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[32]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(33)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button33.config(background="blue") # přepsat číslo tlačítka
            self.button33.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[32]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[32]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(33)  # v závorce je číslo tlačítka
       
    def T34(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button34.config(background="blue") # přepsat číslo tlačítka
            self.button34.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[33]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[33]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(34)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button34.config(background="blue") # přepsat číslo tlačítka
            self.button34.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[33]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[33]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(34)  # v závorce je číslo tlačítka
       
    def T35(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button35.config(background="blue") # přepsat číslo tlačítka
            self.button35.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[34]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[34]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(35)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button35.config(background="blue") # přepsat číslo tlačítka
            self.button35.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[34]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[34]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(35)  # v závorce je číslo tlačítka
        
    def T36(self):
        if self.pexeso.obrazky == []:
            tk.messagebox.showwarning("Error", "Nejprve vyber hrací karty.")
            return
        if len(self.pexeso.obr) == 0:
            self.button36.config(background="blue") # přepsat číslo tlačítka
            self.button36.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[35]) # v závorce je č tlačítka-1
            self.obrazek1.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[35]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(36)  # v závorce je číslo tlačítka
        elif len(self.pexeso.obr) == 1:
            self.button36.config(background="blue") # přepsat číslo tlačítka
            self.button36.config(state=DISABLED) # přepsat číslo tlačítka
            self.pexeso.obr.append(self.pexeso.obrazky[35]) # v závorce je č tlačítka-1
            self.obrazek2.config(file=self.pexeso.cesta + self.pexeso.volba + "/" + self.pexeso.obrazky[35]) # v závorce je č tlačítka-1
            self.pexeso.c_tlacitka.append(36)  # v závorce je číslo tlačítka
        

    def on_close(self):
       self.parent.destroy()

 
if __name__ == '__main__':
    root = tk.Tk()
    pexeso = pexeso()
    app = pexesoGUI(root, pexeso)
    app.mainloop()