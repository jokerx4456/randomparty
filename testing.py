import random

list = ['Saki', 'Taku', 'Noah', 'Reon', 'Onney', 'Pong']
i = 0
while i < 6:
    x = random.randint(1, 5)
    print(list[x])
    list.remove(x)
    i += 1
    list.remove(x)
