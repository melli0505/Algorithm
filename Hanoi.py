# 백준 11729 강다인

# 하노이 탑 문제를 분해해보면 n-1개 원판을 두 번째(via)로 옮기는 것이 먼저이고, 그 다음 n번째 원반을 세 번째(to)로 옮긴 뒤 via에 있던 원판을 to로 옮기는 과정을 거친다.
# 따라서 n개의 원판을 옮기는 문제는 재귀적으로 n-1에 해당하는 하노이탑 함수를 호출함으로써 해결할 수 있다.
def Hanoi(n, start, via, to):
    if n == 1:
        print(start, to) # n = 1이면 경유지가 목적지
    else:
        Hanoi(n-1, start, to, via) # start에서 to를 거쳐서 via로 이동 
        print(start, to)
        Hanoi(n-1, via, start, to) # via에서 start를 거쳐서 to로 이동
 # via에서 start를 거쳐서 to로 이동


pan = int(input()) # 원 판의 갯수

move_list = []

print(pow(2, pan) - 1)
Hanoi(pan, 1, 2, 3)
