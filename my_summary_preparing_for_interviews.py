# |||||||||| Вопросы на собеседовании ||||||||||
# Актуальные версии Python
# ● Python 3.x vs Python 2.7
# ● Основные отличия
# _______________________________________________

# Сильные стороны Python:
# ● кроссплатформенность
# ● мультипарадигмальность (ООП, функциональное и императивно-процедурное программирование)
# ● динамическая типизация
# ● поддержка юникода из коробки
# ● жесткие требования к написанию кода (PEP 8)

# Подробнее о динамической типизации: https://www.youtube.com/watch?v=cbOq9HNU8Yg
# x = 's'
# print(hex(id(x)))
#
# x = 3
# print(hex(id(x)))


def hex_(*args, **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
    """
    Return the hexadecimal representation of an integer.

       >>> hex(12648430)
       '0xc0ffee'
    """
    pass


# _____________________________________________
# Слабые стороны Python:
# ● производительность
# ● многопоточность
# ● реализация функциональной парадигмы
# ● динамическая типизация

# GIL (global interpreter lock) - глобальная блокировка интерпретатора https://www.youtube.com/watch?v=AWX4JnAnjBE


# _____________________________________________
# Области применения
# ● веб-разработка (django, flask, tornado, twisted)
# ● автоматизация процессов - DevOps (ansible, fabric, salt stack)
# ● автоматизация тестирования (behave!, robot framework, pytest, nose, unittest)
# ● наука и анализ данных (scipy, numpy, pandas)●desktop applications (pyqt, pygtk)
# ● gamedev
# ● IoT (Micro Python)
# ● mobile applications (Kivy)


# _____________________________________________
# Трансляторы: compiler, interpreter https://www.youtube.com/watch?v=Vc8FObxtxio

# _____________________________________________
# Абстракция https://www.youtube.com/watch?v=uSnli_4BrEA

# _____________________________________________
# ● Массив в python
# https://codecamp.ru/blog/python-arrays/
# and
# https://pythonworld.ru/moduli/modul-array-massivy-v-python.html

# ● Двоичное дерево https://www.youtube.com/watch?v=9o_i0zzxk1s&list=LL&index=13&t=1s
# ● Односвязный список https://www.youtube.com/watch?v=C9FK1pHLnhI&list=LL&index=12&t=655s
# ● Двусвязный список https://www.youtube.com/watch?v=lQ-lPjbb9Ew&t=434s

# _____________________________________________
# Концепция Big O
# main article https://stackabuse.com/big-o-notation-and-algorithm-analysis-with-python-examples/
# main video https://www.youtube.com/watch?v=ZRdOb4yR0kk
# other important video:
# https://www.youtube.com/watch?v=kwmQwGbAh28
# https://www.youtube.com/watch?v=eJRg4qr7qAo&list=LL&index=2
# https://www.youtube.com/watch?v=mgvbBU4bMF8&list=LL&index=3&t=168s
# https://www.youtube.com/watch?v=72jqTtfw2z4&list=LL&index=1
# https://www.youtube.com/watch?v=C9FK1pHLnhI&list=LL&index=5&t=655s
# https://www.youtube.com/watch?v=9o_i0zzxk1s&list=LL&index=6&t=3s

# we can visualize with this library
import matplotlib.pyplot

x = [2, 4, 6, 8, 10, 12]

y = [2, 4, 6, 8, 10, 12]

matplotlib.pyplot.plot(x, y, 'b')
matplotlib.pyplot.xlabel('my_x')
matplotlib.pyplot.ylabel('my_y')
matplotlib.pyplot.title('It is my table :-)')

# matplotlib.pyplot.show()


# ● O(1)           - когда у нас гарантированно одно действие: например, найти индекс у сортированного элемента
# ● O(n)           - когда сложность растет в линейном порядке параллельно с увеличением входных параметров
#                    или когда мы имеем 2 подряд идущих невложенных зависимых цикла: O(n + n) = O(n)
# ● O(n^2)         - при вложенных циклах, а так же при ситуациях где изначально при запуски и внешнего, и вложенного
#                    циклов длины n внешней и n внутренней равны, а затем одна из них сокращается,
#                    скажем, в 2 раза: O(n^2 / 2) ≈ O(n^2)
# ● O(n^3)         - при вложенных циклах (двойная вложенность)
# ● O(2^n)
# ● O(n + other)   - когда идут 2 подряд независимых друг от друга цикла
# ● O(n * other)   - когда внешний цикл длиной n, а внутренний цикл длинной other
# ● O(log n)       - при использовании бинарного поиска по сортированному контейнеру (ищем по принципу двоичного дерева)
# ● O(n * log(n))  - при использ. бинарного поиска по несортированному контейнеру (ищем по принципу двоичного дерева)


# ● Big O показывает темп роста функции. Следовательно мы не учитываем константы и неважную сложность
# ● Последовательность действий - сложение. Вложенные действия - умножение
# ● Для алгоритма, где на каждой итерации берется половина элементов сложность будет включать O(log n) или O(n * log(n))

# _____________________________________________
# Лучшая статья по всем типам данных
# https://pythonworld.ru/tipy-dannyx-v-python


# _____________________________________________
# a problem from lesson
from typing import Optional, List

# # initial variant
# class Solution:
#     def two_sum(self, nums: List[int], target: int) -> List[int]:
#         for i1, n1 in enumerate(nums):
#             for i2, n2 in enumerate(nums):
#                 if n1 + n2 == target:
#                     return [i1, i2]


# # some simplified variant
# nums = [4, 2, 3, 5, 1, 0, 9]
# target = 9
# for index_1, number_out in enumerate(nums):
#     # print(i1, n1)
#     for index_2, number_inner in enumerate(nums):
#         # print(i2, n2)
#         if index_1 + index_2 == target:  # не должно быть такого, что сумма одного и того же числа давала результат
#             continue
#         if number_out + number_inner == target:
#             print([index_1, index_2])  # это индексы


# # right solution
# nums = [1, 7, 2, 4, 6, 7, 0]
# pairs = {}
# target = 9
# for index_in_nums_list, number in enumerate(nums):
#     pairs[target - number] = index_in_nums_list
#     # print(pairs)
#     if number in pairs:
#         # print(number, pairs, pairs[number], index_in_nums_list)
#         print(pairs[number], index_in_nums_list)
