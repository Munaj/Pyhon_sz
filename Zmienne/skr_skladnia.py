from datetime import datetime

#Zad 1
price = 123
bonus = 23
bonus_granted = False

price = price - bonus if bonus_granted else price
print(price)
#Zad 2
rating = 5

print("very good") if rating == 5 else print("good") if rating == 4 else print("weak")
#Zad3
today_weekday = (datetime.today().weekday())
poniedziałek = "Pomagam mamie"
wtorek = "Pranie"
sroda = "Pranie"
czwartek = "dyżur"
piątek =" dwa zebrania"
sobota = "lekcje"
niedziela = "będzie dla nas"
print(today_weekday)

if today_weekday == 0:
    print("Pomagam mamie")
elif today_weekday == 1 or today_weekday == 2:
    print("Pranie")
elif today_weekday == 3:
    print("Dyżur")
elif today_weekday == 4:
    print("Dwa zebrania")
elif today_weekday == 5:
    print("Lekcje")
else:
    print("Będzie dla nas")

print("Pomagam mamie") if today_weekday == 0 else print("Pranie") if today_weekday == 1 or today_weekday == 2\
else print("Dyżur") if today_weekday == 3 else print("Dwa zebrania") if today_weekday == 4\
else print("Lekcje") if today_weekday == 5 else print("Będzie dla nas")
