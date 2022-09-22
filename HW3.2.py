# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
b = int(input('Введите количество чисел в списке: '))
list_b = list(random.randint(0, 10) for i in range(b))
print(list_b)
multi_b = list(list_b[i]*list_b[-1*(i+1)] for i in range(b//2+(b % 2)))
print(multi_b)

#my_list = [2,3,4,5,6]
#result_list = []
#for i in range((len(my_list)+1)//2)
#   result_list.append(my_list[i]*my list[len(my_list)-1-i])
#   print(result_list)