a = '다들힘내'

b = ''
for i in range(len(a)-1, -1, -1):
    b += a[i]

# print(b)

A = len(a)
for i in range(A//2):
    if a[i] != a[A-1-i]:
        print('다르네')
    else:
        print('같아용')