T = int(input())
for tc in range(1, T+1):
    # N : 세로크기
    # M : 가로크기
    N, M = map(int, input().split())

    code_table = {'0001101':0,
                  '0011001':1,
                  '0010011':2,
                  '0111101':3,
                  '0100011':4,
                  '0110001':5,
                  '0101111':6,
                  '0111011':7,
                  '0110111':8,
                  '0001011':9
                  }

    code_table.get('0001101')

    # 1 또는 0으로 구성된 암호코드가 포함된 문자열 배열
    matrix = [input() for _ in range(N)]

    found = False
    for i in range(N):
            # j는 열 번호인데 뒤에서부터 1 찾기 시작
            # 왜 1을 찾느냐? 모든 암호코드는 다 1로 끝난다
            # 0으로 시작하는 것도 당연하긴 한데 0이 암호코드에 포함되는지 아닌지 확인
        for j in range(M-1,55,-1):
            if matrix[i][j] == '1':
                    # 암호코드가 끝나는 위치 j를 발견했으니까
                    # [j-55, j]가 암호코드 후보 범위
                code = matrix[i][j-55:j+1]
                    # code를 앞에서부터 7개씩 잘라서 code_table에 일치하는 코드가 있는지 확인
                found = True
                break
        if found:
            break

    result = []
    for c in range(0,56,7):
        result.append(code_table.get(code[c:c+7]))

    R = len(result)
    # 1, 3, 5, 7 (짝수번째 자리)
    odd = 0
    # 0, 2, 4, 6 (홀수번째 자리)
    even = 0
    for i in range(R):
        if i % 2 == 0:
            even += result[i]
        else:
            odd += result[i]

    if ((even*3) + odd) % 10 == 0:
        answer = odd + even
    else:
        answer = 0

    print(answer)