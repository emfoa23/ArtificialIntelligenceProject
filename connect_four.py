# Import
from random import randint

# 착수 가능한 곳을 찾아주는 함수
def declareAvailableBettingPoint(map, available_betting_point_address, option):
    new_available_betting_point_address = []
    # initial state이 주어지지 않았을때
    if option == 0:
        for point in available_betting_point_address:
            if map[point[0]][point[1]-1] == 0:
                new_available_betting_point_address.append(point)
            elif point[0] + 1 < 6:
                new_available_betting_point_address.append([point[0]+1, point[1]])
    # initial state이 주어졌을때
    elif option == 1:
        for i in range(7):
            for j in range(6):
                if map[j][i] == 0:
                    new_available_betting_point_address.append([j,i+1])
                    break
        option = 0
    return new_available_betting_point_address, option

# 선택한 열에 착수하는 함수
def betting(turn, map, available_betting_point_address):
    human_bet = 0
    last_betting_point = [-1] * 2
    # 사람 차례
    if turn == 1:
        while human_bet != '1' and human_bet != '2' and human_bet != '3' and human_bet != '4' and human_bet != '5' and human_bet != '6' and human_bet != '7':
            human_bet = input("Where do you want to bet? (1~7) : ")

            # 테스트용 코드
            # human_bet = str(randint(1, 7))    # 사람 차례에도 랜덤하게 두기

            if human_bet != '1' and human_bet != '2' and human_bet != '3' and human_bet != '4' and human_bet != '5' and human_bet != '6' and human_bet != '7':
                print("Wrong Input. Please try it again.")
            else:
                for point in available_betting_point_address:
                    if int(human_bet) == point[1]:
                        map[point[0]][int(human_bet)-1] = 1
                        # 마지막 착수점 저장
                        last_betting_point[0] = point[0]
                        last_betting_point[1] = int(human_bet) - 1
                        return map, True, last_betting_point
                print("Column " + human_bet + " is already full. Please select another column.")
                return map, False, last_betting_point
    # 컴퓨터 차례
    else:
        cpu_input = -1
        while cpu_input != '0' and cpu_input != '1':
            cpu_input = input("Choose betting method CPU should select. (0 - random / 1 - heuristic): ")
            if int(cpu_input) == 0:
                # 1~7열 사이에 랜덤하게 착수하기
                random_variable = randint(0, len(available_betting_point_address)-1)
                cpu_bet_row = available_betting_point_address[random_variable][0]
                cpu_bet_column = available_betting_point_address[random_variable][1]
            elif int(cpu_input) == 1:
                # 1~7열 사이에 랜덤하게 착수하기
                random_variable = randint(0, len(available_betting_point_address)-1)
                cpu_bet_row = available_betting_point_address[random_variable][0]
                cpu_bet_column = available_betting_point_address[random_variable][1]
            else:
                print("Wrong Input. Please try it again.")
        map[cpu_bet_row][cpu_bet_column-1] = -1
        # 마지막 착수점 저장
        last_betting_point[0] = cpu_bet_row
        last_betting_point[1] = cpu_bet_column - 1
        if last_betting_point[0] == 0:
            alphabet = 'A'
        elif last_betting_point[0] == 1:
            alphabet = 'B'
        elif last_betting_point[0] == 2:
            alphabet = 'C'
        elif last_betting_point[0] == 3:
            alphabet = 'D'
        elif last_betting_point[0] == 4:
            alphabet = 'E'
        else:
            alphabet = 'F'
        print("( CPU betted",alphabet+str(cpu_bet_column),")")
        return map, True, last_betting_point

# 착수할 열을 선택하고 착수 결과를 보여주는 함수
def gameProgressing(map, turn, state ,available_betting_point_address):
    success_betting = False
    dot = [['.'] * 7 for i in range(6)]
    print("---------------------------------------")
    while not success_betting:
        map, success_betting, last_betting_point = betting(turn, map, available_betting_point_address)
    state.append(last_betting_point[1]+1)
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

    # 테스트용 코드
    print("State: "+''.join(str(i) for i in state))    # 현재 state 보여주기

    turn *= -1  # 턴 바꾸기
    return map, turn, last_betting_point, state    # 맵, 누구턴인지, 마지막 착수점, state 리턴

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

# 게임 실행 함수
def startGame():
    text_input = ''
    turn = 0    # 누구 차례인지 알려주는 변수. CPU: -1, 사람: 1
    map = [[0] * 7 for i in range(6)]   # 게임판. 빈칸: 0, CPU가 둔곳: -1, 사람이 둔곳: 1
    state = []  # 게임판의 착수됐던 열들을 알려주는 리스트

    # 테스트용 코드
    set_intial_state = ''   # 시작 state를 설정해주는 변수

    available_betting_point_address = [[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7]]   # 착수가능한 위치를 알려주는 리스트
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
        map, turn, last_betting_point, state = gameProgressing(map, turn, state, available_betting_point_address)
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

# 메인 함수
game_continue = ''  # 게임이 한판 끝났을때 재시작할지에 대한 변수
print()
print("----------------------------------------")
print("---- Artificial Intellgence Project ----")
print("------------- Connect Four -------------")
print("------------- Human vs CPU -------------")
print("----------------------------------------")
print()
# 게임 실행 함수
startGame()
while game_continue != 'Y' and game_continue != 'y' and game_continue != 'N' and game_continue != 'n':
    game_continue = input("Do you want to restart the game? (Y/N) : ")

    # 테스트용 코드
    # game_continue = 'y' # 게임 무한 재실행

    # 게임 재시작을 원할때
    if game_continue == 'Y' or game_continue == 'y':
        print()
        print("----------------------------------------")
        print("------------- Game Restart -------------")
        print("----------------------------------------")
        print()
        game_continue = ''
        startGame()
    # 게임 재시작을 원하지 않을때
    elif game_continue == 'N' or game_continue == 'n':
        print()
        print("----------------------------------------")
        print("-------- Game Engine Terminated --------")
        print("----------------------------------------")
        print()
        break
    else:
        print("Wrong Input. Please try it again.")