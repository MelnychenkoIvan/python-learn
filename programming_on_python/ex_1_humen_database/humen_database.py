"""Списки"""
from pprint import pprint

bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones', 45, 40000, 'hardware']

people = [bob, sue]

pays = [person[2] for person in people]
print('list salary', pays)

pays_2 = map((lambda x: x[2]), people)
print('list salary', list(pays_2))

sum_salary = sum(person[2] for person in people)
print('sum of salaries', sum_salary)

people.append(['Tom', 50, 0, 'None'])
print(people)

NAME, AGE, PAY = range(3)
print(bob[NAME])

bob_2 = [['name', 'Bob Smith'], ['age', 42], ['pay', 20000]]
sue_2 = [['name', 'Sue Jones'], ['age', 45], ['pay', 40000]]

people_2 = [bob_2, sue_2]

name_list = [people[0][1] for people in people_2]
print(name_list)

for person in people_2:
    for (name, value) in person:
        print(name, ' = ', value)


def field(record, label):
    for (fname, fvalue) in record:
        if fname == label:
            return fvalue

print(field(bob_2, 'name'))


def some(fname=None, lname=None):
    print('first name = %s; last name = %s' % (fname, lname))

some(lname='smith')


"""Словари"""

bob_3 = {'name': 'Bob Smith', 'age': 42, 'pay': 20000}
sue_3 = {'name': 'Sue Jones', 'age': 45, 'pay': 40000}
ann_3 = {'name': 'Ann Brown', 'age': 45, 'pay': 40000}

print((bob_3['name'], sue_3['pay']))

names = ['name', 'age', 'pay']
values = ['Bob Smith', 43, 20000]

print(list(zip(names, values)))
print(dict(zip(names, values)))

records_1 = dict.fromkeys(names, None)
print(records_1)

people_3 = [bob_3, sue_3, ann_3]
print(people_3)

for person in people_3:
    print(person)

names_2 = [person['name'] for person in people_3]
print(names_2)

names_3 = list(map(lambda x: x['name'], people_3))
print(names_3)

print([person for person in people_3 if person['age'] > 43])
print([(rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people_3])

G = (rec['name'] for rec in people_3 if rec['age'] >= 45)
print(next(G))
print(next(G))

people_3_dict = {'bob': bob_3, 'sue': sue_3, 'ann': ann_3}
print(people_3_dict)
pprint(people_3_dict)

for rec in people_3_dict.values():
    print(rec)

print(list(people_3_dict.keys()))