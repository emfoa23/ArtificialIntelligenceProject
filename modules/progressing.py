# 특정 방향에 같은 수가 연속으로 몇개 존재하는지 찾아내는 함수
def continuousBetting(map, last_betting_point, row_direction, column_direction, count):
    row_address = last_betting_point[0]
    column_address = last_betting_point[1]
    next_row_address = row_address + row_direction
    next_column_address = column_address + column_direction
    if next_row_address < 0 or next_row_address > 5 or next_column_address < 0 or next_column_address > 6:
        return count
    elif map[next_row_address][next_column_address] != map[row_address][column_address]:
        return count
    else:
        next_checking_point = [next_row_address, next_column_address]
        return continuousBetting(map, next_checking_point, row_direction, column_direction, count+1)

# 게임판이 꽉 찼는지 확인하는 함수
def checkMapIsFull(map):
    for i in range(6):
        for j in range(7):
            if map[i][j] == 0:
                return False
    return True

# 게임오버 인지 확인하는 함수
def gameOver(map, last_betting_point, turn):
    winner = None
    if continuousBetting(map,last_betting_point,-1,0,0) + continuousBetting(map,last_betting_point,1,0,0) >= 3:
        winner = turn * -1
        return True, winner
    elif continuousBetting(map,last_betting_point,0,-1,0) + continuousBetting(map,last_betting_point,0,1,0) >= 3:
        winner = turn * -1
        return True, winner
    elif continuousBetting(map,last_betting_point,-1,1,0) + continuousBetting(map,last_betting_point,1,-1,0) >= 3:
        winner = turn * -1
        return True, winner
    elif continuousBetting(map,last_betting_point,-1,-1,0) + continuousBetting(map,last_betting_point,1,1,0) >= 3:
        winner = turn * -1
        return True, winner
    elif checkMapIsFull(map):
        winner = 0
        return True, winner
    else:
        return False, winner


# 게임 실행 함수
def startGame():
    # Import
    from .AI import initialMapSetter
    from .betting import declareAvailableBettingPoint, gameProgressing

    text_input = ''
    turn = 0    # 누구 차례인지 알려주는 변수. CPU: -1, 사람: 1
    map = [[0] * 7 for i in range(6)]   # 게임판. 빈칸: 0, CPU가 둔곳: -1, 사람이 둔곳: 1
    state = []  # 게임판의 착수됐던 열들을 알려주는 리스트
    is_first_turn = True    # 첫 착수임을 알려주는 변수
    turn_count = 0

    # 테스트용 코드
    set_intial_state = ''   # 시작 state를 설정해주는 변수

    available_betting_point_address = [[0,1],[0,2],[0,3],[0,5],[0,6],[0,7]]   # 착수가능한 위치를 알려주는 리스트
    while text_input != 'F' and text_input != 'f' and text_input != 'S' and text_input != 's':
        text_input = input("Will you go First or Second? (F/S) : ")

        # 테스트용 코드
        # text_input = 'f'    # 무조건 선공하기

        # 사람이 먼저 시작할때
        if text_input == 'F' or text_input == 'f':
            print()
            print("# 1 2 3 4 5 6 7 #")
            print('F . . . . . . . #')
            print('E . . . . . . . #')
            print('D . . . . . . . #')
            print('C . . . . . . . #')
            print('B . . . . . . . #')
            print('A . . . . . . . #')
            print("# # # # # # # # #")
            print()
            print("You go First.")
            turn = 1
            break
        # CPU가 먼저 시작할때
        elif text_input == 'S' or text_input == 's':
            print("CPU go First.")
            turn = -1
            break
        else:
            print("Wrong Input. Please try it again.")

    # 테스트용 코드
    while set_intial_state != 'Y' and set_intial_state != 'y' and set_intial_state != 'N' and set_intial_state != 'n':
        set_intial_state = input("Do you want to set initial state? (Y/N): ")
        # 초기 state를 설정할때
        if set_intial_state == 'Y' or set_intial_state == 'y':
            state = [int(x) for x in input("Initial State (ex. 4435): ")]
            map, turn = initialMapSetter(map, state, turn)
            turn_count = len(state)
            is_first_turn = False
            option = 1
        # 초기 state를 설정하지 않을때
        elif set_intial_state == 'N' or set_intial_state == 'n':
            state = []
            option = 0
        else:
            print("Wrong Input. Please try it again.")
    while True:
        # 착수 가능한 곳을 찾아주는 함수
        available_betting_point_address, option = declareAvailableBettingPoint(map, available_betting_point_address, option)

        # 테스트용 코드
        print("Available betting point:",available_betting_point_address)   # 배팅가능 포인트 출력

        # 게임 진행
        map, turn, last_betting_point, state, is_first_turn, turn_count = gameProgressing(map, turn, state, available_betting_point_address ,is_first_turn, turn_count)
        # 게임오버 됐는지를 알려주는 함수
        game_over, winner = gameOver(map, last_betting_point, turn)
        if game_over:
            print()
            print("---------------------------------------")
            print("-------------- Game Over --------------")
            # 사람이 이겼을 경우
            if winner == 1:
                print("--------------- You Win ---------------")
            # CPU가 이겼을 경우
            elif winner == -1:
                print("--------------- CPU Win ---------------")
            # 비겼을 경우
            else:
                print("---------------- Draw! ----------------")
            print("---------------------------------------")
            print()
            break