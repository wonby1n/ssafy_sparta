a = 0
b = 0
for _ in range(5):
    a = int(input())
    if a < 40:
        a = 40
    b += a
print(b//5)