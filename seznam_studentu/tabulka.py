print("Vítejte ve správci studentů :)")
#nacist a zapsat do csv
#pridat radek do tabulky 
#!/usr/bin/env python3

filename = "database.csv"

def read_csv(filename):
    with open(csv_file, newline='', encoding="utf-8") as csvfile:
        lines = csvfile.readlines()
    for line in lines:
        print(line.strip().split(","))

def zapis(filename):
    seznam = []
    seznam.append(input("Zadejte jméno: "))
    seznam.append(input("Zadejte příjmení: "))
    seznam.append(input("Zadejte třídu: "))
    seznam.append(input("Zadejte rok narození: "))
    record = ",".join(seznam) + "\n"
    with open(filename, "a") as f:          
        f.write(record)
    print("Záznam byl přidán.")

def list_all(filename):
    print("\n--- Seznam studentů ---")
    try:
        with open(filename) as csvfile:
            lines = csvfile.readlines()
            if not lines:
                print("Žádná data v tabulce.")
                return
            for line in lines:
                print(line.strip().split(","))
    except FileNotFoundError:
        print("Soubor zatím neexistuje. Nejprve zapište nějaká data.")

def main(filename):
    while True:
        print("1 - nacteni")
        print("2 - zapis")
        print("3 - list all")
        print("4 - konec")
        try:
            choice = int(input("Zadejte volbu: "))
        except ValueError:
            print("Neplatná volba.")
            continue
        if choice == 4:
            print("Konec programu.")
            break
        if choice == 3:
            list_all(filename)
        elif choice == 2:
            zapis(filename)
        elif choice == 1:
            read_csv(filename)
        else:
            print("Neplatná volba.")

if __name__ == "__main__":
    main(filename)




