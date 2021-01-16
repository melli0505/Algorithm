# 프로그래머스 가장 큰 수

def solution(numbers):
    sum_num = sum(numbers)
    # 문자열은 앞 문자가 큰 순서대로 & 길이가 긴 순서대로 sorting이 가능하다.
    numbers = sorted(list(map(str, numbers)), key = lambda x:x*4, reverse = True)
    # key 값에 각 요소의 문자열을 4번 반복해준 값을 기준으로 정렬하도록 했다. numbers의 최고값이 1000이기 때문에,가장 작은 수를 입력해도 4자릿수 이상이 되도록 했다.
    # reverse를 통해서 앞 자리가 큰 수부터 뒤로 점진적으로 확인해서 정렬하도록 했다.
    answer = ''
    
    if sum_num == 0:
        answer = '0'
    else:
        answer = ''.join(numbers)
    
    return answer

number = list(map(int, input().split()))
print(solution(number))