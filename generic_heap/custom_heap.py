from typing import Any, Callable, Generic, Iterable, List, Optional, TypeVar
import heapq

T = TypeVar("T")


class Heap(Generic[T]):
	"""A heap (aka priority queue) data structure.

	Args:
		Generic (T): The type of the elements in the heap.
	"""

	def __init__(
		self, items: Iterable[T] = None, key: Callable[[T], Any] = lambda _: _
	):
		"""Construct a heap data structure.

		Args:
			items (Iterable[T], optional): The items to initialize the heap with. If omitted will create an empty heap.
			key (Callable[[T], Any], optional): A function to be used to determine the priority of the elements in the heap. It should take an element of type T and return some comparable object (e.g. an integer) which represents the priority. Lower priorities are extracted first. If no priority function is provided, then the inserted objects themselves are used and a min-heap is created.
		"""
		self.__heap_key = key
		self.__heap_list = [
			(self.__heap_key(item), i, item) for i, item in enumerate(items or [])
		]
		self.__heap_index = len(self.__heap_list)
		heapq.heapify(self.__heap_list)

	def push(self, item: T):
		"""Insert a new item into the heap.

		Args:
			item (T): The item to insert.
		"""
		heapq.heappush(
			self.__heap_list, (self.__heap_key(item), self.__heap_index, item)
		)
		self.__heap_index += 1

	def pop(self) -> T:
		"""Extrace an item from the heap.

		Returns:
			T: The item extracted from the heap.

		Raises:
			IndexError: If there are no more items in the heap.
		"""
		return heapq.heappop(self.__heap_list)[-1]

	def size(self) -> int:
		"""Get the number of items in the heap.

		Returns:
			int: The number of items in the heap.
		"""
		return len(self.__heap_list)

	def show(self):
		"""Print the items in the heap."""
		for item in self.__heap_list:
			print(item[-1], end=" ")
		print()


if __name__ == "__main__":
	print("Nothing to Show")
