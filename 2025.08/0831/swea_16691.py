T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    graph = list(map(int, input().split()))

    cleft = [0] * (E+2)
    cright = [0] * (E+2)

    for i in range(E):
        p = [i*2]
        c = [i*2+1]

        if cleft[p] == 0:
            cleft[p] = c
        elif cright[p] == 0:
            cright[p] = c

def subtree(t):
