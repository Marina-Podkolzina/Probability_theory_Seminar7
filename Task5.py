#5) Заявляется, что партия изготавливается со средним арифметическим 2,5 см. 
#Проверить данную гипотезу, если известно, что размеры изделий подчинены нормальному закону распределения. 
#Объем выборки 10, уровень статистической значимости 5%

#2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34

#Решение: Составим гипотезы  
# H0 : mu= 2.5
# H1 : mu!= 2.5

import numpy as np
import scipy.stats as stats

weights = np.array([2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34])
n = 10
mean = weights.mean()
std = weights.std(ddof=1)
mean, std
print(mean, std)

# хср = 2.5279999999999996, среднее квадратичное отклонение =0.1572542173961923)
# Так как дисперсия нам не известна то используем критерий Стьюдента 

t = (mean-2.5)/(std/np.sqrt(n)) # t- наблюдаемое
t
print(t)

# t расчетное = 0.5630613661802959
#Доверительная вероятность 95% , число степеней свободы = 9

stats.t.ppf(0.975, 9)
print(stats.t.ppf(0.975, 9))
# t наблюдаемое = 2.2621571627409915
#Вывод: на уровне альфа 5 %  статистически значимых различий  нет,
# т.к расчетное значение =0,563 > наблюдаемого = 2.26.
# Гипотезу Н0 не отвергаем.


