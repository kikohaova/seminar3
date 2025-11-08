#!/usr/bin/env python3

from kostka import Kostka
from lod import Lod

class Sektor:
    '''
    Sprava souboje
    '''

    def __init__(self, jmeno, lod_1, lod_2, kostka):
        self._jmeno = jmeno
        self._lod_1 = lod_1
        self._lod_2 = lod_2
        self._kostka = kostka
    
    def _vypis_lod(self,lod):
        print(lod)
        print(f'Trup: {lod.graficky_trup(lod._trup, lod._max_trup)}')
    
    def _graficky_trup(self):
        pass



    def souboj(self):
        import random
        print(f'Vitej v sektoru {self._jmeno}!')
        print(f'======================{len(self._jmeno)*"="}=')
        print()
        print(f'Dnes se stretnou {self._lod_1} a {self._lod_2}')
        print('Zahajit souboj...')
        input()

        if random.randint(0, 1):
            self._lod_1, self._lod_2 = self._lod_2, self._lod_1



        while self._lod_1.je_operacni() and self._lod_2.je_operacni():
            self._lod_1.utoc(self._lod_2)
            self._vykresli()
            self._vypis_zpravu(self._lod_1.vypis_zpravu())
            self._vypis_zpravu(self._lod_2.vypis_zpravu())
            self._vypis_lod(self._lod_2)
            
            if self._lod_2.je_operacni():
                self._lod_2.utoc(self._lod_1)
                self._vykresli()
                self._vypis_zpravu(self._lod_2.vypis_zpravu())
                self._vypis_zpravu(self._lod_1.vypis_zpravu())
                self._vypis_lod(self._lod_1)

    def _vypis_zpravu(self, zprava):
        import time as _time
        if zprava:
            print(zprava)
            _time.sleep(0.5)


    def _vycisti(self):
        import sys as _sys
        import subprocess as _subprocess
        if _sys.platform.startswith('win'):
            _subprocess.call(['cmd.exe', '/C', 'cls'])
        else:
            _subprocess.call(['clear'])

    def _vykresli(self):
        self._vycisti()
        print(f'==================== Sektor {self._jmeno} ====================')
        print('Lode:\n')
        self._vypis_lod(self._lod_1)
        self._vypis_lod(self._lod_2)
        print()



if __name__ == '__main__':
    k = Kostka(10)
    lod1 = Lod('Ajax', 100, 20, 18, k)
    lod2 = Lod('Barracuda', 100, 15, 22, k)
    orion = Sektor("Orion", lod1, lod2, k)
    m = Sektor("Orion", lod1, lod2, k)
    orion.souboj()
