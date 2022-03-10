ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

f_step = [(a,b) for a in ports for b in ports]
print(f_step)



s_step = [(a,b) for a in ports for b in ports if a!=b]
print(s_step)

t_step = [(a,b) for a in ports for b in ports if a < b ]
print(t_step)

print(len(f_step))
print(len(s_step))
print(len(t_step))
