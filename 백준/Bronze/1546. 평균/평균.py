N = int(input())
M = list(map(int, input().split()))
high = max(M)
for i in range(N):
    M[i] = M[i] / high * 100

print(sum(M) / N)
