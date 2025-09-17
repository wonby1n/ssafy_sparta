arr = [1,2,3,4,4,3,2,1,0,5,1]
N = 5
gohome = [0] * (5+1)
iwantpizza = []

for i in range(len(arr)):
    gohome[arr[i]] += 1

print(gohome)

for i in range(1, N+1):
    gohome[i] += gohome[i-1]

print(gohome)

for i in range(len(arr)-1, -1, -1):
    gohome[arr[i]] -=1
    iwantpizza[gohome[arr[i]]] = arr[i]

print(iwantpizza)