# Задача 1. Когда используется критерий Стьюдента, а когда Z –критерий?

# Задача 2. Проведите тест гипотезы. Утверждается, что шарики для подшипников, изготовленные
# автоматическим станком, имеют средний диаметр 17 мм.
# Используя односторонний критерий с α=0,05, проверить эту гипотезу, если в выборке из
# n=100 шариков средний диаметр
# оказался равным 17.5 мм, а дисперсия генеральной совокупности известна и равна 4 кв. мм.

# Задача 3. Проведите тест гипотезы. Продавец утверждает, что средний вес пачки печенья
# составляет 200 г.
# Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет:
# 202, 203, 199, 197, 195, 201, 200, 204, 194, 190.
# Известно, что их веса распределены нормально.
# Верно ли утверждение продавца, если учитывать, что уровень значимости 1%? (Провести двусторонний тест.)

# Задачу 4 решать с помощью функции.
# Задача 4. Есть ли статистически значимые различия в среднем росте матерей и
# дочерей?
# Рост матерей 172, 177, 158, 170, 178,175, 164, 160, 169, 165
# Рост взрослых дочерей: 173, 175, 162, 174, 175, 168, 155, 170, 160, 163

#1
print ('Задача 1\nКритерий Стьюдента используется для проверки статистических гипотез о среднем значении выборки, когда известно только среднеквадратическое отклонение генеральной совокупности. Z-критерий, или критерий нормального распределения, используется в тех случаях, когда известны среднее значение и стандартное отклонение генеральной совокупности. Если размер выборки больше 30, то оба критерия могут быть использованы приблизительно одинаково. Если размер выборки меньше 30, то следует использовать критерий Стьюдента.')


#2
print ('\nЗадача 2')
import math


#Задаем уровень значимости α и определяем критическую область:
alpha = 0.05
t_critical = 1.645 # для df=99, односторонний критерий

#Вычисляем статистику критерия:
sample_mean = 17.5
pop_mean = 17
pop_std = math.sqrt(4)
n = 100

t_score = (sample_mean - pop_mean) / (pop_std / math.sqrt(n))

#Сравниваем значение статистики критерия с критическим значением и делаем вывод:
if t_score > t_critical:
    print("Отвергаем нулевую гипотезу")
else:
    print("Принимаем нулевую гипотезу")



#3
print ('\nЗадача 3')
#Задаем уровень значимости α/2 и определяем критическую область:

alpha = 0.01
t_critical = 2.821 # для df=9, двусторонний критерий

#Задаем выборку и вычисляем ее среднее значение и стандартное отклонение:
sample = [202, 203, 199, 197, 195, 201, 200, 204, 194, 190]
n = len(sample)
sample_mean = sum(sample) / n
sample_std = math.sqrt(sum([(x - sample_mean)**2 for x in sample]) / (n - 1))


#Вычисляем статистику критерия:
t_score = (sample_mean - 200) / (sample_std / math.sqrt(n))


#Сравниваем значение статистики критерия с критическим значением и делаем вывод:
if abs(t_score) > t_critical:
    print("Отвергаем нулевую гипотезу")
else:
    print("Принимаем нулевую гипотезу")


#4
print ('\nЗадача 4')
import numpy as np
from scipy.stats import t

mother_heights = [172, 177, 158, 170, 178, 175, 164, 160, 169, 165]
daughter_heights = [173, 175, 162, 174, 175, 168, 155, 170, 160, 163]

alpha = 0.05
df = len(mother_heights) + len(daughter_heights) - 2
t_critical = abs(t.ppf(alpha / 2, df))

n1 = len(mother_heights)
n2 = len(daughter_heights)
mean1 = np.mean(mother_heights)
mean2 = np.mean(daughter_heights)
std1 = np.std(mother_heights, ddof=1)
std2 = np.std(daughter_heights, ddof=1)

se = math.sqrt((std1**2 / n1) + (std2**2 / n2))
t_score = (mean1 - mean2) / se


if abs(t_score) > t_critical:
    print("Отвергаем нулевую гипотезу")
else:
    print("Принимаем нулевую гипотезу")