# 백준 9935
# 리스트의 replace함수로 먼저 풀었었는데, 시간 제한이 촘촘하게 있어서 replace함수를 사용할 수 없었다.
# pop과 append와 같은 O(1) 수행시간을 갖는 리스트 함수를 통해서 stack을 구현하여 수행시간을 최소화 시키기 위해서 노력했다.
# 입력된 전체 문자열의 길이가 n이라고 할 때, 이 알고리즘의 전체 수행시간은 O(n) 정도라고 생각할 수 있다.

Ex = input()
c4 = input()

str_stack = [] # 문자열 분해할 스택
count = -1 # 현재 스택의 index

for i in Ex:
    count += 1
    str_stack.append(i) # 스택에 문자열 추가
    if i == c4[-1]: # 마지막 폭발 문자열의 character가 현재 문자와 같을 때
        # print(str_stack[count - len(c4) + 1:count+1])
        if ''.join(str_stack[count - len(c4) + 1:count+1]) == c4: # 범위의 문자열이 폭발 문자열과 같으면
            del str_stack[count - len(c4) + 1:count+1] # 스택에서 삭제
            count -= len(c4) # 인덱스 감소

if len(str_stack) == 0:
    print("FRULA")
else:
    print(''.join(str_stack))

