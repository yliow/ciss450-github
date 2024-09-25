def pprint(s):
    def line(n):
        return n * '+-' + '+'
    n = len(s)
    print(line(n))
    for row in s:
        print('|' + ('|'.join(row)) + '|')
        print(line(n))
        
    
def bt_kt(s, r, c):
    pass

if __name__ == '__main__':
    n = int(input("n: "))
    print(n)
    s = [[' ' for r in range(n)] for c in range(n)]
    pprint(s)
