import math
def pprint(n, s):
    w = int(math.log10(n*n)) + 1
    def line(n):
        return n * ('+' + w * '-') + '+'
    print(line(n))
    for row in s:
        print('|' + ('|'.join([str(_).rjust(w) for _ in row])) + '|')
        print(line(n))
        
def bt_kt(n, s, r=None, c=None, taken=0):
    pprint(n, s)
    if r == None:
        # special case ... can pick any square
        for r in range(n):
            for c in range(n):
                s[r][c] = 1
                flag = bt_kt(n, s, r, c, 1)
                if flag:
                    return True
                else:
                    s[r][c] = ' '
        print("HAVE TO BACKTRACK!!!")
        return False
    else:
        if taken == n * n: # board is filled
            return True
        else:
            for (dr, dc) in [(-1, +2), (-2, +1),
                             (-2, -1), (-1, -2),
                             (+1, -2), (+2, -1),
                             (+2, +1), (+1, +2)]:
                r0, c0 = r + dr, c + dc
                if 0 <= r0 < n and 0 <= c0 < n and s[r0][c0] == ' ':
                    s[r0][c0] = taken + 1
                    flag = bt_kt(n, s, r0, c0, taken + 1)
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
        pprint(n, s)
    else:
        print("FAIL!!!")        
