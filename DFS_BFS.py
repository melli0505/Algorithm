# BOJ 1260 DFS와 BFS (강다인)

from collections import deque


def dfs(graph, start):
    stack = [start] # stack에 값을 쌓음
    visited = [] # 방문한 노드

    while stack:
        v = stack.pop() 
        if v not in visited: # 노드를 방문하지 않았다면
            visited.append(v)
            stack.extend(sorted(graph[v], reverse=True)) # last in-first out이므로 역정렬을 해줘야 작은 수부터
            print(v, end=' ')


def bfs(graph, start):
    visited = []
    queue = deque([start]) # queue 모듈 사용
    # print(queue)

    while queue:
        v = queue.popleft() # fifo
        if v not in visited:
            queue.extend(sorted(graph[v])) # first in-first out이므로 정렬해줘야 작은 수부터 
            visited.append(v)
            print(v, end=' ')


# N = 정점 개수, M = 선의 개수, V = 시작할 정점
N, M, V = map(int, input().split())
m_list = [[] for i in range(N + 1)]  # 연결 선을 저장할 2차원 리스트

for line in range(M):
    s, e = map(int, input().split())
    m_list[s].append(e) # 시작 인덱스에 끝 값 넣기
    m_list[e].append(s) # 끝 인덱스에 시작 값 넣기

dfs(m_list, V)
print()
bfs(m_list, V)
