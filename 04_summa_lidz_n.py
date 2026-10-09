ievade = input("Ievadi pozitīvu veselu skaitli: ")

if ievade.strip() == "":
    print("Kļūda: tu neievadīji skaitli.")
elif not ievade.isdigit():
    print("Kļūda: jāievada vesels skaitlis.")
else:
    n = int(ievade)

    if n <= 0:
        print("Kļūda: skaitlim jābūt lielākam par 0.")
    else:
        summa = 0

        for i in range(1, n + 1):
            summa = summa + i

        print(f"Summa ir {summa}")