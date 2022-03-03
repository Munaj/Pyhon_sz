"""
wybory = ["load data", "export data", "analyze & predict"]
opcje = [1,2,3]

while True:
    wybor = input("Wybierz opcje: \n1 {}\n2 {}\n3 {} ".format(*wybory)).strip()
    try:
        wybor = int(wybor)
    except:
        print("\n!!Podana wartość nie jest liczbą!!\n")
    else:
        if wybor in opcje:
            print(f"\n{wybor} {wybory[wybor-1]}")
            break
        else:
            print("\nPodano liczbę spoza zakresu\n")
"""


def DisplayOptions(lista):
    print(("1 - {}\n2 - {}\n3 - {} ".format(*lista)).strip())
    user_choice = input("Select option above or press enter to exit:")
    return user_choice
    
options = ["load data", "export data", "analyze & predict"]
choice = "x"

while choice:
    choice  = DisplayOptions(options)
    if choice:
        try:
            choice_num = int(choice)
        except:
            print("\n\nPodana wartość nie jest liczbą!!\n\n")
            choice_num = 0

        if choice_num in range(1,4):
            print(f"\n\n{choice_num} - {options[choice_num - 1]}\n\n")

        elif choice_num == 0:
            pass
        else:
            print("\n\nLiczba z poza zakresu!\n\n")
    else:
        print("Koniec programu.")
