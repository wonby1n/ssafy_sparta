"""
X   Y
1 3 5 7
1 켜진시간 3 꺼진시간
5 켜진시간 7 켜진시간
동시에 않켜짐 않되 않이이럴수가

"""
T = int(input())
for tc in range(1, T+1):
    A, B, C, D = map(int, input().split())

    light = [0] * 101

    for i in range(A+1,B+1):
        light.append(i)

    print(light)