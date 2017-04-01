- 1.变量与内存
  - locals()、globals()两个函数，查看所有变量
  - 查看内存地址: id(variable)
  - 查看变量占用的空间大小: sys.getsizeof(variable)
  - 要检测所有的变量的话，可以用python的smiley模块监测所有的内存变量情况
  
- 2.字典的灵活运用
```python
>>> s = {'abc':1, 'bcd':2}
>>> isinstance(s.keys(), list)
True

>>> s = {'abc', 'bcd'}
>>> isinstance(s, set)
True

>>> {}.fromkeys('xyz')
{'y': None, 'x': None, 'z': None}

>>> {}.fromkeys('xyz',1)
{'y': 1, 'x': 1, 'z': 1}
```
如果只给字典key，没有value，相当于是一个set

- 3.Pickle存储对象
  - 通常用来存储一些计算好的变量，方便以后直接使用：对象 -> 文本 -> 文件
  - dumps()和load()
  
```python
# 对象保存进文件
pickle_file = os.path.join('.', 'notMNIST.pickle')

try:
    f = open(pickle_file, 'wb')
    save = {
        'train_dataset': train_dataset,
        'train_labels': train_labels,
        'valid_dataset': valid_dataset,
        'valid_labels': valid_labels,
        'test_dataset': test_dataset,
        'test_labels': test_labels,
        }
    pickle.dump(save, f, pickle.HIGHEST_PROTOCOL)
    f.close()
except Exception as e:
    print('Unable to save data to', pickle_file, ':', e)

# 从文件中读取对象
pickle_file = 'notMNIST.pickle'
with open(pickle_file, 'rb') as f:
    save = pickle.load(f)
    train_dataset = save['train_dataset']
    train_labels = save['train_labels']
    valid_dataset = save['valid_dataset']
    valid_labels = save['valid_labels']
    test_dataset = save['test_dataset']
    test_labels = save['test_labels']
    del save
```

- 4.集合更新方法汇总：add(), update(), remove(), -=
```
>>> s = set(['a', 'b', 'c', 'd'])
>>> s
set(['a', 'c', 'b', 'd'])
>>> s.add('z') # 增加元素
>>> s
set(['a', 'c', 'b', 'd', 'z'])
>>> s.update('python')  # 增加元素
>>> s
set(['a', 'c', 'b', 'd', 'h', 'o', 'n', 'p', 't', 'y', 'z'])
>>> s.remove('z') # 删除某个元素
>>> s
set(['a', 'c', 'b', 'd', 'h', 'o', 'n', 'p', 't', 'y'])
>>> s -= set('python')  # 计算两个集合的差集
>>> s
set(['a', 'c', 'b', 'd'])
```

- 5.序列相关的内建函数
sorted(), reversed(), enumerate(), zip()

- 6.列表操作方法汇总
```
list.append(obj)  # 像列表中添加一个对象obj
list.count(obj)    # 返回一个对象在列表中出现的次数
list.extend(seq)   # 把序列seq的内容添加到列表中
list.index(obj, i=0, j=len(list))   # 返回list[k]=obj的k值，并且k的范围在[i,j]；否则引发ValueError异常
list.find(obj) # 从list中找到obj，返回索引值，未找到返回－1，不会报错
list.insert(index, obj)   # 在索引量为index的位置插入对象obj
list.pop(index=-1)     # 删除并返回指定位置（默认尾部）的对象
list.remove(obj)   # 从列表中删除对象obj
list.reverse()    # 原地翻转泪飙
list.sort(func=None, key=None, reverse=False) # 原地排序列表
```
