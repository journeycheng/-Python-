# 八大排序算法的Python实现

## 1.冒泡排序

重复地走访过要排序的数列，一次比较两个元素，如果顺序错误就把它们交换过来。

例如，从小到大排序：

```python
def bubble_sort(lists):
    length = len(lists)
	  for i in range(length-1):
		    for j in range(i+1, length):
			      if lists[i] > lists[j]:
				        lists[i], lists[j] = lists[j], lists[i]
	  return lists
```

## 2.插入排序

插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中，从而得到一个新的、个数加一的有序数据，算法适用于少量数据的排序，时间复杂度为O(n^2)。是稳定的排序方法。

插入算法把要排序的数组分成两部分：第一部分包含了这个数组的所有元素，但将最后一个元素除外（让数组多一个空间才有插入的位置）。而第二部分就只包含着一个元素（即待插入元素）

```python
def insert_sort(lists):
	  length = len(lists)
	  for i in range(1, length):
		    key = lists[i]
		    j = i
		    while (j > 0 and key < lists[j-1]):
			      lists[j] = lists[j-1]
			      j -= 1
		    lists[j] = key
	  return lists
```

## 3.希尔排序
希尔排序是插入排序的一种。也称为缩小增量排序，是直接插入排序算法的一种更高效的改进版本。希尔排序是非稳定排序算法。
```python
```

## 4.选择排序
算法思想：第1趟，在排序记录1～n中选出最小的纪录，将它与1交换；第2趟，在2～n中选出最小的纪录，将它与2交换；...
```python
def select_sort(lists):
	  length = len(lists)
	  for i in range(0, length-1):
		    min_index = i
		    for j in range(i+1, length):
			      if lists[min_index] > lists[j]:
				        min_index = j
		    lists[i], lists[min_index] = lists[min_index], lists[i]
	  return lists
```

## 5.快速排序

通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据要小，然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行。
```python
def quick_sort(lists, left_index, right_index):
    if left_index >= right_index:
		    return lists
	  key = lists[left_index]
	  low = left_index
	  high = right_index
	  while left_index < right_index:
		    while left_index < right_index and lists[right_index] >= key:
			      right_index -= 1
		    lists[left_index], lists[right_index] = lists[right_index],lists[left_index]

		    while left_index < right_index and lists[left_index] <= key:
			      left_index += 1
		    lists[left_index], lists[right_index] = lists[right_index],lists[left_index]

	  quick_sort(lists, low, left_index - 1)
	  quick_sort(lists, left_index + 1, high)
	  return lists
```
