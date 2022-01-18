from collections import namedtuple

City = namedtuple('City', 'name country capital')

Nairobi = City('Nairobi', 'Kenya', False)

print(Nairobi)
print(type(Nairobi))
print(City._fields)
print(Nairobi._asdict)  #returns a collection.OrderedDict attached to the named tuple class

Card = namedtuple('Card', ['rank', 'suit'])

ranks = [str(n) for n in range(2, 11)] + list('JQKA')
suits = 'spades diamonds clubs hearts'.split()

cards = [Card(rank, suit) for suit in suits
for rank in ranks]

print(cards)

#tuple mutability

names = ('steve', 'kevin', 'antony', ['james', 'adam'])

names[3].extend(['joyner', 'logic'])
print(names)
names[3] += ['ryan', 'dan']

