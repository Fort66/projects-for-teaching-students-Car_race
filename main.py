#🏆🚗🚙🚩🔋

# python -m pip install rich[jupiter] - установка библиотеки в терминале
# from rich import print as rprint - подключение модуля rprint для вывода в терминал, если понадобится

import sqlite3
from rich.console import Console
import time
import os
import sys
import keyboard
from random import choice
from icecream import ic

# install()

# подгрузка параметров из БД
connection = sqlite3.connect('cr.db')
cursor = connection.cursor()

NICK_LICT = cursor.execute('SELECT name FROM nick_list').fetchall()
CAR_SPR = cursor.execute('SELECT * FROM car_spr').fetchall()
PLAYER_SLOGAN = cursor.execute('SELECT slogan FROM player_slogan').fetchall()
ROAD_LIST = cursor.execute('SELECT symbol FROM road_list').fetchall()
parametrs = cursor.execute('SELECT x_road, x_space_cell, players, distance, time_sec, sleep, station_time FROM parametrs').fetchall()

connection.close()

# определение необходимых переменных
PLAYER_LIST: list[object] = []
STATION_LIST: list[int] = []
MOVE_LIST: list[str] = []
SUM_POSITION: list[int] = []

# распаковка парамеров из БД в переменные
X_ROAD, X_SPACE_CELL, PLAYERS, DISTANCE, TIME_SEC, SLEEP, STATION_TIME = parametrs[0]

# подгрузка функций
from road_map import create_road_map
from cars_create import create_object
from race_logic import race_logic

# создаем консоль для вывода в терминал из бибиотеки rich
console = Console()


# создаем объекты (юниты) автоматом от класса Car
create_object(CAR_SPR, NICK_LICT, PLAYERS, X_ROAD, DISTANCE, PLAYER_LIST, SUM_POSITION)

# очищаем терминал
os.system('cls')

# создаем карту дороги для каждого юнита
for i in range(len(PLAYER_LIST)):
    create_road_map(i, X_ROAD, X_SPACE_CELL, PLAYERS, ROAD_LIST, MOVE_LIST, STATION_LIST, PLAYER_LIST)

# выводим на экран карты дорог
for i in range(len(MOVE_LIST)):
    pass
    print(f'\n{MOVE_LIST[i]}\n')
    

    console.print(f'Дорожка номер {i + 1}. Пилот [yellow italic]{PLAYER_LIST[i].get_name()[0]}[/]. Интервью перед стартом: [green italic]{choice(PLAYER_SLOGAN)[0]}[/]')
console.print('\n[yellow bold]Для старта заезда нажмите Enter[/]')
    
# ожидаем нажатия
keyboard.wait('enter')

# создаем стартовый экран с отсчетом времени
for i in range(10, 0, -1):
    if i == 10:
        console.print(f'    [red bold]Заезд начнется через  {i}[/]', end = '\r')
    else:
        console.print(f'    [red bold]Заезд начнется через  0{i}[/]', end = '\r')
        
    time.sleep(SLEEP)
    
os.system('cls')



while True:
        
    for i in range(len(PLAYER_LIST)):
        
        create_road_map(i, X_ROAD, X_SPACE_CELL, PLAYERS, ROAD_LIST, MOVE_LIST, STATION_LIST, PLAYER_LIST)
        race_logic(i, PLAYER_LIST, X_ROAD, DISTANCE, TIME_SEC, SUM_POSITION, STATION_LIST)

        # если машина достигла финиша или закончилось топливо, то обнуляем ее позицию в списке позиций
        if PLAYER_LIST[i].get_x_position() <= 1 or PLAYER_LIST[i].get_tank_volume() <= 0:
            SUM_POSITION[i] = 0
        else:
            SUM_POSITION[i] = round(PLAYER_LIST[i].get_x_position())

        # обновляем позицию машины
        PLAYER_LIST[i].update(PLAYER_LIST[i].get_speed_volume() / 60 * TIME_SEC / (DISTANCE / X_ROAD))    

        print()
        print(MOVE_LIST[i])
        # ic(PLAYER_LIST[i].get_speed_volume())

        # ic(PLAYER_LIST[i].get_tank_volume())
        # ic(PLAYER_LIST[i].get_x_position())
        # ic(PLAYER_LIST[i].get_avg_max())
        # ic((PLAYER_LIST[i].get_x_position() - STATION_LIST[i]) * DISTANCE / X_ROAD)
        # ic(PLAYER_LIST[i].get_mark())
        # ic(PLAYER_LIST[i].get_stop_station())

        print()
    console.print('\n[green bold]Гоночное табло: [/]')
    # ic(SUM_POSITION)
    for i in range(len(PLAYER_LIST) * 20):
        # работаем с потоком вывода на экран терминала
        # Возврат курсора на предыдущую строку, а в цикле - в начало экрана
        sys.stdout.write("\033[F")  
    
    if sum(SUM_POSITION) == 0:
        # os.system('cls')
        break
        
    time.sleep(SLEEP)







            

