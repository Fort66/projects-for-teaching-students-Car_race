import sqlite3
from settings import ROAD_LIST, NICK_LIST, PLAYER_SLOGAN, CAR_DICT, X_ROAD, X_SPACE_CELL, PLAYERS, DISTANCE, TIME_SEC, SLEEP, STATION_TIME

connection = sqlite3.connect('cr.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS nick_list (
               id INTEGER PRIMARY KEY AUTOINCREMENT, 
               name TEXT NOT NULL);''')

cursor.execute('''create table if not exists player_slogan (
               id integer primary key autoincrement, 
               slogan text not null);''')    

cursor.execute('''CREATE TABLE IF NOT EXISTS car_spr (
               id integer PRIMARY KEY AUTOINCREMENT, 
               views TEXT NOT NULL, mark TEXT NOT NULL, 
               remaining_fuel INTEGER DEFAULT 0, 
               avg_consumption INTEGER DEFAULT 0, 
               avg_max INTEGER DEFAULT 0, 
               max_speed INTEGER DEFAULT 0, 
               max_tank INTEGER DEFAULT 0);''')

cursor.execute('''CREATE TABLE IF NOT EXISTS parametrs (
               id INTEGER PRIMARY KEY AUTOINCREMENT, 
               x_road INTEGER DEFAULT 0, 
               x_space_cell TEXT DEFAULT "__", 
               players INTEGER DEFAULT 2, 
               distance INTEGER DEFAULT 0, 
               time_sec INTEGER DEFAULT 0, 
               sleep INTEGER DEFAULT 0, 
               station_time INTEGER DEFAULT 0);''')

cursor.execute('''CREATE TABLE IF NOT EXISTS road_list (
               id INTEGER PRIMARY KEY AUTOINCREMENT, 
               symbol TEXT NOT NULL);''')

connection.commit()


for i in NICK_LIST:
    cursor.execute('INSERT INTO nick_list (name) VALUES (?)', (i,))
    connection.commit()

for i in PLAYER_SLOGAN:
    cursor.execute('INSERT INTO player_slogan (slogan) VALUES (?)', (i,))
    connection.commit()

for i in CAR_DICT:
    cursor.execute('''INSERT INTO car_spr (
                   views, mark, 
                   remaining_fuel, 
                   avg_consumption, 
                   avg_max, 
                   max_speed, 
                   max_tank) VALUES (?, ?, ?, ?, ?, ?, ?)''', 
                   (CAR_DICT[i]['views'], 
                    CAR_DICT[i]['mark'], 
                    CAR_DICT[i]['remaining_fuel'], 
                    CAR_DICT[i]['avg_consumption'], 
                    CAR_DICT[i]['avg_max'], 
                    CAR_DICT[i]['max_speed'], 
                    CAR_DICT[i]['max_tank']))
    connection.commit()

cursor.execute('''INSERT INTO parametrs (
               x_road, 
               x_space_cell, 
               players, 
               distance, 
               time_sec, 
               sleep, 
               station_time) VALUES (?, ?, ?, ?, ?, ?, ?)''', 
               (X_ROAD, 
                X_SPACE_CELL, 
                PLAYERS, 
                DISTANCE, 
                TIME_SEC, 
                SLEEP, 
                STATION_TIME))
connection.commit()


for i in ROAD_LIST:
    cursor.execute('INSERT INTO road_list (symbol) VALUES (?)', (i))
connection.commit()