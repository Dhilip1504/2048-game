board = [[0, 0, 0, 0], [0, 2, 0, 0], [0, 0, 0, 4], [0, 0, 0, 0]]


def display():
    for row in board:
        currRow = '|'
        for element in row:
            if element == 0:
                currRow += ' |'
            else:
                currRow += str(element) + '|'

        print(currRow)
    print()


display()
