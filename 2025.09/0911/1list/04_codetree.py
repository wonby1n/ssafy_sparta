char = input()
arr = ['L','E','B','R','O','S']
N = len(arr)

result = None

for i in range(N):
    if arr[i] == char:
        result = i
    else:
        continue

print(result)