def maxDepth(s: str) -> int:
    
    max = 0
    holder = 0
    
    for c in s:
        if c == "(":
            print(c, "upper------------")
            holder += 1
            print(holder)
            if holder > max:
                max = holder
        elif c == ")":
            print(c, "lower")
            holder -= 1
        else: max = max
    return max
        




s1 = "(1+(2*3)+((8)/4))+1"
s2 = "(1)+((2))+(((3)))"

print(maxDepth(s1), "testee")
