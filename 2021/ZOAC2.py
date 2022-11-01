# 백준 18238 강다인

zoac = input()  
pointer = 0 # 현재 포인터 위치
counter = 0 # 총 걸린 시간 저장
for i in zoac:
    index = ord(i) - 65 # 탐색할 값의 인덱스(ASCII 기준, ord 함수 = character to ASCII)
    # 정방향 탐색, 가중치 forward
    if index < pointer: forward = 26 - (pointer - index)
    else: forward = index - pointer

    #역방향 탐색, 가중치 reverse
    if index > pointer: reverse = 26 - (index - pointer)
    else: reverse = pointer - index

    counter += forward if forward <= reverse else reverse # 두 값 중 더 작은 값을 count에 add
    pointer = index

print(counter)