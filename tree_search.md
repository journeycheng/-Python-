## 二叉树遍历

### 1、树的定义和测试用例
```python
#! coding=utf-8
class TreeNode(object):
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
```

### 2、先序遍历
- 先序递归遍历
```python
def preOrder_recursive(root):
    if not root:
        return
    print root.val
    preOrder_recursive(root.left)
    preOrder_recursive(root.right)
```

- 先序非递归遍历
```python
def preOrder_nonrecursive(root):
    stack = list()
    while root or stack:
        while root:
            print root.val
            stack.append(root)
            root = root.left
        if stack:
            root = stack.pop()
            root = root.right
```
- DFS遍历

```python
def dfs(root):
    stack = list()
    if root: 
        stack.append(root)
    while stack:
        current = stack.pop()
        print current.val
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
```

### 3、中序遍历

- 中序递归遍历
```python
def midOrder_recursive(root):
    if not root:
        return
    midOrder_recursive(root.left)
    print root.val
    midOrder_recursive(root.right)
```

- 中序非递归遍历

```python
def midOrder_nonrecursive(root):
    stack = list()
    while root or stack:
        while root:
            stack.append(root)
            root = root.left

        if stack:
            root = stack.pop()
            print root.val
            root = root.right
```

### 4、后序遍历

- 后序递归遍历

```python
def postOrder_recursive(root):
    if not root:
        return
    postOrder_recursive(root.left)
    postOrder_recursive(root.right)
    print root.val
```

- 后序非递归遍历
```python
def postOrder_nonrecursive(root):
    stack = list()
    stack_flag = list()
    while root or stack:
        while root:
            stack.append(root)
            stack_flag.append(0)
            root = root.left

        while stack and stack_flag[-1] == 1:
            stack_flag.pop()
            current = stack.pop()
            print current.val
        if stack:
            stack_flag.pop()
            stack_flag.append(1)
            root = stack[-1]
            root = root.right
```

### 5、层次遍历或者BFS遍历

```python
from collections import deque
def levelOrder(root):
    if not root:
        return
    queue = deque()
    queue.append(root)

    while queue:
        current = queue.popleft()
        print current.val
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
```





