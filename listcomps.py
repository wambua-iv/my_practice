colors = ['black', 'white']
sizes = ['S', 'L', 'M']

t_shirts = [(color, size) for color in colors for size in sizes]
print(t_shirts)

dominos = [(x, y) for x in range(1,7) for y in range(x, 7)]
print(dominos)

#generator expressions