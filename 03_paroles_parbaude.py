pareiza_parole = "JanisValorants"
meginajumi = 0
max_meiginajumi = 3
ievadita_parole = ""

while ievadita_parole != pareiza_parole and meginajumi < max_meiginajumi:
    ievadita_parole = input("Ievadi paroli: ")
    if ievadita_parole != pareiza_parole:
        meginajumi= meginajumi + 1
        print(f"Atlikuši mēģinājumi: {max_meiginajumi - meginajumi}")
    if ievadita_parole == pareiza_parole:
        print("Piekļuve piešķirta!!!")
    if meginajumi == max_meiginajumi:
        print("Piekļuve bloķēta")
        break

