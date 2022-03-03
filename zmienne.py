# Lab1 zad1
a = b = c = 10
print(a, id(a), b, id(b), c, id(c))
a = 20
print(a, id(a), b, id(b), c, id(c))
print("--------------------")

###################################
#Lab1 zad2
a = b = c = [1,2,3]
print(a, id(a), b, id(b), c, id(c))
a.append(4)
print(a, id(a), b, id(b), c, id(c))
print("--------------------")

###################################
#Lab1 zad3
x = 10
y = 10
print(id(x), id(y))
y += 1

y -= 1
print(id(x), id(y))
y += 1234567890
y -= 1234567890
print(id(x),id(y))
print("--------------------")

###################################
#Lab2 zad1
days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
workdays = days.copy()
workdays = workdays[:-2]
print(days)
print(workdays)
