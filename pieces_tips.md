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
