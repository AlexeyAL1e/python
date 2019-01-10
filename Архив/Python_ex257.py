class Dog:
    def __init__(self, alias, breed, owner):
        self.alias = alias  # кличка
        self.breed = breed  # порода
        self.owner = owner  # хозяин


class Person:
    def __init__(self, name, age):
        self.name = name    # имя
        self.age = age


mick = Person('Мик Джаггер')
stan = Dog('Стенли', 'Бульдог', mick)

print(stan.alias)
