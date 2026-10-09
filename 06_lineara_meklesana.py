
skaitli = [4, 7, 2, 9, 7, 1]

try:
    meklejamais = int(input("Kādu skaitli meklēt? "))

    atrastie_indeksi = []

    for i in range(len(skaitli)):
        if skaitli[i] == meklejamais:
            atrastie_indeksi.append(i)

    if len(atrastie_indeksi) > 0:
        print(f"Pirmais indekss: {atrastie_indeksi[0]}")
        print(f"Visi atrastie indeksi: {atrastie_indeksi}")
    else:
        print("Nav atrasts")

except ValueError:
    print("Kļūda: ievadi veselu skaitli!")