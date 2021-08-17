# Heap

Heap data structure similar to priority queues in Java and C++.

---

## Installation

```
pip install generic_heap
```

## Usage

First you must import the `Heap` class.

```py
from generic_heap import Heap
```

### Constructor

To create a heap call the constructor. It takes two optional arguments.

- `items`: An iterable object containing the items to initialize the heap with. If omitted, the heap will be empty.
- `key`: A function which determines the priority of the items. It should accept one item of the type that is stored in the heap and return any object that is comparable. Lower keys are popped first.

```py
empty_min_heap = Heap()

populated_max_heap = Heap([6,2,7,2,3,1,6,3,9,3], key=lambda x: -x)

custom_heap = Heap(items=[[0,30],[15,20],[5,10]], key=lambda x: -(x[0]*x[0]+x[1]*x[1]))
```

### Push

You can add `my_item` to `my_heap` like this.

```py
my_heap.push(`my_item`)
```

### Pop

You can extract the minimum value (determined by the `key` function) like this.

```py
min_val = my_heap.pop()
```

### Other Methods

```py
heap.show() # print all the elements of the heap

heap.size() # get the number of items in the heap
```

## License

© 2021 Pritam Sarkar

This repository is licensed under the MIT license. See LICENSE for details.
