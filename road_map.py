from random import randint

# создаем карту дороги для каждого юнита
def create_road_map(idx: int, X_ROAD: int, X_SPACE_CELL: str, PLAYERS: int, ROAD_LIST: tuple, MOVE_LIST: list, STATION_LIST: list, PLAYER_LIST: list) -> str:
    
    # определяем рандомное расположение станций заправки
    if len(STATION_LIST) < PLAYERS:
        STATION_LIST.append(randint(1, X_ROAD - 5))

    road_map = ROAD_LIST[0][0]
    
    # создаем карту дороги
    for i in range(X_ROAD + 1):
        # следующий символ в дороге всегда __
        road_map_next_position = X_SPACE_CELL
        
        # если позиция машины <= 0, то позиция равна 0
        if PLAYER_LIST[idx].get_x_position() <= 0:
            PLAYER_LIST[idx].set_x_position(0)
        
        if i == STATION_LIST[idx]:
            road_map_next_position = ROAD_LIST[-2][0]

        if i == round(PLAYER_LIST[idx].get_x_position()):
            road_map_next_position = PLAYER_LIST[idx].get_views()
        
        road_map += road_map_next_position

    road_map += ROAD_LIST[-1][0]        

    if len(MOVE_LIST) < PLAYERS:
        MOVE_LIST.append(road_map)
    else:
        MOVE_LIST[idx] = road_map





