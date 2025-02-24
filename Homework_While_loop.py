"""
Практическое задание
Домашняя работа по уроку "Стиль кода часть II. Цикл While."

Цель: применить навыки создания цикла while, а так же применения операторов break и continue.

Задача "Нули ничто, отрицание недопустимо!":

Дан список чисел [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

Нужно выписывать из этого списка только положительные числа до тех пор, пока не встретите отрицательное
или не закончится список (выход за границу).

Пункты задачи:

Запишите исходный список в переменную my_list.

Напишите цикл while с соответствующими задаче условиями.
Используйте операторы прерывания/продолжения цикла в соответствии с условиями задачи.


Результат выполнения программы:
Исходные данные:
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

Вывод на консоль:
42
69
322
13
99

Примечания:
Чтобы перебрать список вам понадобиться обращение по индексу, запишите в отдельную переменную начальное значение - 0.
Чтобы не выйти за границу списка, в условии цикла while рекомендуется сравнивать текущий индекс и длину списка (функция len()).
Оператор continue - возвращает вас к условию цикла, игнорируя код после себя, break - прерывает цикл.
0 - не отрицательное и не положительное число.
"""

# Дан список чисел [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

# 1. Запишите исходный список в переменную my_list:

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

# 2. Напишите цикл while с соответствующими задаче условиями

i = 0 # счетчик цикла

print('Исходный список: ', my_list)

while i <= len(my_list):
	if my_list[i] < 0:
		break

		if my_list[i] == 0:
			continue # 0 - не отрицательное и не положительное число

	else:
		print(my_list[i])

	i = i + 1