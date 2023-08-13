N = int(input())

T = [0]
P = [0]
dp = [0] * 100

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

# i + T_i 가 N보다 크면 dp 최댓값 갖고오기
# i + T_i 가 N보다 작거나 같으면 i + T_i부터 N 사이에서 dp 최댓값 갖고온 다음 P_i 더해서 저장
for i in range(N):
    i = N - i
    if i + T[i] > N + 1:
        max = dp[i + 1]
        for j in range(i + 1, N + 1):
            if max < dp[j]:
                max = dp[j]
        dp[i] = max
    else:
        max = dp[i + T[i]]
        for j in range(i + T[i], N + 1):
            if max < dp[j]:
                max = dp[j]
        dp[i] = max + P[i]

max = 0
for i in dp:
    if max < i:
        max = i
print(max)
