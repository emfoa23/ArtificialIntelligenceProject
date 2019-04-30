def showing(map, turn): #착수 함수
    human_bet = 0
    alphabet = ''
    last_betting_point = [0] * 2
    dot = [['.'] * 7 for i in range(6)]
    if turn == 1:   #사람 차례
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
                        break
                break
    elif turn == -1:  #컴퓨터 차례
        for i in range(6):
            cpu_bet = 3
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
        print("CPU betted",alphabet+str(3))
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


def checkHorizontalClear(map, last_betting_point):
    column = last_betting_point[0]
    row = last_betting_point[1]
    if (row-2 < 0) and (map[column][row+1] != map[column][row]):
        return False
    elif (row+2 > 6) and (map[column][row-1] != map[column][row]):
        return False
    elif (map[column][row-1] != map[column][row]) and (map[column][row+1] != map[column][row]):
        return False
    elif (map[column][row-1] == map[column][row]) and  (map[column][row+1] != map[column][row]):
        if (map[column][row-2] != map[column][row]) or (map[column][row-3] != map[column][row]):
            return False
    elif (map[column][row-1] != map[column][row]) and  (map[column][row+1] == map[column][row]):
        if (map[column][row+2] != map[column][row]) or (map[column][row+3] != map[column][row]):
            return False
    else:
        if (map[column][row-2] != map[column][row]) and (map[column][row+2] != map[column][row]):
            return False
    print("가로 빙고")
    return True
def checkVerticalClear(map, last_betting_point):
    column = last_betting_point[0]
    row = last_betting_point[1]
    if (column - 2 < 0) and (map[column+1][row] != map[column][row]):
        return False
    elif (column + 2 > 5) and (map[column-1][row] != map[column][row]):
        return False
    elif (map[column-1][row] != map[column][row]) and (map[column+1][row] != map[column][row]):
        return False
    elif (map[column-1][row] == map[column][row]) and (map[column+1][row] != map[column][row]):
        if (map[column-2][row] != map[column][row]) or (map[column-3][row] != map[column][row]):
            return False
    elif (map[column-1][row] != map[column][row]) and (map[column+1][row] == map[column][row]):
        if (map[column+2][row] != map[column][row]) or (map[column+3][row] != map[column][row]):
            return False
    else:
        if (map[column-2][row] != map[column][row]) and (map[column+2][row] != map[column][row]):
            return False
    print("세로 빙고")
    return True
def checkLeftDiagonalClear(map, last_betting_point):
    column = last_betting_point[0]
    row = last_betting_point[1]
    if ((column-2 < 0) or (row + 2 > 6)) and (map[column+1][row - 1] != map[column][row]):
        return False
    elif ((column+2 > 5) or (row - 2 < 0)) and (map[column-1][row + 1] != map[column][row]):
        return False
    elif (map[column+1][row - 1] != map[column][row]) and (map[column-1][row + 1] != map[column][row]):
        return False
    elif (map[column+1][row - 1] == map[column][row]) and (map[column-1][row + 1] != map[column][row]):
        if (map[column+2][row - 2] != map[column][row]) or (map[column+3][row - 3] != map[column][row]):
            return False
    elif (map[column+1][row - 1] != map[column][row]) and (map[column-1][row + 1] == map[column][row]):
        if (map[column-2][row + 2] != map[column][row]) or (map[column-3][row + 3] != map[column][row]):
            return False
    else:
        if (map[column+2][row - 2] != map[column][row]) and (map[column+2][row - 2] != map[column][row]):
            return False
    print("왼쪽 대각 빙고")
    return True
def checkRightDiagonalClear(map, last_betting_point):
    column = last_betting_point[0]
    row = last_betting_point[1]
    if ((column - 2 < 0) or (row - 2 < 0)) and (map[column + 1][row + 1] != map[column][row]):
        return False
    elif ((column + 2 > 5) or (row + 2 > 6)) and (map[column - 1][row - 1] != map[column][row]):
        return False
    elif (map[column - 1][row - 1] != map[column][row]) and (map[column + 1][row + 1] != map[column][row]):
        return False
    elif (map[column - 1][row - 1] == map[column][row]) and (map[column + 1][row + 1] != map[column][row]):
        if (map[column - 2][row - 2] != map[column][row]) or (map[column - 3][row - 3] != map[column][row]):
            return False
    elif (map[column - 1][row - 1] != map[column][row]) and (map[column + 1][row + 1] == map[column][row]):
        if (map[column + 2][row + 2] != map[column][row]) or (map[column + 3][row + 3] != map[column][row]):
            return False
    else:
        if (map[column - 2][row - 2] != map[column][row]) and (map[column + 2][row + 2] != map[column][row]):
            return False
    print("오른쪽 대각 빙고")
    return True

def gameOver(map, last_betting_point):  #게임오버 인지 확인하는 함수
    if checkHorizontalClear(map, last_betting_point):
        return True
    elif checkVerticalClear(map, last_betting_point):
        return True
    elif checkLeftDiagonalClear(map, last_betting_point):
        return True
    elif checkRightDiagonalClear(map, last_betting_point):
        return True
    else:
        return False


#메인 함수
print()
print("------------------------------")
print("Artificial Intellgence Project")
print("-------- Connect Four --------")
print("-------- Human vs CPU --------")
print("------------------------------")
print()
text_input = ''
turn = 0
map = [[0] * 7 for i in range(6)]
on_going = True
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
while on_going: #게임 진행 함수
    map, turn, last_betting_point = showing(map, turn)
    if gameOver(map, last_betting_point):   #게임이 끝나면 누가 이겼는지 출력
        print()
        print("-----------------------------")
        print("--------- Game Over ---------")
        if turn == 1:
            print("---------- CPU Win ----------")
        else:
            print("---------- You Win ----------")
        print("-----------------------------")
        break
