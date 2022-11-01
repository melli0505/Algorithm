# 20519 백준
# 브루트 포스 알고리즘을 통해서 모든 경우를 검사했다. 처음에는 리스트를 슬라이싱해서 거리를 계산하는 함수를 만들었는데, 
# 리스트를 이용하려다 보니 index out of range 에러가 종종 발생해서 단순하게 반복문을 이용하는 방식으로 변경했다.
# 그 이후에도 삼중 for문 + while문을 사용했기 때문에 계속해서 시간초과 문제가 있었는데 이 부분은 비둘기 집 원리로 해결했다.

import sys # input 함수도 시간복잡도에 영향을 준다.
input = sys.stdin.readline

test = int(input())

while test:
    test -= 1
    person = int(input())
    mbti = list(map(str, input().split()))
    
    minn = 200 # 최대치, 적당한 값으로 잡기
    i=0

    if person > 32: # 비둘기 집 원리. 시간초과 잡는 방법
        print(0)
    else: # 브루트 포스
        for i in range(person):
            for j in range(person):
                for o in range(person):
                    if i == j or i == o or j == o:
                        continue
                    temp = 0
                    for x in range(4):
                        if mbti[i][x] != mbti[j][x]: temp += 1
                        if mbti[j][x] != mbti[o][x]: temp += 1
                        if mbti[i][x] != mbti[o][x]: temp += 1
                    minn = min(minn, temp) # 최소값 갱신
        print(minn)