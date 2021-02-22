# BOJ 1343 강다인

# 치환 함수
def substition(string, s, time, char):
    string = string[:s] + char * time + string[s + len(char) * time :]
    return string

board = input()

s = 0 # 시작 인덱스
e = 0 # 끝 인덱스
doing = False  # 마지막 문자 탐색 여부

for i in range(len(board)):  # board 탐색
    if len(board) == 1:
        board = '-1'
        break
    # 탐색 시작
    if board[i] == 'X' and doing == False:
        if i == len(board) - 1:
            board = '-1'
            break
        s = i
        doing = True
        
    elif (doing == True and board[i] == 'X'):  # 현재 값이 X이고 탐색 중일 때
        # 다음 인덱스가 out of range가 아니고 X가 아니거나 현재 인덱스가 마지막 인덱스일 때
        if (i+1 != len(board) and board[i+1] != 'X') or i+1 == len(board):
            e = i
            doing = False # 탐색 끝
            sub_len = len(board[s:e+1]) # 치환할 문자열 길이
            if sub_len >= 4 and sub_len % 2 == 0: # 4보다 크고 짝수이면
                if sub_len % 4 == 0:
                    board = substition(board, s, sub_len//4, 'AAAA') # 전체 부분 AAAA로 치환
                else:
                    board = substition(board, s, (sub_len-2)//4, 'AAAA') # 마지막 2개를 뺀 나머지를 AAAA로 치환
                    board = substition(board, e-1, 1, 'BB') # 마지막 2개를 BB로 치환
            elif sub_len == 2: # 2이면
                board = substition(board, s, 1, 'BB')
            else: # 2로 안 나누어지면 치환 불가
                board = '-1'
                break
print(board)