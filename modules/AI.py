# state 설정 함수
def initialMapSetter(map, state, turn):
    dot = [['.'] * 7 for i in range(6)]
    for i in range(len(state)):
        if turn == 1:
            for j in range(6):
                if map[j][int(state[i]) - 1] == 0:
                    map[j][int(state[i]) - 1] = 1
                    break
        else:
            for j in range(6):
                if map[j][int(state[i]) - 1] == 0:
                    map[j][int(state[i]) - 1] = -1
                    break
        turn *= -1
    for i in range(6):
        for j in range(7):
            if map[i][j] == 1:
                dot[i][j] = '○'
            elif map[i][j] == -1:
                dot[i][j] = '●'
            else:
                dot[i][j] = '.'
    print()
    print("# 1 2 3 4 5 6 7 #")
    print('F', dot[5][0], dot[5][1], dot[5][2], dot[5][3], dot[5][4], dot[5][5], dot[5][6], '#')
    print('E', dot[4][0], dot[4][1], dot[4][2], dot[4][3], dot[4][4], dot[4][5], dot[4][6], '#')
    print('D', dot[3][0], dot[3][1], dot[3][2], dot[3][3], dot[3][4], dot[3][5], dot[3][6], '#')
    print('C', dot[2][0], dot[2][1], dot[2][2], dot[2][3], dot[2][4], dot[2][5], dot[2][6], '#')
    print('B', dot[1][0], dot[1][1], dot[1][2], dot[1][3], dot[1][4], dot[1][5], dot[1][6], '#')
    print('A', dot[0][0], dot[0][1], dot[0][2], dot[0][3], dot[0][4], dot[0][5], dot[0][6], '#')
    print("# # # # # # # # #")
    print()
    print("You: ○ , CPU: ●")
    return map, turn

# 특정 열의 score를 찾아주는 함수
def bestScoreFinder(map,turn,turn_count,available_betting_point_address, best_score):
    # Import
    from .progressing import gameOver
    from .betting import declareAvailableBettingPoint

    for point in available_betting_point_address:
        map[point[0]][point[1] - 1] = turn

        # 테스트용 코드
        # if turn == -1:
        #     print("내",int(turn_count/2)+1,"번째 차례 예측을 시작합니다.")
        #     print("내가",str(point[1])+"열에 뒀을때")
        # else:
        #     print("상대방",int(turn_count/2)+1,"번째 차례 예측을 시작합니다.")
        #     print("상대방이", str(point[1]) + "열에 뒀을때")

        # 테스트용 코드
        # dot = [['.'] * 7 for i in range(6)]
        # for i in range(6):
        #     for j in range(7):
        #         if map[i][j] == 1:
        #             dot[i][j] = '○'
        #         elif map[i][j] == -1:
        #             dot[i][j] = '●'
        #         else:
        #             dot[i][j] = '.'
        # print()
        # print("# 1 2 3 4 5 6 7 #")
        # print('F', dot[5][0], dot[5][1], dot[5][2], dot[5][3], dot[5][4], dot[5][5], dot[5][6], '#')
        # print('E', dot[4][0], dot[4][1], dot[4][2], dot[4][3], dot[4][4], dot[4][5], dot[4][6], '#')
        # print('D', dot[3][0], dot[3][1], dot[3][2], dot[3][3], dot[3][4], dot[3][5], dot[3][6], '#')
        # print('C', dot[2][0], dot[2][1], dot[2][2], dot[2][3], dot[2][4], dot[2][5], dot[2][6], '#')
        # print('B', dot[1][0], dot[1][1], dot[1][2], dot[1][3], dot[1][4], dot[1][5], dot[1][6], '#')
        # print('A', dot[0][0], dot[0][1], dot[0][2], dot[0][3], dot[0][4], dot[0][5], dot[0][6], '#')
        # print("# # # # # # # # #")
        # print()
        # print("You: ○ , CPU: ●")

        # 테스트용 코드
        # if turn == -1:
        #     print("내", int(turn_count / 2) + 1, "번째 차례 기존베스트 스코어: ", best_score)
        # else:
        #     print("상대방", int(turn_count / 2) + 1, "번째 차례 기존베스트 스코어: ", best_score)

        # 게임 오버 됐는지
        game_over, winner = gameOver(map, [point[0], point[1] - 1], turn)

        if game_over:
            if winner == 1:
                score = 21 - int(turn_count/2)

                # 테스트용 코드
                # print("컴퓨터가",int(turn_count/2)+1,"번째 차례에 이깁니다.")
            elif winner == -1:
                score = (21 - int(turn_count/2))*-1

                # 테스트용 코드
                # print("컴퓨터가",int(turn_count/2)+1,"번째 차례에 집니다.")
            else:
                score = 0

                # 테스트용 코드
                # print(int(turn_count/2)+1,"번째 차례에 비깁니다.")

            # 테스트용 코드
            # print(int(turn_count/2)+1,"단계 스코어:",score)
        else:

            # 테스트용 코드
            # print("한 단계 더 찾아보겠습니다.")
            # print("-----------------")

            available_betting_point_address = declareAvailableBettingPoint(map,available_betting_point_address,1)[0]
            score = bestScoreFinder(map,turn*-1,turn_count+1,available_betting_point_address, 21*turn*-1)
        map[point[0]][point[1]-1] = 0
        if (turn == -1 and score >= best_score) or (turn == 1 and score <= best_score):
            # 테스트용 코드
            # print("스코어가", best_score, "에서", score, "으로 갱신되었습니다.")

            best_score = score

            # 테스트용 코드
            # if turn == -1:
            #     print("나",str(int(turn_count/2)+1)+"단계 베스트 스코어:", best_score)
            # else:
            #     print("상대",str(int(turn_count / 2) + 1) + "단계 베스트 스코어:", best_score)

    return best_score

# 수를 둘곳을 찾아주는 함수
def pointFinder(map, turn, turn_count, available_betting_point_address, best_score):
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

                # 테스트용 코드
                # print("컴퓨터가", int(turn_count / 2) + 1, "번째 차례에 이깁니다.")
            elif winner == -1:
                score = (21 - int(turn_count / 2)) * -1

                # 테스트용 코드
                # print("컴퓨터가", int(turn_count / 2) + 1, "번째 차례에 집니다.")
            else:
                score = 0

                # 테스트용 코드
                # print(int(turn_count / 2) + 1, "번째 차례에 비깁니다.")

        else:
            available_betting_point_address = declareAvailableBettingPoint(map, available_betting_point_address, 1)[0]
            score = bestScoreFinder(map, turn*-1, turn_count+1, available_betting_point_address, 21*turn*-1)

        map[point[0]][point[1]-1] = 0

        if (turn == -1 and score >= best_score) or (turn == 1 and score <= best_score):
            # 테스트용 코드
            # print("최종 스코어가", best_score, "에서", score, "으로 갱신되었습니다.")

            best_score = score
            best_point_address = point

            # 테스트용 코드
            # if turn == -1:
            #     print("나",str(int(turn_count/2)+1)+"단계 베스트 스코어:", best_score)
            # else:
            #     print("상대",str(int(turn_count / 2) + 1) + "단계 베스트 스코어:", best_score)

    return best_score, best_point_address

# 인공지능
def connect4AI(available_betting_point_address, map, turn, turn_count):
    best_score, best_point_address = pointFinder(map,turn,turn_count, available_betting_point_address, -21)

    # 테스트용 코드
    # print(best_point_address)

    best_row = best_point_address[0]
    best_column = best_point_address[1]


    # 테스트용 코드
    print(best_point_address,"에 두는게 제일좋음, 최종 베스트 스코어:",best_score)

    return best_row, best_column