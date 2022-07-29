#LEET CODE LINK: https://leetcode.com/problems/linked-list-cycle/
#TIME COMPLEXITY (O(n))
#SPACE COMPLEXITY (O(n))
#LEARNINGS

"""
My strategy began by recording every node visited and if it was
added twice to the dict, return true, else, False. However, Space
complexy is o(n) -> potentially every node is going to be added to the dict 
-> No bueno.

The optimized way: Floyds Toirtoise & Hare algorithm. If the fast
pointer and slow point meet, means that there's a loop somewhere.
"""

#CODE


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        curr = head
        pos_dict = {}
        pos = 0
        
        while curr:
            
            if curr in pos_dict:
                return True
            
            pos_dict[curr] = pos
            curr = curr.next
            pos += 1
        return False

#Floyds Toirtoise & Hare algorithm
class Solution1:
    def hasCycle(self, head: ListNode) -> bool:
        
        f, s = head, head

        while f and f.next:
            if f == s:
                return True

            s = s.next
            f = f.next.next
        return False

       
