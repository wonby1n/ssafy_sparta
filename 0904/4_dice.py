# 주사위 3개를 던져서 합이 10 이하인 케이스의 수

path = [] # 무조건 기존 주사위를 기록해놔야 할까...?
result = 0

def recur(cnt):
    global result

    # 이미 10을 넘은 경우는 더 볼 필요가 없다
    # 기저 조건에서 많은 경우의 수들을 줄일 수 있다
    if sum(path) > 10:
        return

    # 종료조건 : 주사위 3개를 던지면
    if cnt == 3:
        if sum(path) <= 10:
            print(*path)
            result += 1

        return

    for num in range(1, 7):
        path.append(num)
        recur(cnt + 1)
        path.pop()

recur(0)

# 누적합을 활용하는 버전 ----------------------
def recur(cnt, total):
    global result

    # 이미 10을 넘은 경우는 더 볼 필요가 없다
    # 기저 조건에서 많은 경우의 수들을 줄일 수 있다
    if total > 10:
        return

    # 종료조건 : 주사위 3개를 던지면
    if cnt == 3:
        result += 1
        return

    for num in range(1, 7):
        recur(cnt + 1, total + num)

result = 0
recur(0,0)
print(result)