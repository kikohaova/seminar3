#!/usr/bin/env python3

import sys
import argparse
from file import readcsv

def outline_args():
    
    p = argparse.ArgumentParser(description= __doc__, formatter_class=argparse.RawDescriptionHelpFormatter)

    # positional arguments – reliant on positions of each parameter, e.g.: argument, číslo, -T
    # nmap – nápověda, arguments listed 

    p.add_argument("-i", "--ifile", help="vstupní soubor")
    p.add_argument("-o", "--ofile", help="výstupní soubor")

    return p.parse_args()

def process_args():
    lines = readcsv(args.ifile)
    for line in lines:
        print(line)
    print(lines)

if __name__ == "__main__":

    if sys.version_info < (3, 6, 0):
        sys.stderr.write("You need Python 3.5 or later.\n")
        sys.exit(1)
    
    # zkouska
    #try:
    args = outline_args()
    process_args()
    #print(args)
    #except:
    #   print("Try main.py parameter -t")

    print()
    

