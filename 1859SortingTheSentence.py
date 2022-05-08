
"""
My resolution
What I learned:

-> sort key -> i can select the factor in which sorting occurs. In this case I want to sort
by the last character. So I pass a lambda that return the last digit of each element
"""

def sortSentence(s: str) -> str:
    #new_list = s.split(" ").sort(key=lambda x: x[-1])
    #new_list.sort(key=lambda x: x[-1])
    return " ".join([word[:-1] for word in s.split(" ").sort(key=lambda x: x[-1])])

print("is2 sentence4 This1 a3".split(" "))
print(sortSentence("is2 sentence4 This1 a3"))



