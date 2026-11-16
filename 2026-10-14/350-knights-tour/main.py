def tostring(board):
    line = n * '+-' + '+'
    ret = line + '\n'
    for row in board:
        t = '|' + ('|'.join(row)) + '|'
        ret += t + '\n' + line + '\n'
    return ret

def bt(board):
    n = len(board)
    # find out how many knights were already placed
    m = None # the max integer placed in board starting with '0'
    mr, mc = None, None
    for r, row in enumerate(board):
        for c, value in enumerate(row):
            if value == ' ':
                continue
            else:
                i = int(value)
                if m == None:
                    m, mr, mc = i, r, c
                else:
                    if i > m:
                        m, mr, mc = i, r, c
    if m == None:
        for r in range(n):
            for c in range(n):
                board[r][c] = '0'
                flag = bt(board)
                if flag:
                    return True
                else:
                    board[r][c] = ' ' # something wrong in the future. undo.
        return False
    else:
        for (r,c) in options:
            board[r][c] = str(m + 1)
            flag = bt(board)
            if flag:
                return True
            else:
                board[r][c] = ' ' # something wrong in the future. undo.
        return False
    
if __name__ == '__main__':
    n = int(input("n: "))
    board = [[' ' for _ in range(n)] for _ in range(n)]
    board[0][0] = '0'
    board[1][2] = '1'
    print(tostring(board))
    bt(board)
