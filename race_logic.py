# логика игры каждого гонщика
'''
1. Каждый игрок проверяет остаток топлива в баке машины (который сгенерирован случайным образом).
Если топлива хватает жать на полную до финиша, то max_speed и полетел.
2. Если до финиша на максималке не хватает, то проверяет, хватит ли на максималке до заправки. Если да, то жмем до заправки по максимуму.
3. Если до заправки на максималке не хватит, то на экономе до заправки.
4. Если ни на что не хватает, т.е. даже на экономе до заправки, то позоримся красиво, максималка и до окончания топлива в баке.
'''

# Итак, главным становится уровень топлива в баке на момент старта всей гонки. Именно от него и будем плясать во всех расчетах. И далее уровень топлива будет определять скоростной режим машин.


# DISTANCE = 300 # км
# GAME_TIME_SEC = 5 # 1 секунда - 5 мин
# X_ROAD = 60 # кол-во ячеек на путь в DISTANCE км
# DISTANCE = 300 / X_ROAD  - км в одной ячейке
# Пройденный путь за GAME_TIME_SEC секунд - V / 60 * GAME_TIME_SEC


def race_logic(idx: int, PLAYER_LIST: list, X_ROAD: int, DISTANCE: int,
               TIME_SEC: int, SUM_POSITION: list, STATION_LIST: list) -> None:

    # кол-во км в одной ячейке
    lenght_cells = DISTANCE / X_ROAD

    # расстояние, которое осталось проехать до финиша
    finish_distance = PLAYER_LIST[idx].get_x_position() * lenght_cells

    # расстояние до заправки
    station_distance = finish_distance - (STATION_LIST[idx] * lenght_cells)

    # необходимое количество топлива для проезда трассы на максималке
    amount_fuel_maxspeed_alldistance = PLAYER_LIST[idx].get_avg_max(
    ) * finish_distance / 100

    # необходимое количество топлива для проезда трассы до заправки на максималке
    amount_fuel_maxspeed_station = (finish_distance - station_distance) * PLAYER_LIST[idx].get_avg_max() / 100

    # на экономе до заправки.
    amount_fuel_econom_station = (finish_distance - station_distance) * PLAYER_LIST[idx].get_avg_consumption() / 100

    # проверка возможности дистанции на максималке и установка скорости
    if PLAYER_LIST[idx].get_tank_volume() >= amount_fuel_maxspeed_alldistance:
        PLAYER_LIST[idx].set_speed_volume(PLAYER_LIST[idx].get_max_speed())

    # проверка возможности дистанции до заправки на максималке и установка скорости
    elif PLAYER_LIST[idx].get_tank_volume() >= amount_fuel_maxspeed_station and PLAYER_LIST[idx].get_x_position() > STATION_LIST[idx]:
        PLAYER_LIST[idx].set_speed_volume(PLAYER_LIST[idx].get_max_speed())
        PLAYER_LIST[idx].set_stop_station(TIME_SEC * 2)

    # проверка на экономе до заправки и установка скорости
    elif PLAYER_LIST[idx].get_tank_volume() >= amount_fuel_econom_station and PLAYER_LIST[idx].get_x_position() > STATION_LIST[idx]:
        PLAYER_LIST[idx].set_speed_volume(110)
    
    else:
    # иначе позоримся красиво 250 км/ч до выгорания топлива
        PLAYER_LIST[idx].set_speed_volume(PLAYER_LIST[idx].get_max_speed())
    
    # расход топлива на максимальной скорости за пройденный отрезок x = avg_max * S / 100
    fuel_consumption_max = (PLAYER_LIST[idx].get_avg_max() * (PLAYER_LIST[idx].get_old_x_position() - PLAYER_LIST[idx].get_x_position()) * lenght_cells) / 100

    # расход топлива на эконом режиме за пройденный отрезок x = avg_consumption * S / 100
    fuel_consumption_econom = (PLAYER_LIST[idx].get_avg_consumption() * (PLAYER_LIST[idx].get_old_x_position() - PLAYER_LIST[idx].get_x_position()) * lenght_cells) / 100

    # Обрабатываем расход топлива от пройденной дистанции
    if PLAYER_LIST[idx].get_speed_volume() == PLAYER_LIST[idx].get_max_speed():    
        # для максимальной скорости
        PLAYER_LIST[idx].set_tank_volume(PLAYER_LIST[idx].get_tank_volume() - fuel_consumption_max)
    else:
        # для эконом режима
        PLAYER_LIST[idx].set_tank_volume(PLAYER_LIST[idx].get_tank_volume() - fuel_consumption_econom)

    # присваиваем старой позиции значение  текущей, после вычисления расхода топлива
    PLAYER_LIST[idx].set_old_x_position(PLAYER_LIST[idx].get_x_position())

    # проверяем не проскочили ли мы заправку при необходимости залить топливо и позиционируем машину на ней на время заправки
    if PLAYER_LIST[idx].get_x_position() <= STATION_LIST[idx] and PLAYER_LIST[idx].get_stop_station() > 0:
        PLAYER_LIST[idx].set_speed_volume(0)
        PLAYER_LIST[idx].set_x_position(STATION_LIST[idx])
        PLAYER_LIST[idx].set_tank_volume(PLAYER_LIST[idx].get_max_tank())
        PLAYER_LIST[idx].set_stop_station(PLAYER_LIST[idx].get_stop_station() - TIME_SEC)
    
    # Если топливо в машине закончилось, устанавливаем скорость в 0 и машина просто стоит на трассе
    if PLAYER_LIST[idx].get_tank_volume() <= 0:
        PLAYER_LIST[idx].set_speed_volume(0)

