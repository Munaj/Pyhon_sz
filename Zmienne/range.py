
colours = ["red", "orange", "green", "violet", "blue", "yellow"]

def cutter(array,size):
    new_arr = array[:size]
    return new_arr

for i in range(len(colours)+1):
    print(cutter(colours,i))
