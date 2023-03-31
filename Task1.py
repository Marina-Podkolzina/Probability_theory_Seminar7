#1 )  Даны две  независимые выборки. Не соблюдается условие нормальности
#x1  380,420, 290
#y1 140,360,200,900
#Сделайте вывод по результатам, полученным с помощью функции

#Решение: У нас в задаче 2 выборки и 
#они независимые значит используем критерий Манна- Уитни.

import numpy as np
import scipy.stats as stats

x1=np.array([380,420,290])
y1=np.array([140,360,200,900])
alpha=0.05
stats.mannwhitneyu(x1, y1)
print(stats.mannwhitneyu(x1, y1))

#Вывод: на уровне альфа 5 %  статистически значимых различий  нет,т.к pvalue=0,628 > альфа=0,05.
# Гипотезу Н0 не отвергаем.

