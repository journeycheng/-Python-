# 八大排序算法的Python实现

## 内排序和外排序

根据在排序过程中待排序的纪录是否全部被放置在内存中，排序可以分为：内排序和外排序。
> - 内排序是在排序整个过程中，待排序的所有记录全部被放置在内存中。
> - 外排序是由于排序的纪录个数太多，不能同时放置在内存中，整个排序过程需要在内外存之间交换多次数据才能进行。


对于内排序来说，排序算法的性能主要受到3个方面的影响：
> - 时间性能

在内排序中，主要进行两种操作：比较和移动。高效率的内排序算法应该是具有尽可能少的关键字比较次数和尽可能少的纪录移动次数。
> - 辅助空间

辅助空间是除了存放待排序所占用的存储空间之外，执行算法所需要的其他存储空间。
> - 算法的复杂性



内排序：插入排序、选择排序


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
时间复杂度O(n^2)

## 2.选择排序
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
> - 最大的特点就是交换移动次数相当少
> - 无论最好最差的情况，比较次数都是一样的，都需要比较(n-1)+(n-2)+...+2+1=n(n-1)/2次
> - 交换次数，最好的时候是0次，最差的情况是n－1次，因此总的时间复杂度是O(n^2)


## 3.插入排序

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
> - 需要有一个保存待插入数值的辅助空间
> - 最好的情况是本身有序，比较n－1次，不需要移动，时间复杂度是O(n)
> - 最差的情况是逆序的，比较(n+2)(n-1)/2，移动次数达到最大值(n+4)(n-1)/2
> - 平均比较和移动次数为n^2/4。时间复杂度为O(n^2)
> - 比冒泡和选择性能好

## 4.快速排序

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
> - 平均情况下，时间复杂度是O(nlogn)，空间复杂度是O(logn)
> - 枢轴的值太大或者太小都会影响快排的性能，三数取中法、九数取中法等
