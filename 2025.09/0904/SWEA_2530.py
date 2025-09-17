count = 1800
run = 0
while True:
    try:
        run += int(input())
    except EOFError:             # [EOF를 만나면] 반복 종료
        break

if count - run >= 300:
    print('Yes')

else:
    print('No')