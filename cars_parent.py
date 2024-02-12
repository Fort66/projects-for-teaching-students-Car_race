# from abc import ABC, abstractmethod

# # абстрактный базовый класс Транспорт
# class Vehicle(ABC):

#     # метод, который возвращает объем бака
#     @abstractmethod
#     def get_max_tank(self):
#         pass

#     # метод, который возвращает средний расход топлива
#     @abstractmethod
#     def get_avg_consumption(self):
#         pass

#     # метод, который возвращает максимальный расход на высокох скоростях
#     @abstractmethod
#     def get_avg_max(self):
#         pass
    
#     # метод, который возвращает марку транспорта
#     def get_mark(self):
#         pass

#     # метод, который возвращает информацию о транспорте
#     def get_car_info(self):
#         pass

#     # метод, котрый возвращает максимальную скорость
#     def get_max_speed(self):
#         pass

    

# подкласс автомобили
class Cars():

    def __init__(self, mark: str, max_tank: int, avg_consumption: int, avg_max: int, max_speed: int):
        self.__mark = mark
        self.__max_tank = max_tank
        self.__avg_cons = avg_consumption
        self.__max_speed = max_speed
        self.__avg_max = avg_max
    
    def get_max_tank(self) -> int:
        return self.__max_tank
    
    def get_avg_consumption(self) -> int:
        return self.__avg_cons
    
    def get_avg_max(self) -> int:
        return self.__avg_max
    
    def get_mark(self) -> str:
        return self.__mark

    def get_max_speed(self) -> int:
        return self.__max_speed
    
    # Характеристики машины
    def get_car_info(self) -> str:
        return f'Марка: {self.__mark}\nМаксимальная скорость: {self.__max_speed}\nСредний расход топлива: {self.__avg_cons}\nОбъем бака: {self.__max_tank}\nМаксимальный расход топлива: {self.__avg_max}\n'