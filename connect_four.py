def showing(map, turn):
    bet = 0
    alphabet = ''
    if turn == 1:
        while bet != '1' and bet != '2' and bet != '3' and bet != '4' and bet != '5' and bet != '6' and bet != '7':
            bet = input("Where do you want to bet? (1~7) : ")
            if bet != '1' and bet != '2' and bet != '3' and bet != '4' and bet != '5' and bet != '6' and bet != '7':
                print("Wrong Input. Please try it again.")
            else:
                for i in range(6):
                    if map[i][int(bet)-1] == '.':
                        map[i][int(bet)-1] = '○'
                        break
                break
    if turn == -1:
        for i in range(6):
            if map[i][3] == '.':
                map[i][3] = '●'
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
    turn *= -1
    return map, turn

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
    map, turn = showing(map, turn)

#병수가 수정함
