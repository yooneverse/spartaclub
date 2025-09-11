T = int(input())

for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]     # 띄어쓰기 있을 때

    box90 = [[0] * n for _ in range(n)]
    box180 = [[0] * n for _ in range(n)]
    box270 = [[0] * n for _ in range(n)]

    def nineo():
        for i in range(n):
            for j in range(n):
                box90[i][j] = arr[n-1-j][i]

    def oneeighto():
        for i in range(n):
            for j in range(n):
                box180[i][j] = arr[n-1-i][n-1-j]

    def twoseveno():
        for i in range(n):
            for j in range(n):
                box270[i][j] = arr[j][n-1-i]

    nineo()
    oneeighto()
    twoseveno()

    print(f'#{t}')
    for i in range(n):
        for val in box90[i]:
            print(val, end='')
        print(' ', end='')

        for val in box180[i]:
            print(val, end='')
        print(' ', end='')

        for val in box270[i]:
            print(val, end='')
        print()


