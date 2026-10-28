def tostring(board):
    n = len(board)
    line = n * '+--' + '+' + '\n'
    ret = line 
    for row in board:
        t = '|' + '|'.join(["%2s" % val for val in row]) + '|' + '\n'
        ret += t
        ret += line
    return ret

def bt(board):
    n = len(board)
    # find max (i.e. m) value in board where (mr,mc) is location of m.
    m, mr, mc = None, None, None
    for r, row in enumerate(board):
        for c, val in enumerate(row):
            if val != ' ':
                i = int(val)
                if m == None:
                    m, mr, mc = i, r, c
                else:
                    if i > m:
                        m, mr, mc = i, r, c
    #print("m,mr,mc:", m, mr, mc)
    print("m:", m)
    if m == n * n - 1:
        # base case
        return True
     
    if m == None:
        for r in range(n):
            for c in range(n):
                board[r][c] = '0'
                flag = bt(board)
                if flag: return True
                board[r][c] = ' '
        return False
    else:
        dr_dc_s = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                   (2, 1), (2, -1), (-2 , 1), (-2, -1)]
        options = []
        for dr, dc in dr_dc_s:
            r, c = mr + dr, mc + dc
            if 0 <= r < n and 0 <= c < n and board[r][c] == ' ':
                options.append((r, c))
        for r, c in options:
            board[r][c] = str(m + 1)
            flag = bt(board)
            if flag: return True
            board[r][c] = ' '
        return False
                    
if __name__ == '__main__':
    n = int(input("n? "))
    board = [[' ' for _ in range(n)] for _ in range(n)]
    #print(tostring(board))
    flag = bt(board)
    if flag:
        print("SUCCESS")
        print(tostring(board))
    else:
        print("FAILURE")
