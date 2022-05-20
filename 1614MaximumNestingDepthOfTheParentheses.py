"""
my solution
basically if "(", adds one point, ")" removes a point.
As when -1 happens, it will never be a point in which holder will be max, 
so no need for max = holder in that condition.

What I learned from the best solution:

Using max instead of if, like this:

   def maxDepth(self, s):
        res = cur = 0
        for c in s:
            if c == '(':
                cur += 1
                res = max(res, cur)
            if c == ')':
                cur -= 1
        return res
"""

def maxDepth(s: str) -> int:
    max_num = 0
    holder = 0

    for c in s:
        if c == "(":
            holder += 1
            max_num = max(holder, max)
        elif c == ")":
            holder -= 1
    return max
        






