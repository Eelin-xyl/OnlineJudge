# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        h = ListNode()
        h.next = head
        h1 = h
        while True:
            h2 = h1
            for _ in range(n + 1):
                h2 = h2.next
            if not h2:
                h1.next = h1.next.next
                break
            h1 = h1.next
        return h.next