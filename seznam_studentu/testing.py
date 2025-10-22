print("Hello, World!")
#!/usr/bin/env python3

filename = "studenti.csv"

def read_csv(csv_file):
    with open(csv_file, newline='', encoding="utf-8") as csvfile:
        lines = csvfile.readlines()
    for line in lines:
        print(line.strip().split(","))

def zapis(csv_file):
    seznam = []
    seznam.append(input("Zadejte jmeno: "))
    seznam.append(input("Zadejte prijmeni: "))
    seznam.append(input("Zadejte tridu: "))
    seznam.append(input("Zadejte rok narozeni: "))
    record = ",".join(seznam) + "\n"
    with open(csv_file, "a", newline='', encoding="utf-8") as csvfile:
        csvfile.write(record)

def main(filename):
    while True:
        print("1 - nacteni")
        print("2 - zapis")
        print("3 - konec")
        try:
            choice = int(input("Zadejte volbu: "))
        except ValueError:
            print("Neplatná volba.")
            continue
        if choice == 3:
            print("Konec programu.")
            break
        elif choice == 2:
            zapis(filename)
        elif choice == 1:
            read_csv(filename)
        else:
            print("Neplatná volba.")

if __name__ == "__main__":
    main(filename)


