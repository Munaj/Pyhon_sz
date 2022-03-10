import os

def policz(sorce):
    f = open(path)
    words = f.read()
    words = words.split()
    print(len(words))
    f.close()


path = r"/home/kuba/Desktop/pomocniczy/operacje_na_plikach/plik.txt"

'''
if os.path.isfile(path):
    policz(path)
'''
os.path.isfile(path) and policz(path)
