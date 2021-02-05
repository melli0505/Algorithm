# BOJ 10989 강다인
import sys 

N = int(sys.stdin.readline())    
num = [0] * 10001 # 메모리가 매우 작게 설정되어 있기 때문에 배열의 인덱스를 숫자로 사용했다.

for i in range(N):
    num[int(sys.stdin.readline())] += 1

for j in range(10001):
    if num[j] != 0:
        sys.stdout.write('%s\n' %j * num[j]) # 중복되는 만큼 반복 출력