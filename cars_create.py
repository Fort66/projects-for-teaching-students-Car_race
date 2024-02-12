from random import randint, choice
# from icecream import ic
from car import Car

name_object = ''
tmp_list = []

# создаем экземпляры класса по количеству гонщиков. ЭК  получает имя пилота и все параметры авто, на котором будет заезд

def create_object(CAR_DICT: tuple, NICK_LIST: tuple, PLAYERS: int, X_ROAD: int = 0, DISTANCE: int = 0, PLAYER_LIST: list[object] = [], SUM_POSITION: list[int] = []) -> object:

    # создаем список имён гонщиков (уникальный)
    for i in range(PLAYERS):
        name_object = choice(NICK_LIST)

        while name_object in tmp_list:
            name_object = choice(NICK_LIST)

        tmp_list.append(name_object)

        # ccd - car choice dict читаем параметры авто случайно выбранные
        ccd = choice(CAR_DICT)

        # создаем экземпляры класса
        name_object = Car(
                          name = name_object, 
                          mark = ccd[2], 
                          tank_volume = randint(0, ccd[-1]), 
                          max_tank = ccd[-1], 
                          avg_consumption = ccd[4], 
                          max_speed = ccd[6], 
                          views = ccd[1], 
                          x_position = X_ROAD,
                          avg_max = ccd[5],
                          speed_volume = 0, 
                          distance = DISTANCE
                                            )
                          #speed_volume = randint(100, ccd[6]),
                        #speed_volume = 0,

        # добавляем в список гонщиков
        PLAYER_LIST.append(name_object)

        # добавляем в список позиций авто
        SUM_POSITION.append(name_object.get_x_position())

tmp_list.clear()

        




