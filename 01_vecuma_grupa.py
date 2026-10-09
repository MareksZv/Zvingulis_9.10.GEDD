vecums = input("Ievadi savu vecumu: ")

if vecums.strip() == "":
    print("Kļūda: vecums nav ievadīts.")
else:
        vecums = int(vecums)

        if vecums < 0:
            print("Kļūda: vecums nevar būt negatīvs.")
        elif vecums <= 11:
            print("bērns")
        elif vecums <= 17:
            print("pusaudzis")
        elif vecums <= 64:
            print("pieaugušais")
        else:
            print("seniors")

