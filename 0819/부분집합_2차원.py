grid = [
    [1, 2, 3],
    [4, 5, 6],
]
R = len(grid)
C = len(grid[0])

def make_sum(idx, selected):

    # 종료 조건
    if idx == R * C:
        return


    # 자기 자신을 호출
