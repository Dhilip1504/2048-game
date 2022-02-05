board = [[0, 16, 0, 0], [0, 2, 0, 0], [0, 0, 0, 4], [0, 0, 0, 0]]


def display():

    largest = board[0][0]
    for row in board:
        for element in row:
            if element > largest:
                largest = element

    numSpaces = len(str(largest))

    for row in board:
        currRow = '|'
        for element in row:
            if element == 0:
                currRow += " " * numSpaces + '|'
            else:
                currRow += " " * (numSpaces - len(str(element))
                                  ) + str(element) + '|'

        print(currRow)
    print()


display()
