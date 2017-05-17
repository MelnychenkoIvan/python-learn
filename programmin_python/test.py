import locale

locale.setlocale(locale.LC_NUMERIC, 'Russian_Russia.1251')
print(locale.getlocale())

"""This is the command of our module"""
file = open('index.html', 'r', encoding='utf-8')
template_file = file.read()
template_var = {"title": 'Some Title'}
# print(template_file.format(**template_var))

file.close()


class Car:

    def __init__(self, model, color):
        self.model = model
        self.color = color


car = Car('BMW', 'red')
car2 = Car('Lada', 'blue')
print('{0.model:1s} - {0.color}\n{1.model:10} - {1.color}\n{2:c}'.format(car, car2, 65))

