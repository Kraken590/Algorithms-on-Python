'''3. В массиве найти максимальный отрицательный элемент. Вывести на
экран его значение и позицию в массиве.'''

import random

r = [random.randint(-99, 99) for _ in range(100)]
print(f'Массив: {r}')

max_index = 0

for i in r:
    if r[max_index] > i:
        max_index = r.index(i)

if r[max_index] >= 0:
    print(f'В массиве нет отрицательных элементов')
else:
    print(f'В массиве максимальный отрицательный элемент: {r[max_index]}.',
            f'Находится в массиве на позиции {max_index}')