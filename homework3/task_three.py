from random import randint
import random

element_list = [randint(-100, 100) for i in range(10)]
print(element_list)
element_list[2] = random.randrange(start=-100, stop=100)
element_list.pop(6)

print(element_list)
