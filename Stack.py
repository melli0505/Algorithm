# 백준 10828

import sys
input = sys.stdin.readline # python에서 input이 시간복잡도에 영향을 주는 케이스 2.

num = int(input())

s = []

for i in range(num):
    cmd = list(input().split()) # cmd[0]은 명령어, [1]은 있디면 값 저장
    if cmd[0] == 'push':
        s.append(cmd[1]) # list append == stack push
    elif cmd[0] == 'pop':
        print(-1) if len(s) == 0 else print(s.pop()) # 파이썬 삼항연산. list pop = stack pop
    elif cmd[0] == 'size':
        print(len(s)) # 길이 출력
    elif cmd[0] == 'empty':
        print(1) if len(s) == 0 else print(0) # 길이가 0이면 1을, 아니면 0을 출력
    else:
        print(-1) if len(s) == 0 else print(s[-1]) # 길이가 0이면 -1을, 아니면 last in 요소 출력
