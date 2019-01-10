class Person:
    def __init__(self):
        self.name = 'Боб'


bob = Person()
same_bob = bob
print(bob is same_bob)

another_bob = Person()
print(bob is another_bob)

print(bob)
print(same_bob)
print(another_bob)
