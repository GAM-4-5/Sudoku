def check(b):
    find = find_empty(b)
    if not find:
        return True
    else:
        red, stupac = find

    for i in range(1, 10):
        if valid(b, i, (red, stupac)):
            b[red][stupac] = i

            if check(b):
                return True

            b[red][stupac] = 0

    return False


def valid(b, br, poz):
    # red
    for i in range(len(b[0])):
        if b[poz[0]][i] == br and poz[1] != i:
            return False

    # stupac
    for i in range(len(b)):
        if b[i][poz[1]] == br and poz[0] != i:
            return False

    # 3x3
    box_x = poz[1] // 3
    box_y = poz[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if b[i][j] == br and (i,j) != poz:
                return False

    return True


def print_board(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(b[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(b[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i, j)  # red, stupac

    return None
