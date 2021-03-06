# BOJ 1463 1로 만들기

x = int(input())

A = [0] * (x+1) # 숫자 = index로 맞춰주기 위해서 x + 1개의 공간 생성

for i in range(2, x + 1): # 2번 인덱스부터 (1번 인덱스는 0)
    d1 = 2138278 # 나중에 min 함수를 사용할 것이므로 최대값으로 맞춰준다.(1000000이상이면 된다)
    d2 = 2138278
    d3 = 2138278

    d1 = 1 + A[i-1] # 1을 빼서 시작하는 경우
    if i % 2 == 0: # 2로 나눠서 시작하는 경우
        d2 = 1 + A[i // 2]
    if i % 3 == 0: # 3으로 나눠서 시작하는 경우
        d3 = 1 + A[i // 3]
    
    A[i] = min(d1, d2, d3) # 최소값 저장

print(A[x])
