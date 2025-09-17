T = int(input())
for test_case in range(1, T + 1):
# K = 최대 이동 정류장
# N = 종점 번호
# M = 충전기 설치된 정류장 번호 (리스트로도 따로 줌)

# 정류장을 인덱스라고 생각하고
# 충전기를 인덱스 안 숫자 개수라고 생각하자

	K, N, M = map(int, input().split())
	bus = list(map(int, input().split()))

	# 종점까지의 인덱스를 만듦
	idx = [0] * (N+1)

	# 해당하는 x(인덱스)에 충전기가 있다고 넣음
	for i in bus:
		idx[i] = 1

	# K만큼 가면서 가장 멀리 있는 1을 찾으면 됨. N 전까지
	# 못 찾으면 0 리턴
	# 현재 위치와 충전 횟수 정함
	pos = 0
	count = 0
	# 종점 N 전까지 현재 위치와 최대 이동 정류장의 합을 반복
	while pos+K < N:
		# 최대 3 이동 가능하고, 1,3 정류장에 충전기가 있으면 3에서 충전을 해야 함
		# 그러므로 그 구간 안에서 반대로 찾아야 함
		for i in range(pos+K, pos, -1):
			# 구간 안에 1이 들어있으면 (충전소가 있으면)
			if idx[i] == 1:
				pos = i # 내 위치는 i로 감
				count += 1 # 그리고 충전 횟수를 1번 올리기
				break # ← 더 이상 볼 필요 없음, 바로 while문으로 돌아감
			else:
				count = 0
				break # ← while문까지 종료, 프로그램 끝

	print(f'#{test_case} {count}')