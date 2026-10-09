
atlikums = 100
izvele = ""

while izvele != "4":
    print("\n--- MINI BANKOMĀTS ---")
    print("1 — Apskatīt atlikumu")
    print("2 — Iemaksāt naudu")
    print("3 — Izņemt naudu")
    print("4 — Beigt darbu")

    izvele = input("Izvēlies darbību: ")

    if izvele == "1":
        print(f"Atlikums: {atlikums} eiro")

    elif izvele == "2":
        try:
            iemaksa = int(input("Cik eiro vēlies iemaksāt? "))

            if iemaksa > 0:
                atlikums = atlikums + iemaksa
                print(f"Iemaksa veiksmīga! Jaunais atlikums: {atlikums} eiro")
            else:
                print("Kļūda! Iemaksai jābūt lielākai par 0.")

        except ValueError:
            print("Kļūda! Ievadi summu kā veselu skaitli.")

    elif izvele == "3":
        try:
            iznemsana = int(input("Cik eiro vēlies izņemt? "))

            if iznemsana <= 0:
                print("Kļūda! Izņemamajai summai jābūt lielākai par 0.")
            elif iznemsana > atlikums:
                print("Kļūda! Kontā nav pietiekami daudz naudas.")
            else:
                atlikums = atlikums - iznemsana
                print(f"Izņemšana veiksmīga! Atlikums: {atlikums} eiro")

        except ValueError:
            print("Kļūda! Ievadi summu kā veselu skaitli.")

    elif izvele == "4":
        print("Darbs pabeigts. Uz redzēšanos!")

    else:
        print("Kļūda! Izvēlies darbību no 1 līdz 4.")