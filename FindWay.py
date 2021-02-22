# 알고리즘 미로찾기 - backtracking 0219 강다인

def find_way(r, c): # row, column
    
    visited[r][c] = True
    if r == ex and c == ey: return True
    if maze[r][c+1] == '0' and visited[r][c+1] == False:
        if find_way(r, c+1) == True:
            maze[r][c+1] = 'o'
            return True
    if maze[r+1][c] == '0' and visited[r+1][c] == False:
        if find_way(r+1, c) == True:
            maze[r+1][c] = 'o'
            return True
    if maze[r][c-1] == '0' and visited[r][c-1] == False:
        if find_way(r, c-1) == True:
            maze[r][c-1] = 'o'
            return True
    if maze[r-1][c] == '0' and visited[r-1][c] == False:
        if find_way(r-1, c) == True:
            maze[r-1][c] = 'o'
            return True
    return False

n = int(input()) # n x n 미로
sx, sy, ex, ey = map(int, input().split())

maze = []
visited = [[False for _ in range(n)] for _ in range(n)]
for r in range(n):
    inst = list(input().split())
    # print(inst)
    maze.append(inst)

print(maze)

maze[sx][sy] = 's'
is_success = find_way(sx, sy)
maze[ex][ey] = 'e'

if is_success:
    for row in maze:
        for column in row:
            print(column, end='')
        print()
else:
    print('Fail')
            

