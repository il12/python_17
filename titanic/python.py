import pandas as pd
import numpy as np
import statistics

data = pd.read_csv('train.csv', index_col='PassengerId')

def getNames(sexTarget,ageTarget=0):
    # Функция возвращает список имен всех лиц нужного пола, которые старше определенного возраста
    res = []
    allNames = list(data['Name'])
    sex = list(data['Sex'])
    age = list(data['Age'])
    for i in range(len(allNames)):
        name = allNames[i]
        if (sex[i] == sexTarget and ageTarget <= age[i]):
            if (sex[i] == 'male'):
                if (name.find('(') != -1):
                    tmp = name.split('(')[0].split(' ')
                    index = -2
                    if (tmp[index] == 'Mr.' or tmp[index] == 'Master.'):
                        index = -1
                    res.append(tmp[index])
                else:
                    tmp = name.split('(')[0].split(' ')
                    index = -3
                    if (tmp[index] == 'Mr.' or tmp[index] == 'Master.'):
                        index = -2
                    res.append(tmp[index])
            else:
                if (name.find('(') != -1):
                    tmp = name.split('(')[0].split(' ')
                    index = -3
                    if (tmp[index] == 'Mrs.' or tmp[index] == 'Miss.'):
                        index = -2
                    res.append(tmp[index])
                else:
                    tmp = name.split('(')[0].split(' ')
                    index = -2
                    if (tmp[index] == 'Mrs.' or tmp[index] == 'Miss.'):
                        index = -1
                    res.append(tmp[index])
    return res

def convertGenderIntoInt(data):
    # Функция переводит пол в числовое представление
    res = []
    for d in data:
        if d == 'male':
            res.append(1)
        else:
            res.append(0)
    return res


def get_number_of_pass(sex, data = None):
    '''
    Сколько женщин и мужчин ехали на пароходе
    :param sex:
    :param data:
    :return:
    '''
    sexratio = data.value_counts()
    if sex == 'male':
        return sexratio['male']
    else:
        return sexratio['female']

male = get_number_of_pass('male',data['Sex'])
female = get_number_of_pass('female',data['Sex'])
print("Number of passengers")
print(male, female)

def get_count_of_pass_in_port(port, data=None):
    '''
    Сколько пассажиров загрузилось на борт в различных портах
    :param port:
    :param data:
    :return:
    '''
    portcount = data.value_counts()
    if port == 'C':
        return portcount['C']
    elif port == 'Q':
        return portcount['Q']
    elif port == 'S':
        return portcount['S']

cherbourg = get_count_of_pass_in_port('C', data['Embarked'])
queenstown = get_count_of_pass_in_port('Q', data['Embarked'])
southampton = get_count_of_pass_in_port('S', data['Embarked'])
print('Ports')
print(cherbourg, queenstown, southampton)

def get_count_of_pass_in_class(port, data=None):
    '''
    Какие доли составляли пассажиры первого, второго, третьего класса?
    :param port:
    :param data:
    :return:
    '''
    classcount = data.value_counts()
    if port == 1:
        return classcount[1]
    elif port == 2:
        return classcount[2]
    elif port == 3:
        return classcount[3]

first = get_count_of_pass_in_class(1, data['Pclass'])
second = get_count_of_pass_in_class(2, data['Pclass'])
third = get_count_of_pass_in_class(3, data['Pclass'])
sum = first+second+third
print('Class')
print(round(first/sum, 3), round(second/sum, 3), round(third/sum, 3))


survived = data['Survived']
age = data['Age'].values.reshape(1,-1)
sex = convertGenderIntoInt(data['Sex'])
pclass = data['Pclass']
print("Корелляция")
print(np.corrcoef(age, survived)[0][1], np.corrcoef(survived, sex)[0][1], np.corrcoef(survived, pclass)[0][1])

print('Cредняя цена за билет')
print(data['Fare'].mean())

print('Цена за билет: медиана')
print(data['Fare'].median())


print('Cамое популярное мужское имя на корабле. Человек должен быть старше 15 лет')
print(statistics.mode(getNames('male',15)))
print()

print('Cамое популярное женское имя на корабле. Человек должен быть старше 15 лет')
print(statistics.mode(getNames('female',15)))

