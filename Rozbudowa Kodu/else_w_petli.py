import os, urllib.request

data_dir = r"/home/kuba/Desktop/pomocniczy/else/"
pages = [

    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},

    { 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' },

    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} ]

for page in pages:

    path = data_dir + page["name"] +".html"
    try:
        urllib.request.urlretrieve(page["url"],path)
    except:
        print("Error at :",path)
        break
else:
    print("Wszystkie działania zakończone powodzeniem")
