n = int(input())

while True:
    array = list(map(int, input().split()))
    a = min(array)
    b = max(array)

    if len(array) == n:
        break

print(a, b)