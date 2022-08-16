# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        MyHeap = []         # 우선순위큐 (Min Heap)
        for List in lists:
            while List:
                heapq.heappush(MyHeap, List.val)
                List = List.next
        AnswerNode = ListNode(0, None)
        Pointer = AnswerNode
        while len(MyHeap) != 0:
            Pointer.next = ListNode(heapq.heappop(MyHeap), None) # Min Heap의 pop은 최소값을 먼저
            Pointer = Pointer.next
        return AnswerNode.next