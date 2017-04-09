## 深度搜索和广度搜索走迷宫

[图解深搜和广搜](https://wenku.baidu.com/view/97c9220452ea551810a687e4.html?from=search)

### DFS
```python
def dfs(map, start_x, start_y, end_x, end_y):
    if not map or map[start_x][start_y]:
        return

    stack =list()
    map[start_x][start_y] = 1
    stack.append([start_x, start_y])

    while stack:
        s = stack[-1]
        if s[0] == end_x and s[1] == end_y:
            return stack
        if map[s[0]+1][s[1]] == 0:
            stack.append([s[0]+1, s[1]])
            map[s[0]+1][s[1]] = 1
        elif map[s[0]][s[1]+1] == 0:
            stack.append([s[0], s[1]+1])
            map[s[0]][s[1]+1] = 1
        elif map[s[0]][s[1]-1] == 0:
            stack.append([s[0], s[1]-1])
            map[s[0]][s[1]-1] = 1
        elif map[s[0]-1][s[1]] == 0:
            stack.append([s[0]-1, s[1]])
        else:
            stack.pop()
    return stack
```
- 返回从起点到终点的路径

### BFS

```python
from collections import deque
def bfs(map, start_x, start_y, end_x, end_y):
    if not map or map[start_x][start_y]:  # 起始点不能走
        return
    queue = deque()
    map[start_x][start_y] = 1
    queue.append([start_x, start_y, 0]) # 坐标x,坐标y,当前已走步数

    dir = [[1, 0, -1, 0], [0, 1, 0, -1]]
    
    while queue:
        s = queue.popleft()
        if s[0] == end_x and s[1] == end_y:
            return s[2]

        for i in range(0, 4):
            tmp = [0, 0, s[2]]
            tmp[0] = s[0] + dir[0][i]
            tmp[1] = s[1] + dir[1][i]

            if map[tmp[0]][tmp[1]] == 0:  # 下一步可以走
                tmp[2] += 1
                map[tmp[0]][tmp[1]] = 1   # 标记为1,防止后面再走这一步
                queue.append(tmp)
```
- 返回从起点到终点所走的步数

### 使用例子
```python
start_x = 1
start_y = 1

end_x = 8
end_y = 8
map = [[1,1,1,1,1,1,1,1,1,1], [1,0,0,1,0,0,0,1,0,1], [1,0,0,1,0,0,0,1,0,1],
       [1,0,0,0,0,1,0,0,0,1], [1,0,1,1,1,0,0,0,0,1], [1,0,0,0,1,0,0,0,0,1],
       [1,0,1,0,0,0,1,0,0,1], [1,0,1,1,1,0,1,1,0,1], [1,1,1,0,0,0,0,0,0,1],
       [1,1,1,1,1,1,1,1,1]]
```
