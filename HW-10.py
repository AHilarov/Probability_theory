# Провести дисперсионный анализ для определения того, есть ли различия среднего роста
# среди взрослых футболистов, хоккеистов и штангистов. Даны значения роста в трех группах
# случайно выбранных спортсменов:
# Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
# Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
# Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.

import numpy as np
from scipy.stats import f


football = np.array([173, 175, 180, 178, 177, 185, 183, 182])
hockey = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
weightlifting = np.array(
    [172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])


mean_total = np.mean(np.concatenate((football, hockey, weightlifting)))


mean_football = np.mean(football)
mean_hockey = np.mean(hockey)
mean_weightlifting = np.mean(weightlifting)


s2_total = np.sum(
    (np.concatenate((football, hockey, weightlifting)) - mean_total)**2)


s2_between = (mean_football - mean_total)**2 * len(football) + (mean_hockey -
                                                                mean_total)**2 * len(hockey) + (mean_weightlifting - mean_total)**2 * len(weightlifting)


s2_within = np.sum((football - mean_football)**2) + np.sum((hockey -
                                                            mean_hockey)**2) + np.sum((weightlifting - mean_weightlifting)**2)


s2 = s2_total / (len(football) + len(hockey) + len(weightlifting) - 1)


s2_factor = s2_between / 2


s2_residual = s2_within / \
    (len(football) + len(hockey) + len(weightlifting) - 3)


F = s2_factor / s2_residual


p_value = f.sf(F, 2, len(football) + len(hockey) + len(weightlifting) - 3)

print(F, p_value)

# ответ: 5.500053450812598 0.010482206918698694
# так как p-value меньше уровня значимости 0.05, мы можем отвергнуть нулевую гипотезу
# о равенстве средних значений роста в трех группах.
