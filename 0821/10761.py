"""
버튼 1에서 100까지 100개
오렌지 블루 둘 다 버튼 1에서 시작
4
B2 O1 O2 B4


o 2 o 1
오렌지가 2로 감, 1초
오렌지가 2를 누름, 1초
오렌지가 1로 감, 1초
오렌지가 1을 누름, 1초

B가 2로 감, 1초
B가 2를 누름, 2초
O가 1을 누름 B가 3으로 감, 3초
O가 2로 감 B가 4로 감, 4초
O가 2를 누름, 5초
B가 4를 누름, 6초
"""

T = int(input())
for tc in range(1, T+1):
    # 눌러야 하는 버튼의 개수 N
    # 버튼 N개 한 줄에 주어짐
    arr = list(input().split())
    N = int(arr[0])
    button = arr[1:]
    push = 0

    while push != 4:
        for i in range(2):
            if arr[i] == 'B':
