from dataclasses import dataclass
from typing import Any

@dataclass
class Element:
    value: Any
    priority: int


class BinaryHeap:

    def __init__(self):
        self.heap = []

    def heap_check_up(self, idx:int)->None:
        if idx == 0:
            return None
        parent = (idx-1) // 2
        if self.heap[idx].priority < self.heap[parent].priority:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            self.heap_check_up(parent)

    def heap_check_down(self, idx:int)->None:
        left = 2 * idx + 1
        right = 2 * idx + 2
        smallest = idx

        if left < len(self.heap) and self.heap[left].priority < self.heap[smallest].priority:
            smallest = left

        if right < len(self.heap) and self.heap[right].priority < self.heap[smallest].priority:
            smallest = right

        if smallest != idx:
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            self.heap_check_down(smallest)

    def push(self, element:Element):
        self.heap.append(element)
        self.heap_check_up(len(self.heap)-1)

    def pop(self)->Element:
        # najdi nejmensi prvek a vrat ho
        if not self.heap:
            raise Exception("Heap is empty")

        if len(self.heap) == 1:
            return self.heap.pop()

        smallest_element = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heap_check_down(0)
        return smallest_element

    def head(self)->Element:
        if not self.heap:
            raise Exception("Heap is empty")
        return self.heap[0]
