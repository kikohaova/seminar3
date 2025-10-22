#!/usr/bin/env python3

from kostka import Kostka
from lod import Lod

class Sektor: 
    """
    Sprava souboje
    """

    def __init__(self, lod_1, lod_2, kostka):
        self._lod_1 = lod_1
        self._lod_2 = lod_2
        self._kostka = kostka

    def _vypis_lod(self, lod): # "_" znamena, ze je to metoda urcena pro vnitrni pouziti
        print(lod)
        print(f"Trup: {lod._trup} hp")

    def souboj(self):
        import random 
        print("Vite v sektoru Orion")
        print("====================")
        print()
        print(f"Dnes se stretnou lode {self._lod_1} a {self._lod_2}")
        print("Zahajit souboj...")
        input()

        while self._lod_1.je_operacni() and self._lod_2.je_operacni():
            self._lod_1.utoc(self._lod_2)
            self._vykresli()
            self._vypis_zpravu(self._lod_1.vypis_zpravu())
            self._vypis_zpravu(self._lod_2.vypis_zpravu())
            self._vypis_lod(self._lod_1)

            """if self._lod_2.je_operacni():
                self._lod_2.utoc(self._lod_1)
                self._vykresli()
                self._vypis_zpravu(self._lod_2.vypis_zpravu())
                self._vypis_zpravu(self._lod_1.vypis_zpravu())
                self._vypis_lod(self._lod_2)"""
            
            self._lod_2.utoc(self._lod_1)
            self._vykresli()
            self._vypis_zpravu(self._lod_2.vypis_zpravu())
            self._vypis_zpravu(self._lod_1.vypis_zpravu())
            self._vypis_lod(self._lod_2)



    def _vypis_zpravu(self, zprava):
        print(zprava)
        import time as _time
        if zprava:
            print(zprava)
            _time.sleep(0.5)


    def _vycisti(self):
        import sys as _sys
        import subprocess as _subprocess
        if _sys.platform.startswith('win'):
            _subprocess.call(['cls'])
        else:
            _subprocess.call(['clear'])

    def _vyresli(self):
        self._vycistit()
        print("============= Sektor Orion =============")
        print("Lode \n") #za ty Lode bude prazdny radek
        self._vypis_lod(self._lod_1)
        self._vypis_lod(self._lod_2)
        print()


if __name__ == "__main__":
    k = Kostka(20)
    lod1 = Lod('Ajax', 100, 20, 18, k)
    lod2 = Lod('Baracuda', 100, 15, 22, k)

    orion = Sektor(lod1, lod2, k)
    orion.souboj()

