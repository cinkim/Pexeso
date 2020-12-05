import random

import tkinter as tk
from tkinter import NORMAL, CENTER, LEFT, NO, NORMAL, W, E, N, S, StringVar, ttk, DISABLED
from time import sleep
# import tkinter.messagebox



class pexeso:

    def __init__(self):
        self.obrazky = ["1.jpg", "1.jpg", "2.jpg", "2.jpg", "3.jpg", "3.jpg", 
                        "4.jpg", "4.jpg", "5.jpg", "5.jpg", "6.jpg", "6.jpg", 
                        "7.jpg", "7.jpg", "8.jpg", "8.jpg", "9.jpg", "9.jpg",
                        "10.jpg", "10.jpg", "11.jpg", "11.jpg", "12.jpg", "12.jpg",
                        "13.jpg", "13.jpg", "14.jpg", "14.jpg", "15.jpg", "15.jpg",
                        "16.jpg", "16.jpg", "17.jpg", "17.jpg", "18.jpg", "18.jpg"]
        # self.cesta = "D:/Python/Projekty_Python/Pex/"
        self.zamichat(self.obrazky)
        self.sedy_obrazek = ""
        self.obr = []


    def zamichat(self, obrazky):
        # funguje
        for zamichat in range(1001):
            random.shuffle(obrazky)
        print(self.obrazky)
        self.obrazky = obrazky

    def schovat_obrazky(self):
        ...

    def otoc_kartu(self, volba):
        ...


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
        self.button1 = tk.Button(text="1", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T1)
        self.button1.grid(row=0, column=0)
        self.button2 = tk.Button(text="2", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T2)
        self.button2.grid(row=0, column=1)
        self.button3 = tk.Button(text="3", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T3)
        self.button3.grid(row=0, column=2)
        self.button4 = tk.Button(text="4", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T4)
        self.button4.grid(row=0, column=3)
        self.button5 = tk.Button(text="5", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T5)
        self.button5.grid(row=0, column=4)
        self.button6 = tk.Button(text="6", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T6)
        self.button6.grid(row=0, column=5)
        """
        self.obrazek1 = tk.PhotoImage(file="")
        self.image1 = tk.Label(image=self.obrazek1)
        self.image1.grid(row=0, column=7)
        """
        self.button7 = tk.Button(text="7", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T7)
        self.button7.grid(row=1, column=0)
        self.button8 = tk.Button(text="8", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T8)
        self.button8.grid(row=1, column=1)
        self.button9 = tk.Button(text="9", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T9)
        self.button9.grid(row=1, column=2)
        self.button10 = tk.Button(text="10", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T10)
        self.button10.grid(row=1, column=3)
        self.button11 = tk.Button(text="11", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T11)
        self.button11.grid(row=1, column=4)
        self.button12 = tk.Button(text="12", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T12)
        self.button12.grid(row=1, column=5)
        self.skore1 = tk.Label(text="6", font="Arial 40", padx=90, pady=self.vyska)
        self.skore1.grid(row=1, column=7)

        self.button13 = tk.Button(text="13", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T13)
        self.button13.grid(row=2, column=0)
        self.button14 = tk.Button(text="14", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T14)
        self.button14.grid(row=2, column=1)
        self.button15 = tk.Button(text="15", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T15)
        self.button15.grid(row=2, column=2)
        self.button16 = tk.Button(text="16", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T16)
        self.button16.grid(row=2, column=3)
        self.button17 = tk.Button(text="17", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T17)
        self.button17.grid(row=2, column=4)
        self.button18 = tk.Button(text="18", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T18)
        self.button18.grid(row=2, column=5)
        self.hrat_znovu = tk.Button(text="Hrát znovu",font="Arial 15", width=self.sirka, state=NORMAL, height=self.vyska, command=self.hrat_znovu, background="yellow")
        self.hrat_znovu.grid(row=2, column=7, rowspan=2, sticky=N+W+E+S)

        self.button19 = tk.Button(text="19", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T19)
        self.button19.grid(row=3, column=0)
        self.button20 = tk.Button(text="20", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T20)
        self.button20.grid(row=3, column=1)
        self.button21 = tk.Button(text="21", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T21)
        self.button21.grid(row=3, column=2)
        self.button22 = tk.Button(text="22", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T22)
        self.button22.grid(row=3, column=3)
        self.button23 = tk.Button(text="23", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T23)
        self.button23.grid(row=3, column=4)
        self.button24 = tk.Button(text="24", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T24)
        self.button24.grid(row=3, column=5)

        self.button25 = tk.Button(text="25", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T25)
        self.button25.grid(row=4, column=0)
        self.button26 = tk.Button(text="26", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T26)
        self.button26.grid(row=4, column=1)
        self.button27 = tk.Button(text="27", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T27)
        self.button27.grid(row=4, column=2)
        self.button28 = tk.Button(text="28", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T28)
        self.button28.grid(row=4, column=3)
        self.button29 = tk.Button(text="29", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T29)
        self.button29.grid(row=4, column=4)
        self.button30 = tk.Button(text="30",width=self.sirka, state=NORMAL, height=self.vyska, command=self.T30)
        self.button30.grid(row=4, column=5)
        self.skore2 = tk.Label(text="4", font="Arial 40", padx=90, pady=self.vyska)
        self.skore2.grid(row=4, column=7)

        self.button31 = tk.Button(text="31", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T31)
        self.button31.grid(row=5, column=0)
        self.button32 = tk.Button(text="32", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T32)
        self.button32.grid(row=5, column=1)
        self.button33 = tk.Button(text="33", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T33)
        self.button33.grid(row=5, column=2)
        self.button34 = tk.Button(text="34", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T34)
        self.button34.grid(row=5, column=3)
        self.button35 = tk.Button(text="35", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T35)
        self.button35.grid(row=5, column=4)
        self.button36 = tk.Button(text="36", width=self.sirka, state=NORMAL, height=self.vyska, command=self.T36)
        self.button36.grid(row=5, column=5)
        """
        self.obrazek2 = tk.PhotoImage(file="")
        self.image2 = tk.Label(image=self.obrazek2)
        self.image2.grid(row=5, column=7)
        """


    def hrat_znovu(self):
        ...

    def T1(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[0])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[0])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button1.config(background="green")
                self.button1.config(state=DISABLED)
            else:
                pass


    def T2(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[1])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[1])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button2.config(background="green")
                self.button2.config(state=DISABLED)
            else:
                pass

    def T3(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[2])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[2])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button3.config(background="green")
                self.button3.config(state=DISABLED)
            else:
                pass

    def T4(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[3])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[3])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button4.config(background="green")
                self.button4.config(state=DISABLED)
            else:
                pass

    def T5(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[4])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[4])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button5.config(background="green")
                self.button5.config(state=DISABLED)
            else:
                pass

    def T6(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[5])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[5])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button6.config(background="green")
                self.button6.config(state=DISABLED)
            else:
                pass

    def T7(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[6])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[6])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button7.config(background="green")
                self.button7.config(state=DISABLED)
            else:
                pass

    def T8(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[7])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[7])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button8.config(background="green")
                self.button8.config(state=DISABLED)
            else:
                pass

    def T9(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[8])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[8])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button9.config(background="green")
                self.button9.config(state=DISABLED)
            else:
                pass

    def T10(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[9])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[9])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button10.config(background="green")
                self.button10.config(state=DISABLED)
            else:
                pass

    def T11(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[10])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[10])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button11.config(background="green")
                self.button11.config(state=DISABLED)
            else:
                pass

    def T12(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[11])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[11])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button12.config(background="green")
                self.button12.config(state=DISABLED)
            else:
                pass

    def T13(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[12])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[12])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button13.config(background="green")
                self.button13.config(state=DISABLED)
            else:
                pass

    def T14(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[13])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[13])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button14.config(background="green")
                self.button14.config(state=DISABLED)
            else:
                pass

    def T15(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[14])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[14])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button15.config(background="green")
                self.button15.config(state=DISABLED)
            else:
                pass

    def T16(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[15])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[15])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button16.config(background="green")
                self.button16.config(state=DISABLED)
            else:
                pass

    def T17(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[16])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[16])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button17.config(background="green")
                self.button17.config(state=DISABLED)
            else:
                pass

    def T18(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[17])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[17])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button18.config(background="green")
                self.button18.config(state=DISABLED)
            else:
                pass

    def T19(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[18])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[18])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button19.config(background="green")
                self.button19.config(state=DISABLED)
            else:
                pass

    def T20(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[19])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[19])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button20.config(background="green")
                self.button20.config(state=DISABLED)
            else:
                pass

    def T21(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[20])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[20])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button21.config(background="green")
                self.button21.config(state=DISABLED)
            else:
                pass

    def T22(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[21])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[21])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button22.config(background="green")
                self.button22.config(state=DISABLED)
            else:
                pass

    def T23(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[22])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[22])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button23.config(background="green")
                self.button23.config(state=DISABLED)
            else:
                pass

    def T24(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[23])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[23])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button24.config(background="green")
                self.button24.config(state=DISABLED)
            else:
                pass

    def T25(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[24])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[24])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button25.config(background="green")
                self.button25.config(state=DISABLED)
            else:
                pass

    def T26(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[25])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[25])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button26.config(background="green")
                self.button26.config(state=DISABLED)
            else:
                pass

    def T27(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[26])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[26])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button27.config(background="green")
                self.button27.config(state=DISABLED)
            else:
                pass

    def T28(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[27])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[27])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button28.config(background="green")
                self.button28.config(state=DISABLED)
            else:
                pass

    def T29(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[28])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[28])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button29.config(background="green")
                self.button29.config(state=DISABLED)
            else:
                pass

    def T30(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[29])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[29])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button30.config(background="green")
                self.button30.config(state=DISABLED)
            else:
                pass

    def T31(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[30])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[30])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button31.config(background="green")
                self.button31.config(state=DISABLED)
            else:
                pass

    def T32(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[31])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[31])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button32.config(background="green")
                self.button32.config(state=DISABLED)
            else:
                pass

    def T33(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[32])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[32])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button33.config(background="green")
                self.button33.config(state=DISABLED)
            else:
                pass

    def T34(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[33])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[33])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button34.config(background="green")
                self.button34.config(state=DISABLED)
            else:
                pass

    def T35(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[34])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[34])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button35.config(background="green")
                self.button35.config(state=DISABLED)
            else:
                pass

    def T36(self):
        if len(self.pexeso.obr) == 0:
            self.pexeso.obr.append(self.pexeso.obrazky[35])
            print(self.pexeso.obr)
        elif len(self.pexeso.obr) == 1:
            self.pexeso.obr.append(self.pexeso.obrazky[35])
            # tady budeme pokračovat
            print(self.pexeso.obr)
            if self.pexeso.obr[0] == self.pexeso.obr[1]: # v případě shody zablokuje zlačítko
                self.button36.config(background="green")
                self.button36.config(state=DISABLED)
            else:
                pass

    def on_close(self):
       self.parent.destroy()


    
if __name__ == '__main__':
    root = tk.Tk()
    pexeso = pexeso()
    app = pexesoGUI(root, pexeso)
    app.mainloop()