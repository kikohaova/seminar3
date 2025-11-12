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
    
    def graficky_ukazatel(self, aktualni, maximalni):
        celkem = 20
        pocet = int(aktualni / maximalni * celkem)
        if pocet == 0 and self.je_operacni():
            pocet = 1
        return f'[{"#"*pocet}{" "*(celkem-pocet)}]'
    
    def graficky_trup(self, trup, max_trup):
        return self.graficky_ukazatel(self._trup, self._max_trup)

    def je_operacni(self):
        return self._trup > 0

    def nastav_zpravu(self, zprava):
        self._zprava = zprava
        
    def vypis_zpravu(self):
        return self._zprava
    

class Stihac(Lod):
    '''
    Odvozená třída, která přidává energii pro laserový boj.
    Demonstruje dědičnost, polymorfismus a overriding (přepis metody).
    '''
    def __init__(self, jmeno, trup, utok, stit, kostka, energie, laserovy_utok):
        super().__init__(jmeno, trup, utok, stit, kostka)
        self._energie = energie
        self._max_energie = energie
        self._laserovy_utok = laserovy_utok

    def utoc(self, souper):
        if self._energie < self._max_energie:
            self._energie = min(self._max_energie, self._energie + 10)
            super().utoc(souper)
        else:
            uder = self._laserovy_utok + self._kostka.hod()
            zprava = f'{self._jmeno} vypalil laser za {uder} hp'
            self._energie = 0
            souper.bran_se(uder)
    
    def graficka_energie(self):
        return self.graficky_ukazatel(self._energie, self._max_energie)


class Korveta(Lod):
        
    def bran_se(self, uder):
        poskozeni = uder - (self._stit + self._kostka.hod() + 2)
        if poskozeni > 0:
            self._trup -= poskozeni
            if self._trup < 0:
                self._trup = 0
            self._nastav_zpravu(f'{self._jmeno} byl poskozen o {poskozeni} hp trupu.')
        else:
            self._nastav_zpravu(f'{self._jmeno} zcela odrazila utok stity.')
            