#!/usr/bin/env python3
'''
Lod a odvozene tridy pro vesmirny souboj.
'''

class Lod:
    '''
    Zakladni trida reprezentujici lod.
    '''
    def __init__(self, jmeno, trup, utok, stit, kostka):
        self._jmeno = jmeno
        self._trup = trup
        self._max_trup = trup
        self._utok = utok
        self._stit = stit
        self._kostka = kostka
        self._zprava = ''
    
    def __str__(self):
        return str(self._jmeno)
    

    def utoc(self, souper):
        uder = self._utok + self._kostka.hod()
        zprava = f'{self._jmeno} pali kanony za {uder} hp'
        self.nastav_zpravu(zprava)
        souper.bran_se(uder)
    


    def bran_se(self, uder):
        poskozeni = uder - (self._stit + self._kostka.hod())
        if poskozeni > 0:
            zprava = f'{self._jmeno} byl poskozen o {poskozeni} hp trupu.'
            self._trup -= poskozeni
            if self._trup < 0:
                self._trup = 0
                zprava = f'{zprava [:-1]} a byla znicena'
        else:
            zprava = f'{self._jmeno} odrazila utok stity.'
        self.nastav_zpravu(zprava)
    
    def graficky_trup(self, trup, max_trup):
        celkem = 20
        pocet = int(trup / max_trup * celkem)
        if pocet == 0 and self.je_operacni():
            pocet = 1
        return f'[{"#"*pocet}{" "*(celkem-pocet)}]'




    def je_operacni(self):
        return self._trup > 0

    def nastav_zpravu(self, zprava):
        self._zprava = zprava
        
    def vypis_zpravu(self):
        return self._zprava