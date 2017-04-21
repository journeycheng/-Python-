# 实现bitmap数据结构

- 通常基于数组来实现，数组中每个元素可以看成是一些列二进制数，所有元素组成更大的二进制集合
- 对于python而言，整数类型默认为是有符号类型，所以一个整数的可用位数是31位
- bitmap用于对每一位进行操作

## bitmap实现思路
```
00000000 00000000 00000000 00000000
```
- 最高位为符号位，bitmap不能使用
- 左边为高位，右边是低位
- 最低位是第0位

### 初始化bitmap

- 确定数组的长度：max/31，向上取整：int((max+31-1)/31)

### 计算索引
- 计算在数组中的索引：num/31
- 计算在数组元素中的位索引：num%31

### 置1操作
- 在某位上置1表示在此位存储了数据：1左移，或操作

### 清0操作
- 在某位上置0表示丢弃已存储的数据：1左移，取反，与操作

### 测试某位是否为1
- 为了去除之前所存储的数据：1左移，与操作

### 上述过程编程实现
```python
class Bitmap(object):
    def __init__(self, max):
        self.size = int((max + 31 - 1) /31)
        self.array = [0 for i in range(self.size)]
        
    def calcElemIndex(self, num):
        return num / 31
    
    def calcBitIndex(self, num):
        return num % 31
    
    def set(self, num):
        elemIndex = self.calcElemIndex(num)
        bitIndex = self.calcBitIndex(num)
        elem = self.array[elemIndex]
        self.array[elemIndex] = elem | (1 << bitIndex)
        
    def clean(self, num):
        elemIndex = self.calcElemIndex(num)
        bitIndex = self.calcBitIndex(num)
        elem = self.array[elemIndex]
        self.array[elemIndex] = elem & (~(1 << bitIndex))
        
    def test(self, num):
        elemIndex = self.calcElemIndex(num)
        bitIndex = self.calcBitIndex(num)
        if self.array[elemIndex] & (1 << bitIndex):
            return True
        return False
```

## bitmap排序

```python
MAX=879
shuffle_array = [45, 2, 78, 35, 67, 90, 879, 0, 340, 123, 46]
result = []
bitmap = Bitmap(MAX)
for num in shuffle_array:
    bitmap.set(num)
    
for i in range(MAX+1):
    if bitmap.test(i):
        result.append(i)
```

```python
print result
[0, 2, 35, 45, 46, 67, 78, 90, 123, 340, 879]
```
[附源代码](bitmap.py)
