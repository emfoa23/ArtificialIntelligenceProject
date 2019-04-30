def showing(map, turn): #착수 함수
    human_bet = 0
    alphabet = ''
    last_betting_point = [0] * 2
    if turn == 1:   #사람 차례
        while human_bet != '1' and human_bet != '2' and human_bet != '3' and human_bet != '4' and human_bet != '5' and human_bet != '6' and human_bet != '7':
            human_bet = input("Where do you want to bet? (1~7) : ")
            if human_bet != '1' and human_bet != '2' and human_bet != '3' and human_bet != '4' and human_bet != '5' and human_bet != '6' and human_bet != '7':
                print("Wrong Input. Please try it again.")
            else:
                for i in range(6):
                    if map[i][int(human_bet)-1] == '.':
                        map[i][int(human_bet)-1] = '○'
                        last_betting_point[0] = i
                        last_betting_point[1] = int(human_bet)-1  #마지막 착수점 저장
                        break
                break
    if turn == -1:  #컴퓨터 차례
        for i in range(6):
            cpu_bet = 3
            if map[i][cpu_bet] == '.':
                map[i][cpu_bet] = '●'
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

    print()
    print("# 1 2 3 4 5 6 7 #")
    print('F', map[5][0], map[5][1], map[5][2], map[5][3], map[5][4], map[5][5], map[5][6], '#')
    print('E', map[4][0], map[4][1], map[4][2], map[4][3], map[4][4], map[4][5], map[4][6], '#')
    print('D', map[3][0], map[3][1], map[3][2], map[3][3], map[3][4], map[3][5], map[3][6], '#')
    print('C', map[2][0], map[2][1], map[2][2], map[2][3], map[2][4], map[2][5], map[2][6], '#')
    print('B', map[1][0], map[1][1], map[1][2], map[1][3], map[1][4], map[1][5], map[1][6], '#')
    print('A', map[0][0], map[0][1], map[0][2], map[0][3], map[0][4], map[0][5], map[0][6], '#')
    print("# # # # # # # # #")
    print()
    print("You: ○ , CPU: ●")

    turn *= -1  #턴 바꾸기
    return map, turn, last_betting_point    #맵, 누구턴인지, 마지막 착수점 리턴

def gameOver(map):  #게임오버 인지 확인하는 함수
    return True

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
map = [['.'] * 7 for i in range(6)]
on_going = True
last_betting_point = [0] * 2
while text_input != 'F' and text_input != 'f' and text_input != 'S' and text_input != 's':
    text_input = input("Will you go First or Second? (F/S) : ")
    if text_input == 'F' or text_input == 'f':
        print()
        print("# 1 2 3 4 5 6 7 #")
        print('F', map[5][0], map[5][1], map[5][2], map[5][3], map[5][4], map[5][5], map[5][6], '#')
        print('E', map[4][0], map[4][1], map[4][2], map[4][3], map[4][4], map[4][5], map[4][6], '#')
        print('D', map[3][0], map[3][1], map[3][2], map[3][3], map[3][4], map[3][5], map[3][6], '#')
        print('C', map[2][0], map[2][1], map[2][2], map[2][3], map[2][4], map[2][5], map[2][6], '#')
        print('B', map[1][0], map[1][1], map[1][2], map[1][3], map[1][4], map[1][5], map[1][6], '#')
        print('A', map[0][0], map[0][1], map[0][2], map[0][3], map[0][4], map[0][5], map[0][6], '#')
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
while on_going:
    map, turn, last_betting_point = showing(map, turn)  #게임 진행
    if gameOver(map):   #게임이 끝나면 누가 이겼는지 출력
        print()
        print("-----------------------------")
        print("--------- Game Over ---------")
        if turn == 1:
            print("---------- CPU Win ----------")
        else:
            print("---------- You Win ----------")
        print("-----------------------------")
        print(last_betting_point)
        break
