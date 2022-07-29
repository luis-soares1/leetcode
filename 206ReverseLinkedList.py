#LEET CODE LINK: https://leetcode.com/problems/reverse-linked-list/

#TIME COMPLEXITY O(n)
#SPACE COMPLEXITY O(1)

#LEARNINGS


#CODE

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

