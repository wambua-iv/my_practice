f = open('messy.txt', 'w')

f.write('we are learning shit')

for x in range(7):
    for y in range(x, 7):
        print(f'[ {x} | {y} ]' ,end=' ')
        print()