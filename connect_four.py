print("------------------------------")
print("Artificial Intellgence Project")
print("-------- Connect Four --------")
print("-------- Human vs CPU --------")
print("------------------------------")
order = ''
while order != 'F' and order != 'f' and order != 'S' and order != 's':
    order = input("Will you go First or Second? (F/S) : ")
    if order == 'F' or order == 'f':
        print("You decided to fo First.")
        break
    elif order == 'S' or order == 's':
        print("You decided to fo Second.")
        break
    else:
        print("Wrong Input. Please try it again.")