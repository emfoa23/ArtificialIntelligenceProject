# Import
from modules.progressing import startGame

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