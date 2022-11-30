dictionary1 = {'a': 1, 'b': 2, 'c': 3}
dictionary2 = {'c': 3, 'd': 4, 'e': 5}
new_dictionary = {}

dictionary1_set = set(dictionary1)
dictionary2_set = set(dictionary2)

for key in dictionary1_set.union(dictionary2_set):
    new_dictionary[key] = [dictionary1.get(key), dictionary2.get(key)]

print(f'ab = {new_dictionary}')
