import logic

if __name__=='__main__':

    mat = logic.start()

while True:

    x = input("Press the command >> ")

    if x.upper() == "W":

        mat, flag = logic.move_up(mat)

        status = logic.get_current_state(mat)
        print(status)

        if status == "Game not over":
            logic.add_new_2(mat)

        else:
            break
    
    elif x.upper() == "S":

        mat, flag = logic.move_down(mat)

        status = logic.get_current_state(mat)
        print(status)

        if status == "Game not over":
            logic.add_new_2(mat)

        else:
            break
    
    elif x.upper() == "A":

        mat, flag = logic.move_left(mat)

        status = logic.get_current_state(mat)
        print(status)

        if status == "Game not over":
            logic.add_new_2(mat)

        else:
            break

    elif x.upper() == "D":

        mat, flag = logic.move_right(mat)

        status = logic.get_current_state(mat)
        print(status)

        if status == "Game not over":
            logic.add_new_2(mat)

        else:
            break

    else:
        print("Invalid Key")

    print(mat)
