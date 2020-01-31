#
a = {'a': 1, 'b': 1, 'c': 2}
indices = []
key = 1
for coord, dist in a.items():
    if key == dist:
        indices.append(coord)

print(indices)
#

#
a = {'a': 1, 'b': 1, 'c': 2}
key = 1
indices = [coord for coord, dist in a.items() if key == dist]

print(indices)

"How to see a list of keys with desired variable"