# 특정 열의 score를 찾아주는 함수
def bestScoreFinder(map,turn,turn_count,available_betting_point_address, best_score, start_time):
    # Import
    from .progressing import gameOver
    from .betting import declareAvailableBettingPoint
    import time, math

    time_limit = 15
    left_time = time_limit-math.floor(time.time() - start_time)
    if left_time <= 0:
        return -100
    else:
        print("*",left_time,"seconds left ..", end="\r")
        for point in available_betting_point_address:
            map[point[0]][point[1] - 1] = turn
            # 게임 오버 됐는지
            game_over, winner = gameOver(map, [point[0], point[1] - 1], turn)
            if game_over:
                if winner == 1:
                    score = 21 - int(turn_count/2)
                elif winner == -1:
                    score = (21 - int(turn_count/2))*-1
                else:
                    score = 0
            else:
                available_betting_point_address = declareAvailableBettingPoint(map,available_betting_point_address,1)[0]
                score = bestScoreFinder(map,turn*-1,turn_count+1,available_betting_point_address, 21*turn*-1,start_time)
            map[point[0]][point[1]-1] = 0
            if (turn == -1 and score > best_score) or (turn == 1 and score < best_score):
                best_score = score
        return best_score

# 수를 둘곳을 찾아주는 함수
def pointFinder(map, turn, turn_count, available_betting_point_address, best_score, start_time):
    # Import
    from .progressing import gameOver
    from .betting import declareAvailableBettingPoint

    best_score = best_score
    for point in available_betting_point_address:
        map[point[0]][point[1]-1] = turn
        # 게임 오버 됐는지
        game_over, winner = gameOver(map, [point[0], point[1] - 1], turn)
        if game_over:
            if winner == 1:
                score = 21 - int(turn_count / 2)
            elif winner == -1:
                score = (21 - int(turn_count / 2)) * -1
            else:
                score = 0
        else:
            available_betting_point_address = declareAvailableBettingPoint(map, available_betting_point_address, 1)[0]
            score = bestScoreFinder(map, turn*-1, turn_count+1, available_betting_point_address, 21*turn*-1, start_time)
        map[point[0]][point[1]-1] = 0
        if score == -100:
            return -100, [-1,-1]
        if (turn == -1 and score > best_score) or (turn == 1 and score < best_score):
            best_score = score
            best_point_address = point
    return best_score, best_point_address

# 룰 베이스
def ruleBasedSystem(available_betting_point, last_betting_point):
    # 상대방이 착수한 열에 착수
    for x in available_betting_point:
        if last_betting_point[1]+1 == x[1]:
            print("( Betted on the column that Human betted just before )")
            return x[0], x[1]
    # 상대방이 착수한 열에 착수 할수 없을때 중심에서 가깝고 빈자리가 적은 열에 착수
    print("( Betted close to the center of the remaining column )")
    column_available = [[False, -1],[False, -1],[False, -1],[False, -1],[False, -1],[False, -1],[False, -1]]
    for x in available_betting_point:
        col_address = x[1]
        column_available[col_address-1][0] = True
        column_available[col_address-1][1] = x[0]
    if column_available[3][0]:
        return column_available[3][1], 4
    elif column_available[2][0] and not column_available[4][0]:
        return column_available[2][1], 3
    elif not column_available[2][0] and column_available[4][0]:
        return column_available[4][1], 5
    elif column_available[2][0] and column_available[4][0]:
        if column_available[2][1] >= column_available[4][1]:
            return column_available[2][1], 3
        else:
            return column_available[4][1], 5
    elif column_available[1][0] and not column_available[5][0]:
        return column_available[1][1], 2
    elif not column_available[1][0] and column_available[5][0]:
        return column_available[5][1], 6
    elif column_available[1][0] and column_available[5][0]:
        if column_available[1][1] >= column_available[5][1]:
            return column_available[1][1], 2
        else:
            return column_available[5][1], 6
    elif column_available[0][0] and not column_available[6][0]:
        return column_available[0][1], 1
    elif not column_available[0][0] and column_available[6][0]:
        return column_available[6][1], 7
    else:
        if column_available[0][1] >= column_available[6][1]:
            return column_available[0][1], 1
        else:
            return column_available[6][1], 7

# 인공지능
def connect4AI(available_betting_point_address, map, turn, turn_count, state, last_betting_point):
    # Import
    import time
    from .progressing import gameOver
    from .background_knowledge import backgroundExist

    # 착수를 통해 승리가 가능할때 착수
    for point in available_betting_point_address:
        map[point[0]][point[1] - 1] = turn
        game_over = gameOver(map, [point[0], point[1] - 1], turn)[0]
        map[point[0]][point[1]-1] = 0
        if game_over:
            print("CPU has made a judgment based on setted rule.")
            print("( Winning move founded )")
            return point[0], point[1]
    # 착수를 통해 패배를 막는것이 가능할때 착수
    for point in available_betting_point_address:
        map[point[0]][point[1] - 1] = turn*-1
        game_over = gameOver(map, [point[0], point[1] - 1], turn)[0]
        map[point[0]][point[1]-1] = 0
        if game_over:
            print("CPU has made a judgment based on setted rule.")
            print("( Defeat preventing move founded )")
            return point[0], point[1]
    # 첫 4수는 사전에 정해진 방식대로 착수
    background_exist, best_point_address = backgroundExist(state, available_betting_point_address)
    # 첫 4수 이후
    if not background_exist:
        start_time = time.time()    #시간 제한을 15초로 설정
        print("( CPU is thinking now )")
        # 제한시간 동안 minmax algorithm 으로 승리하는 수를 탐색
        best_score, best_point_address = pointFinder(map,turn,turn_count, available_betting_point_address, -21, start_time)
        # 제한시간 안에 탐색을 마치지 못했을때 rule base 기반의 착수
        if best_score == -100:
            print("CPU has made a judgment based on setted rule.")
            best_point_address = ruleBasedSystem(available_betting_point_address, last_betting_point)
        else:
            print("CPU has made a judgment based on search algorithm.")
    else:
        print("CPU has made a judgment based on background knowledge.")
    best_row = best_point_address[0]
    best_column = best_point_address[1]
    return best_row, best_column