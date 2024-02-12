# # длина пути в отрезках
# X_ROAD: int = 10

# # символы заполнения
# X_SPACE_CELL: str = '__'

# # количество игроков
# PLAYERS: int = 2

# # список игроков
# PLAYER_LIST: list[object] = []

# # список символов для создания дороги
# ROAD_LIST: list[str] = [
#                          '🏆', 
#                          '🔋', 
#                          '🚩'
#                               ]

# # список координат станций заправки
# STATION_LIST: list[int] = []

# # длина пути
# DISTANCE: int = 300 # км

# # время игры сек
# TIME_SEC: int = 5 # 1 сек - N мин

# # время паузы между тиками
# SLEEP: int = 1

# STATION_TIME: int = 10 # время на заправке 10 мин

# # список позиций машин, когда сумма позиций равна 0, игра прекращается
# SUM_POSITION: list[int] = []

# # картинка дороги с позицией машины
# MOVE_LIST: list[str] = []

# # слоганы игроков перед началом заезда
# PLAYER_SLOGAN: list[str] = [
#                               'Порву всех! 👹', 
#                               'Посмотрим,что вы все умеете! 😉', 
#                               'И вы на этом хламе хотите меня сделать? 🤔', 
#                               'Моё турбо еще никто не обошёл! ✌️', 
#                               'Ну-ну, посмотрим, кто будет ржать в конце! 😎', 
#                               'Ха! А силенок у всех хватит? 👊', 
#                               'Ой, да ладно! Это вот они решили против меня выйти? 😂', 
#                               'Все - отстой! А я - д\'Артаньян! 😜',
#                               'Кто победитель? Я - победитель! 💪',
#                               'Буду сражаться! ⚔️',
#                               'Я сделаю всех с разницей в 10 минут! 👌',
#                               'Гонки - это моя жизнь. Остальное - ожидание гонок! Вcем - конец! 👍',
#                               'Победит тот, кто откажется проиграть! И это - я! 👌',
#                               'Идите домой, стригите лужайку. Гонки - это не ваше! 😂',
#                               'Мальчики, валите по домам. Здесь место для храбрых! 💪',
#                                                                      ]

# # Ники игроков
# NICK_LIST: list[str] = [
#                          'Bask', 
#                          'Gray', 
#                          'Eshka', 
#                          'Kudo', 
#                          'Harvy', 
#                          'Disel', 
#                          'Vud', 
#                          'Berserk',
#                          'Kezan',
#                          'Tessi',
#                          'Snupi',
#                          'Dunay',
#                          'Strange_Pilot',
#                          'Jastin',
#                          'Light_Soul',
#                          'Adriezan',
#                          'Henessi',
#                          'Emil',
#                          'Blayk',
#                          'Adjy',
#                          'Imperator',
#                          'Buriel',
#                          'Hessi',
#                          'Yusik',
#                          'Bex',
#                          'Gerald',
#                          'Kado',
#                          'Hari',
#                          'Hernes',
#                          'Torg',
#                          'Hugo',
#                          'Tayron',
#                          'AK_47',
#                          'Tiger',
#                          'Valett',
#                          'Nik',
#                                    ]

# # словарь машин
# CAR_DICT: dict = {
#                     1: {'views': '🚗',
#                          'mark': 'AUDI TT',
#                          'remaining_fuel': None,
#                          'avg_consumption': 12,
#                          'avg_max': 20,
#                          'max_speed': 250,
#                          'max_tank': 50
#                                         }, 
#                     2: {'views': '🚕',
#                          'mark': 'BMW X5',
#                          'remaining_fuel': None,
#                          'avg_consumption': 16,
#                          'avg_max': 23,
#                          'max_speed': 250,
#                          'max_tank': 70
#                                         }, 
#                     3: {'views': '🚙',
#                          'mark': 'Mersdes-Benz Sprinter',
#                          'remaining_fuel': None,
#                          'avg_consumption': 16,
#                          'avg_max': 26,
#                          'max_speed': 250,
#                          'max_tank': 80
#                                         }, 
#                     4: {'views': '🚌',
#                          'mark': 'Wolksvagen Passat',
#                          'remaining_fuel': None,
#                          'avg_consumption': 14,
#                          'avg_max': 18,
#                          'max_speed': 250,
#                          'max_tank': 55
#                                         }, 
#                     5: {'views': '🚓',
#                          'mark': 'Nissan Qashqai',
#                          'remaining_fuel': None,
#                          'avg_consumption': 14,
#                          'avg_max': 18,
#                          'max_speed': 250,
#                          'max_tank': 50
#                                         }, 
#                     6: {'views': '🚑',
#                          'mark': 'Toyota Camry',
#                          'remaining_fuel': None,
#                          'avg_consumption': 14,
#                          'avg_max': 18,
#                          'max_speed': 250,
#                          'max_tank': 60
#                                         }, 
#                     7: {'views': '🚒',
#                          'mark': 'Mitsubishi Lancer Sport',
#                          'remaining_fuel': None,
#                          'avg_consumption': 16,
#                          'avg_max': 20,
#                          'max_speed': 250,
#                          'max_tank': 45
#                                         }, 
#                     8: {'views': '🚐',
#                          'mark': ' Toyota  Land Cruiser',
#                          'remaining_fuel': None,
#                          'avg_consumption': 16,
#                          'avg_max': 22,
#                          'max_speed': 250,
#                          'max_tank': 70
#                                         }
#                                              }






