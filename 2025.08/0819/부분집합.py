lst = [1,2,3,4,5]
N = len(lst)
selected = [0] * N

def make_set(idx, selected):

    # 종료 조건
    if idx == N:
        # selected 배열 보고 해당하는 부분집합 출력하기
        # subset는 selected이 1인 애들 넣는 곳
        subset = []
        for i in range(N):
            # 만약 selected가 1이라면
            if selected[i]:
                subset.append(lst[i])
        print(subset)
        return

    # 자기 자신을 호출
    # idx번 원소를 부분집합 selected에 넣고, 그 다음번 원소를 판단하기
    selected[idx] = 1
    make_set(idx+1, selected)

    # idx번 원소를 넣지 않고 그 다음번 원소를 판단하기
    selected[idx] = 0
    make_set(idx+1, selected)

make_set(0, selected)
