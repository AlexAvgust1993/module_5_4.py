class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        house_name = args[0]
        cls.houses_history.append(house_name)
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    # def __init__(self, name, number_of_floors):
    #     self.name = name  # Название
    #     self.number_of_floors = number_of_floors  # Количество этажей (18 и 2 этажа)

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):  # Сравнили текущие с представленными этажам № 1
        return self.number_of_floors == other.number_of_floors

    def __add__(self, other):  # Прибавили к текущим этажам № 2
        self.number_of_floors += other
        return self

    def __iadd__(self, other):  # Арифметическое присваивание
        return self + other

    def __radd__(self, value):  # Обратное сложение
        return self.__add__(value)

# А дальше пойдут сравнения
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)




# class User:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):  # cls Указывает на класс
#         print('Я в нью')
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#     def __init__(self):
#         print('Я в ините')
#
#
# user1 = User()
# user2 = User()
# print(User.__mro__)  # object
# print(id(user1), id(user2))
