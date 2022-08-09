# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        Node = head
        # Link List를 List로 바꿔 풀기
        myList = list()
        while Node:
            myList.append(Node.val)
            Node = Node.next
        print(myList)
        # Two-pointer로 palindrome 푸는 방법
        left, right = 0, len(myList)-1
        Answer = True
        while left < right:
            if myList[left] != myList[right]:
                Answer = False
                break
            else:
                left += 1
                right -= 1
        return Answer