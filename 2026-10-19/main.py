def tostring(board):
    n = len(board)
    line = n * '+-' + '+' + '\n'
    ret = line 
    for row in board:
        t = '|' + '|'.join(row) + '|' + '\n'
        ret += t
        ret += line
    return ret

def bt(board):
    n = len(board)
    m, mr, mc = None, None, None
    for r, row in enumerate(board):
        for c, val in enuemrate(row):
            if val != ' ':
                i = int(val)
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
                board[r][c] = ' '
        return False
    else:
        options = ...
        for r, c in options:
            board[r][c] = str(m + 1)
            flag = bt(board)
            if flag:
                return True
            board[r][c] = ' '
        return False
            
                    
if __name__ == '__main__':
    n = int(input("n? "))
    board = [[' ' for _ in range(n)] for _ in range(n)]
    board[0][0] = '0'
    board[1][2] = '1'
    print(board)
    print(tostring(board))
    
