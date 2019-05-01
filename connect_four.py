# Import
from random import randint

# 선택한 열에 착수하는 함수
def betting(turn, map):
    human_bet = 0
    if turn == 1:   # 사람 차례
        while human_bet != '1' and human_bet != '2' and human_bet != '3' and human_bet != '4' and human_bet != '5' and human_bet != '6' and human_bet != '7':
            human_bet = input("Where do you want to bet? (1~7) : ")
            if human_bet != '1' and human_bet != '2' and human_bet != '3' and human_bet != '4' and human_bet != '5' and human_bet != '6' and human_bet != '7':
                print("Wrong Input. Please try it again.")
            else:
                for i in range(6):
                    if map[i][int(human_bet)-1] == 0:
                        map[i][int(human_bet)-1] = 1
                        last_betting_point[0] = i
                        last_betting_point[1] = int(human_bet)-1  #마지막 착수점 저장
                        print(last_betting_point)
                        return map, True, last_betting_point
                    else:
                        if i == 5:
                            print("The column is full. Please select another column.")
                            return map, False

# 착수할 열을 선택하고 착수 결과를 보여주는 함수
def showing(map, turn):
    human_bet = 0
    alphabet = ''
    last_betting_point = [0] * 2
    dot = [['.'] * 7 for i in range(6)]
    while not betting(turn, map):
        betting(turn, map)

    # if turn == 1:   #사람 차례
    #     while human_bet != '1' and human_bet != '2' and human_bet != '3' and human_bet != '4' and human_bet != '5' and human_bet != '6' and human_bet != '7':
    #         human_bet = input("Where do you want to bet? (1~7) : ")
    #
    #         # 테스트용 코드
    #         # human_bet = str(randint(1, 7))    # 사람 차례에도 랜덤하게 두기
    #
    #         if human_bet != '1' and human_bet != '2' and human_bet != '3' and human_bet != '4' and human_bet != '5' and human_bet != '6' and human_bet != '7':
    #             print("Wrong Input. Please try it again.")
    #         else:
    #             for i in range(6):
    #                 if map[i][int(human_bet)-1] == 0:
    #                     map[i][int(human_bet)-1] = 1
    #                     last_betting_point[0] = i
    #                     last_betting_point[1] = int(human_bet)-1  #마지막 착수점 저장
    #                     print(last_betting_point)
    #                     break
    #                 else:
    #                     if i == 5:
    #                         print("The column is full. Please select another column.")

    elif turn == -1:  #컴퓨터 차례
        cpu_bet = randint(0, 6)
        # cpu_bet = 6
        for i in range(6):
            if map[i][cpu_bet] == 0:
                map[i][cpu_bet] = -1
                last_betting_point[0] = i
                last_betting_point[1] = cpu_bet
                if i == 0:
                    alphabet = 'A'
                elif i == 1:
                    alphabet = 'B'
                elif i == 2:
                    alphabet = 'C'
                elif i == 3:
                    alphabet = 'D'
                elif i == 4:
                    alphabet = 'E'
                else:
                    alphabet = 'F'
                break
        print("CPU betted",alphabet+str(cpu_bet))
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

    turn *= -1  #턴 바꾸기
    return map, turn, last_betting_point    #맵, 누구턴인지, 마지막 착수점 리턴

#가로로 빙고가 존재하는지 확인하는 함수
def checkHorizontalClear(map, last_betting_point):
    column = last_betting_point[0]
    row = last_betting_point[1]
    if (row-2 < 0) and (map[column][row+1] != map[column][row]):
        return False
    elif (row+2 > 6) and (map[column][row-1] != map[column][row]):
        return False
    elif (map[column][row-1] != map[column][row]) and (map[column][row+1] != map[column][row]):
        return False
    elif (map[column][row-1] == map[column][row]) and ((row + 1 > 6) or (map[column][row+1] != map[column][row])):
        if (row - 3 < 0) or (map[column][row-2] != map[column][row]) or (map[column][row-3] != map[column][row]):
            return False
    # elif ((row - 1 < 0) or (map[column][row-1] != map[column][row])) and (map[column][row+1] == map[column][row]):
    elif (map[column][row - 1] != map[column][row]) and (map[column][row + 1] == map[column][row]):
        if (row + 3 > 6) or (map[column][row+2] != map[column][row]) or (map[column][row+3] != map[column][row]):
            return False
    else:
        if ((row - 2 < 0) or (map[column][row-2] != map[column][row])) and ((row + 2 > 6) or (map[column][row+2] != map[column][row])):
            return False
    print("가로 빙고")
    return True

#세로로 빙고가 존재하는지 확인하는 함수
def checkVerticalClear(map, last_betting_point):
    column = last_betting_point[0]
    row = last_betting_point[1]
    if (column - 2 < 0) and (map[column+1][row] != map[column][row]):
        return False
    elif (column + 2 > 5) and (map[column-1][row] != map[column][row]):
        return False
    elif (map[column-1][row] != map[column][row]) and (map[column+1][row] != map[column][row]):
        return False
    elif (map[column-1][row] == map[column][row]) and ((column + 1 > 5) or (map[column+1][row] != map[column][row])):
        if (column - 3 < 0) or (map[column-2][row] != map[column][row]) or (map[column-3][row] != map[column][row]):
            return False
    elif ((column - 1 < 0) or (map[column-1][row] != map[column][row])) and (map[column+1][row] == map[column][row]):
        if (column + 3 > 5) or (map[column+2][row] != map[column][row]) or (map[column+3][row] != map[column][row]):
            return False
    else:
        if ((column - 2 < 0) or (map[column-2][row] != map[column][row])) and ((column + 2 > 5) or (map[column+2][row] != map[column][row])):
            return False
    print("세로 빙고")
    return True

#왼쪽 대각선으로 빙고가 존재하는지 확인하는 함수
def checkLeftDiagonalClear(map, last_betting_point):
    column = last_betting_point[0]
    row = last_betting_point[1]
    if ((column-2 < 0) or (row + 2 > 6)) and ((column+2 > 5) or (row - 2 < 0)):
        return False
    elif ((column-2 < 0) or (row + 2 > 6)) and (map[column+1][row - 1] != map[column][row]):
        return False
    elif ((column+2 > 5) or (row - 2 < 0)) and (map[column-1][row + 1] != map[column][row]):
        return False
    elif (map[column+1][row - 1] != map[column][row]) and (map[column-1][row + 1] != map[column][row]):
        return False
    elif (map[column+1][row - 1] == map[column][row]) and (() or (map[column-1][row + 1] != map[column][row])):
        if (map[column+2][row - 2] != map[column][row]) or (map[column+3][row - 3] != map[column][row]):
            return False
    elif (map[column+1][row - 1] != map[column][row]) and (() or (map[column-1][row + 1] == map[column][row])):
        if (map[column-2][row + 2] != map[column][row]) or (map[column-3][row + 3] != map[column][row]):
            return False
    else:
        if ((column+2 > 5) or (row - 2 < 0) or (map[column+2][row - 2] != map[column][row])) and ((column+2 > 5) or (row - 2 < 0) or (map[column+2][row - 2] != map[column][row])):
            return False
    print("왼쪽 대각 빙고")
    return True

#오른쪽 대각선으로 빙고가 존재하는지 확인하는 함수
def checkRightDiagonalClear(map, last_betting_point):
    column = last_betting_point[0]
    row = last_betting_point[1]
    if((column - 2 < 0) or (row - 2 < 0)) and ((column + 2 > 5) or (row + 2 > 6)):
        return False
    elif ((column - 2 < 0) or (row - 2 < 0)) and (map[column + 1][row + 1] != map[column][row]):
        return False
    elif ((column + 2 > 5) or (row + 2 > 6)) and (map[column - 1][row - 1] != map[column][row]):
        return False
    elif (map[column - 1][row - 1] != map[column][row]) and (map[column + 1][row + 1] != map[column][row]):
        return False
    elif (map[column - 1][row - 1] == map[column][row]) and ((column + 1 > 5) or (row + 1 > 6) or (map[column + 1][row + 1] != map[column][row])):
        if (map[column - 2][row - 2] != map[column][row]) or (map[column - 3][row - 3] != map[column][row]):
            return False
    elif (map[column - 1][row - 1] != map[column][row]) and ((column + 1 > 5) or (row + 1 > 6) or (map[column + 1][row + 1] == map[column][row])):
        if (map[column + 2][row + 2] != map[column][row]) or (map[column + 3][row + 3] != map[column][row]):
            return False
    else:
        if ((column - 2 < 0) or (row - 2 < 0) or (map[column - 2][row - 2] != map[column][row])) and ((column + 2 > 5) or (row + 2 > 6) or (map[column + 2][row + 2] != map[column][row])):
            return False
    print("오른쪽 대각 빙고")
    return True

#게임판이 꽉 찼는지 확인하는 함수
def checkMapIsFull(map):
    for i in range(6):
        for j in range(7):
            if map[i][j] == 0:
                return False
    return True

#게임오버 인지 확인하는 함수
def gameOver(map, last_betting_point, turn):
    winner = None
    # if checkHorizontalClear(map, last_betting_point):
    #     winner = turn * -1
    #     return True, winner
    # elif checkVerticalClear(map, last_betting_point):
    #     winner = turn * -1
    #     return True, winner
    # elif checkLeftDiagonalClear(map, last_betting_point):
    #     winner = turn * -1
    #     return True, winner
    # elif checkRightDiagonalClear(map, last_betting_point):
    #     winner = turn * -1
    #     return True, winner
    # elif checkMapIsFull(map):
    #     winner = 0
    #     return True, winner
    # else:
    #     return False, winner

    # 테스트용 코드
    return False, winner    # 무조건 게임 진행

# 게임 실행 함수
def startGame():
    text_input = ''
    turn = 0
    map = [[0] * 7 for i in range(6)]
    last_betting_point = [0] * 2
    while text_input != 'F' and text_input != 'f' and text_input != 'S' and text_input != 's':
        text_input = input("Will you go First or Second? (F/S) : ")
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
        elif text_input == 'S' or text_input == 's':
            print("CPU go First.")
            turn = -1
            break
        else:
            print("Wrong Input. Please try it again.")
    while True: #게임 진행 함수
        map, turn, last_betting_point = showing(map, turn)
        game_over, winner = gameOver(map, last_betting_point, turn)
        if game_over:   #게임이 끝나면 누가 이겼는지 출력
            print()
            print("-----------------------------")
            print("--------- Game Over ---------")
            if winner == 1:
                print("---------- You Win ----------")
            elif winner == -1:
                print("---------- CPU Win ----------")
            else:
                print("----------- Draw! -----------")
            print("-----------------------------")
            print()
            break

# 메인 함수
game_continue = ''
print()
print("------------------------------")
print("Artificial Intellgence Project")
print("-------- Connect Four --------")
print("-------- Human vs CPU --------")
print("------------------------------")
print()
startGame()
while game_continue != 'Y' and game_continue != 'y' and game_continue != 'N' and game_continue != 'n':
    game_continue = input("Do you want to restart the game? (Y/N) : ")
    if game_continue == 'Y' or game_continue == 'y':
        print()
        print("------------------------------")
        print("-------- Game Restart --------")
        print("------------------------------")
        print()
        startGame()
    elif game_continue == 'N' or game_continue == 'n':
        print()
        print("------------------------------")
        print("--- Game Engine Terminated ---")
        print("------------------------------")
        print()
        break
    else:
        print("Wrong Input. Please try it again.")