
try:
    skaits = int(input("Cik skaitļus ievadīsi? "))

    if skaits <= 0:
        print("Kļūda: skaitļu skaitam jābūt lielākam par 0.")

    else:
        summa = 0
        pozitivie = 0
        negativie = 0
        nulles = 0
        para = 0
        nepara = 0

        for i in range(skaits):
            while True:
                try:
                    skaitlis = int(input(f"Ievadi {i + 1}. skaitli: "))
                    break
                except ValueError:
                    print("Kļūda! Ievadi veselu skaitli, piemēram, 12.")

            summa = summa + skaitlis

            if skaitlis > 0:
                pozitivie = pozitivie + 1
            elif skaitlis < 0:
                negativie = negativie + 1
            else:
                nulles = nulles + 1

            if skaitlis % 2 == 0:
                para = para + 1
            else:
                nepara = nepara + 1

        videjais = summa / skaits

        print("\n--- Rezultāti ---")
        print(f"Summa: {summa}")
        print(f"Pozitīvo skaitļu skaits: {pozitivie}")
        print(f"Negatīvo skaitļu skaits: {negativie}")
        print(f"Nulles skaits: {nulles}")
        print(f"Pāra skaitļu skaits: {para}")
        print(f"Nepāra skaitļu skaits: {nepara}")
        print(f"Vidējais aritmētiskais: {videjais:.2f}")

except ValueError:
    print("Kļūda: skaitļu skaitam jābūt veselam skaitlim.")