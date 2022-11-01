# 백준 1543

string = input() # 전체 문자열
search = input() # 검색할 문자열

count, i = 0, 0 # 단어 갯수, 전체 문자열 길이

while i < len(string): # i(index)가 전체 문자열 길이보다 작은 동안
    # i에 검색할 문자열의 길이를 더한 게 index range를 벗어나지 않고 
    # 전체 문자열을 i(현제 인덱스)부터 i에 검색할 문자열의 길이를 더하여 슬라이싱한 내용이 검색할 문자열과 같으면
    if i + len(search) - 1 < len(string) and string[i:i+len(search)] == search:
        count += 1
        i += len(search) # 검색된 단어 스킵
    else:
        i += 1

print(count)
        