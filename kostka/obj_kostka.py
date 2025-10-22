#!/usr/bin/env python3

import random

class Kostka:
    def __init__(self, pocet_sten):
        self.pocet_sten = pocet_sten

    def hod(self):
        return random.randint(1,self.pocet_sten)

def main():
    k1 = Kostka(6)
    k2 = Kostka(12)
    print(k1.hod())
    print(k2.hod())

if __name__ == '__main__':
    main()