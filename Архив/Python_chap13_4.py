class Rider:
    def __init__(self, name, age):
        self.name = name    # имя
        self.age = age      # возраст


class Horse:
    def __init__(self, alias, breed, owner):
        self.alias = alias  # кличка
        self.breed = breed  # порода
        self.owner = owner  # хозяин


artur = Rider('Артур Морган', 35)
ember = Horse('Уголек', 'арабский', artur)

print(ember.owner.name)
