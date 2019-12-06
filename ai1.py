import matplotlib.pyplot as plt, numpy as np
from pandas import read_csv
from statistics import mode


file = read_csv('BLK2.csv')

title = ['open','high','low','adjclose','volume']


x = file[title].as_matrix()
y = file['close'].as_matrix()
    
n = len(title)


for i in range(0, n):
    plt.xlabel(title[i])
    plt.ylabel('close')
    plt.plot(file[title[i]].as_matrix(), y, 'ro')
    plt.show




##Характеристики цены закрытия

#Cреднее значение цены закрытия
sum = sum(file['close'])
print(sum)
num = len(file['close'])
print(num)
avg = sum/num
print('Средняя цена',avg)


#Медиана
middle = len(file['close'])/2+0.5
list_sorted=sorted(file['close'])
mediane = list_sorted[int(middle)]
print('Медиана',mediane)


#Максимум
max = max(file['close'])
print('Максимум',max)

#Минимум
min = min(file['close'])
print('Минимум',min)

#Мода
mode = mode(file['close'])
print('Мода',mode)

#Размах
r = max - min
print('Размах', r)

#Стандартное отклонение
so = np.std(file['close'])
print('Стандартное отклонение',so)

#Дисперсия
d = so * so
print('Дисперсия',d)

