# 1. Даны значения зарплат из выборки выпускников:
# 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
# Посчитать (желательно без использования статистических методов наподобие std, var, mean) среднее арифметическое, 
# среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.

# 2. В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых. 
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. Какова вероятность того, что 3 мяча белые?

# 3. На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень. Вероятность попадания для первого
# спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6. Найти вероятность того, что выстрел произведен:
# a). первым спортсменом б). вторым спортсменом в). третьим спортсменом.

# 4. В университет на факультеты A и B поступило равное количество студентов, а на факультет C студентов поступило
# столько же, сколько на A и B вместе. Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8.
# Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9. Студент сдал первую сессию.
# Какова вероятность, что он учится: a). на факультете A б). на факультете B в). на факультете C?

# 5. Устройство состоит из трех деталей. Для первой детали вероятность выйти из строя в первый месяц равна 0.1,
# для второй - 0.2, для третьей - 0.25. Какова вероятность того, что в первый месяц выйдут из строя:
# а). все детали б). только две детали в). хотя бы одна деталь г). от одной до двух деталей?

#=========

#1
print ('Задача 1')
salaries = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]

# Mean
mean = sum(salaries) / len(salaries)
print("Mean:", mean)

# Standard deviation
squared_deviations = [(x - mean)**2 for x in salaries]
variance = sum(squared_deviations) / len(salaries)
std_deviation = variance**(0.5)
print("Standard deviation:", round(std_deviation, 2))

# Biased variance
biased_variance = variance
print("Biased variance:", biased_variance)

# Unbiased variance
unbiased_variance = sum(squared_deviations) / (len(salaries) - 1)
print("Unbiased variance:", round(unbiased_variance, 2))

#2
print ('Задача 2')
from math import comb

# Probability of getting 3 white balls out of 6
prob_3_white = (comb(5,2) * comb(3,1) / comb(8,2)) * (comb(5,1) * comb(7,3) / comb(12,4))

# Probability of getting 2 white balls out of 2 and 1 white ball out of 4
prob_2_white_1_white = (comb(5,2) / comb(8,2)) * (comb(5,1) * comb(7,3) / comb(12,4))

# Probability of getting 1 white ball out of 2 and 2 white balls out of 4
prob_1_white_2_white = (comb(5,1) * comb(3,1) / comb(8,2)) * (comb(5,2) * comb(7,2) / comb(12,4))

# Total probability of getting 3 white balls
total_prob = prob_3_white + prob_2_white_1_white + prob_1_white_2_white

print("Probability of getting 3 white balls:", round(total_prob, 4))


#3
print ('Задача 3')
# Probability of shooting by first athlete
prob_first = 0.9

# Probability of shooting by second athlete
prob_second = 0.8

# Probability of shooting by third athlete
prob_third = 0.6

# Total probability of shooting by any athlete
total_prob = prob_first + prob_second + prob_third

# Probability of shooting by first athlete given that the shot hit the target
prob_first_hit = prob_first / total_prob

# Probability of shooting by second athlete given that the shot hit the target
prob_second_hit = prob_second / total_prob

# Probability of shooting by third athlete given that the shot hit the target
prob_third_hit = prob_third / total_prob

print("Probability of shooting by first athlete given that the shot hit the target:", round(prob_first_hit, 2))
print("Probability of shooting by second athlete given that the shot hit the target:", round(prob_second_hit, 2))
print("Probability of shooting by third athlete given that the shot hit the target:", round(prob_third_hit, 2))


#4
print ('Задача 4')
P_DA = 0.8 # вероятность того, что студент факультета A сдал первую сессию
P_DB = 0.7 # вероятность того, что студент факультета B сдал первую сессию
P_DC = 0.9 # вероятность того, что студент факультета C сдал первую сессию
P_A = 1/3 # вероятность того, что случайно выбранный студент учится на факультете A
P_B = 1/3 # вероятность того, что случайно выбранный студент учится на факультете B
P_C = 1/3 # вероятность того, что случайно выбранный студент учится на факультете C
P_D = P_DA * P_A + P_DB * P_B + P_DC * P_C # полная вероятность того, что студент сдал первую сессию

P_A_D = P_DA * P_A / P_D # вероятность того, что студент учится на факультете A, если он сдал первую сессию
P_B_D = P_DB * P_B / P_D # вероятность того, что студент учится на факультете B, если он сдал первую сессию
P_C_D = P_DC * P_C / P_D # вероятность того, что студент учится на факультете C, если он сдал первую сессию

print("Вероятность того, что студент учится на факультете A:", round(P_A_D, 2))
print("Вероятность того, что студент учится на факультете B:", round(P_B_D, 2))
print("Вероятность того, что студент учится на факультете C:", round(P_C_D, 2))


#5
print ('Задача 5')
P_1 = 0.1 # вероятность выхода из строя первой детали
P_2 = 0.2 # вероятность выхода из строя второй детали
P_3 = 0.25 # вероятность выхода из строя третьей детали

# Вероятность того, что все детали выйдут из строя
P_all = P_1 * P_2 * P_3
print("Вероятность того, что все детали выйдут из строя:", round(P_all, 2))

# Вероятность того, что только две детали выйдут из строя
P_two = P_1 * P_2 * (1-P_3) + P_1 * (1-P_2) * P_3 + (1-P_1) * P_2 * P_3
print("Вероятность того, что только две детали выйдут из строя:", round(P_two, 2))

# Вероятность того, что хотя бы одна деталь выйдет из строя
P_one_or_more = 1 - (1-P_1) * (1-P_2) * (1-P_3)
print("Вероятность того, что хотя бы одна деталь выйдет из строя:", round(P_one_or_more, 2))

# Вероятность того, что от одной до двух деталей выйдут из строя
P_one_or_two = P_one_or_more - P_all
print("Вероятность того, что от одной до двух деталей выйдут из строя:", round(P_one_or_two, 2))