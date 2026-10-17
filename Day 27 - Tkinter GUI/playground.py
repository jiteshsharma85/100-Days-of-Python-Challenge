
k = 0
# Adds all given numbers together and prints the running total
def add(*args):
    for n in args:
        global k
        k += n
    print(k)


add(1,1,1,1,1,100,1000)