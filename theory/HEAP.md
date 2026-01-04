HEAP
Created at : 2026-01-04 19:50

### HEAP 이란
힙은 특정한 규칙을 가진 트리 기반의 자료구조이다.
- 우선순위 QUEUE를 구현하는데도 heap을 사용한다.

### HEAP 구조
![[Pasted image 20260104195143.png]]
- python에서 heapq의 default는 min heap이다.
- 최댓값과 최솟값을 찾는 연산을 빠르게 하기 위해 완전 이진트리형태이다.

### heap module function
- heapq.heappush(heap, item)  
    이 함수는 아이템을 힙에 추가한다.
    
- heapq.heappop(heap)  
    힙에서 가장 작은 아이템을 뺴고 그 값을 반한다. 이 함수 자체가 값을 반환하기 때문에  
    print를 쓰면 값을 출력할 수 있다.
    
- heapq.heappushpop(heap, item)  
    아이템을 힙에 추가한 다음, 가장 작은 아이템을 빼고 그 값을 반환한다.
    
- heapq.heapify(x)  
    리스트 x를 즉각적으로 heap으로 변환한다. (O(N))

### HEAP 구현
```python

class MAXHEAP:
    def __init__(self):
        """Max Heap 초기화"""
        self.heap = []
    
    def _parent(self, idx):
        """부모 노드의 인덱스 반환"""
        return (idx - 1) // 2
    
    def _left_child(self, idx):
        """왼쪽 자식 노드의 인덱스 반환"""
        return 2 * idx + 1
    
    def _right_child(self, idx):
        """오른쪽 자식 노드의 인덱스 반환"""
        return 2 * idx + 2
    
    def _heapify_up(self, idx):
        """하향식으로 heap 속성 유지 (부모와 비교하여 위로 올라감)"""
        while idx > 0:
            parent_idx = self._parent(idx)
            if self.heap[idx] <= self.heap[parent_idx]:
                break
            # 부모보다 크면 교환
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            idx = parent_idx
    
    def _heapify_down(self, idx):
        """상향식으로 heap 속성 유지 (자식과 비교하여 아래로 내려감)"""
        while True:
            left_idx = self._left_child(idx)
            right_idx = self._right_child(idx)
            largest = idx
            
            # 왼쪽 자식이 존재하고 더 크면
            if left_idx < len(self.heap) and self.heap[left_idx] > self.heap[largest]:
                largest = left_idx
            
            # 오른쪽 자식이 존재하고 더 크면
            if right_idx < len(self.heap) and self.heap[right_idx] > self.heap[largest]:
                largest = right_idx
            
            # 현재 노드가 가장 크면 종료
            if largest == idx:
                break
            
            # 자식과 교환
            self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
            idx = largest
    
    def push(self, value):
        """값을 heap에 추가"""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
    
    def pop(self):
        """최대값을 제거하고 반환"""
        if self.is_empty():
            raise IndexError("Heap is empty")
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # 루트와 마지막 노드 교환
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_value
    
    def peek(self):
        """최대값을 반환 (제거하지 않음)"""
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self.heap[0]
    
    def size(self):
        """heap의 크기 반환"""
        return len(self.heap)
    
    def is_empty(self):
        """heap이 비어있는지 확인"""
        return len(self.heap) == 0
    
    def __str__(self):
        """heap 내용을 문자열로 반환"""
        return str(self.heap)

```