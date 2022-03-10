ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

f_step = ((a,b) for a in ports for b in ports)
f = 0
while True:
    try:
        print(next(f_step))
        f += 1

    except Exception as e:
        print("Koniec")
        break
print(f)


s_step = ((a,b) for a in ports for b in ports if a!=b)


f = 0
while True:
    try:
        print(next(s_step))
        f += 1

    except Exception as e:
        print("Koniec")
        break
print(f)

t_step = ((a,b) for a in ports for b in ports if a < b )

f = 0
for (a,b) in t_step:
    print(a,b)
    f +=1

print(f)
