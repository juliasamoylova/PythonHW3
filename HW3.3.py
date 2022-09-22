# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# list1 = [1.10, 1.20, 3.10, 5.00, 10.01]
# mix_list = []
# for i in list1:
#     mix_list.append(round((i - int(i)), 4))
# print(list1, end=' --> ')
# print((max(mix_list) - min(mix_list)))


list1 = [1.10, 1.20, 3.10, 5.00, 10.01]
mix_list = []
for i in range(len(list1)):
    a = round(list1[i]*10 % 10, 2)
    if a > 0:
        mix_list.append(a)
b = round(float(max(mix_list)-min(mix_list))*10/100, 2)
print(b)
