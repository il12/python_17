import pandas
import matplotlib.pyplot as plot
import numpy
from random import random

import warnings
warnings.simplefilter('ignore', numpy.RankWarning)

src = pandas.read_csv('src.csv',sep=';')

param = 'rCount' #'square'
paramLabel = 'Кол-во комнат' #'Площадь квартиры'
x = src[param]
y = src['cost']
n = 5

ourValue = 3

def get_coeff(power=1):
    return numpy.polyfit(x,y,power)

def get_expectation(data):
    """
    Ищем математическое ожидание
    """
    items = []
    counts = []
    prob = []
    for i in range(len(data)):
        if items.count(data[i]) == 0:
            items.append(data[i])
            counts.append(0)
        else:
            counts[items.index(data[i])] += 1

    for i in range(len(items)):
        prob.append(counts[i] / len(data))
        prob[i] *= items[i]

    return sum(prob)

def get_deviation():
    """
    Ищем среднеквадратичное отклонение
    """
    return get_expectation(x**2) - get_expectation(x)**2

def get_error(f,x,y):
    """
    Найдём ошибку при работе нашей модели с настоящими данными.
    """
    return sum((f(x) - y) ** 2)

plot.scatter(x, y,s=15)

plot.xlabel(paramLabel)
plot.ylabel("Цена, млн.руб.")

plot.xticks([w for w in range(0,int(round(max(x))) + 1, 10 if max(x)>50 else 1)])
plot.autoscale(tight=True)

plot.grid(True, linestyle='-', color='0.75')

listForLegend = []
for i in range(1,n+1):
    coeff = get_coeff(i)

    lineCoord = numpy.linspace(0, x[len(x)-1], 500)

    model = numpy.poly1d(coeff)

    print(numpy.polyval(model,ourValue))

    print('Ошибка для модели, основанной на полиноме {} степени, равна {}'.format(i,get_error(model,x,y)))

    plot.plot(lineCoord,model(lineCoord),linewidth=2.0,color=[random(),random(),random()])
    listForLegend.append('d={}'.format(i))
plot.legend(listForLegend)
plot.show()

print('Среднеквадратичное отклонение равно {}'.format(get_deviation()))
