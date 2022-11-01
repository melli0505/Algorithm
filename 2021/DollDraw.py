# 프로그래머스 크레인 인형뽑기 게임

def solution(board, moves):
    count = 0 # 터진 인형 개수
    stack = []  # 인형이 쌓일 스택
    stack_before = -1 # 직전 stack에 있는 인형 종류
    for move in moves: # 뽑을 칸 리스트
        for top in range(len(board)):
            if board[top][move-1] != 0: # 인형이 들어있으면
                stack.append(board[top][move-1]) # stack에 추가
                if stack_before == stack[-1]: # 이전 인형과 종류가 같으면 둘 다 pop
                    stack.pop()
                    stack.pop()
                    count += 2
                break
        board[top][move-1] = 0 # 뽑은 인형 자리는 비우기
        if len(stack) != 0: # stack이 비어있을 때 예외 처리
            stack_before = stack[-1]
        else: stack_before = -1
    return count


# board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
# moves = [1, 5, 3, 5, 1, 2, 1, 4]
board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 5, 1, 4, 3]
print(solution(board, moves))
