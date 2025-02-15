class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Plant:
    def __init__(self, name, edible = False):
        self.name = name
        self.edible = edible


class Mammal(Animal):  # млекопитающие класс животные
    def __init__(self, name):
        super().__init__(name)


class Predator(Mammal):  # хищник класс животные
    def __init__(self, name):
        super().__init__(name)


class Flower(Plant):   # цветок класс растение
    def __init__(self, name):
        super().__init__(name, edible = False)


class Fruit(Plant):  # фрукт класс растение
    def __init__(self, name):
        super().__init__(name, edible = True)

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Волк с Уолл-Стрит
# Цветик семицветик
# True
# False
# Волк с Уолл-Стрит не стал есть Цветик семицветик
# Хатико съел Заводной апельсин
# False
# True