a = int(input())
b = int(input())
c = int(input())

x = str(a*b*c)
y = list(x)

for i in range(11):
    cnt = 0
    for j in range(len(y)):
        if y[j] == str(i):
            cnt +=1

    print(cnt)