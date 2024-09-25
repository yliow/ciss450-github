def pprint(n, s):
    def line(n):
        return n * '+-' + '+'
    print(line(n))
    for row in s:
        print('|' + ('|'.join(row)) + '|')
        print(line(n))
        
    
def bt_kt(n, s, r=None, c=None):
    pprint(n, s)
    if r == None:
        for r in range(n):
            for c in range(n):
                s[r][c] = 1
                flag = bt_kt(n, s, r, c)
                if flag:
                    return True
                else:
                    s[r][c] = ' '
        return False
    else:
        for (dr, dc) in [(-1, +2), (-2, +1), (-2, -1), (-1, -2),
                         (+1, -2), (+2, -1), (+2, +1), (+1, +2)]:
            r0, c0 = r + dr, c + dc
            if 0 <= r0 < n and 0 <= c0 < n and s[r0][c0] == ' ':
                s[r0][c0] = s[r][c] + 1
                flag = bt_kt(n, s, r0, c0)
                if flag:
                    return True
                else:
                    s[r0][c0] = ' '
        print("HAVE TO BACKTRACK!!!")
        return False
                    
if __name__ == '__main__':
    n = int(input("n: "))
    s = [[' ' for r in range(n)] for c in range(n)]

    flag = bt_kt(n, s)
    if flag:
        print("DONE!!!")
        pprint(s)
    else:
        print("FAIL!!!")
        
