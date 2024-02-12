# класс автомобили

from cars_parent import Cars


class Car(Cars):
    def __init__(self, mark: str, max_tank: int, avg_consumption: int, avg_max: int, max_speed: int, tank_volume: int,  distance: int, x_position: int, name: str = '', speed_volume: int = 0, views: str = ''):
        super().__init__(mark, max_tank, avg_consumption, avg_max, max_speed)
               
        self.__tank_volume = tank_volume
        self.__views = views
        self.__x_position = x_position
        self.__name = name
        self.__speed_volume = speed_volume
        self.__distance = distance
        self.__stop_station = 0     # добавлена, для отслеживания необходимости заправки и времени на ней
        self.__old_x_position = x_position # добавлена для определения пройденного расстояния и расхода топлива

# tank_volume -------------------------------------
    def get_tank_volume(self) -> int:
        return self.__tank_volume
    
    def set_tank_volume(self, volume: int) -> None:
        self.__tank_volume = volume
#--------------------------------------------------

# speed_volume -------------------------------------
    def get_speed_volume(self) -> int:
        return self.__speed_volume

    def set_speed_volume(self, speed: int) -> None:
        self.__speed_volume = speed
#--------------------------------------------------

# distance ---------------------------------------
    def get_distance(self) -> int:
        return self.__distance

    def set_distance(self, distance: int) -> None:
        self.__distance = distance

#--------------------------------------------------

# добавленные методы для обслуживания self.__stop_station и self.__old_x_position
    def set_stop_station(self, stop_station: int) -> None:
        self.__stop_station = stop_station

    def get_stop_station(self) -> int:
        return self.__stop_station
    
    def get_old_x_position(self) -> int:
        return self.__old_x_position
    
    def set_old_x_position(self, old_x_position: int) -> None:
        self.__old_x_position = old_x_position
#--------------------------------------------------
    
# x_position -------------------------------------

    def get_x_position(self) -> int:
        return self.__x_position

    def set_x_position(self, x_position: int) -> None:
        self.__x_position = x_position
#--------------------------------------------------

    def get_views(self) -> str:
        return self.__views

    def get_name(self) -> str:
        return self.__name

    def update(self, x_position: int) -> int:
        if self.get_tank_volume() > 0:
            self.__x_position = self.get_x_position() - round(x_position)
        return self.__x_position