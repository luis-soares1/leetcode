
"""
my solution
I knew it wasn't really good with all the elifs.
I will try with a dict now.(saw someone doing it, didn't see all the code
but thought of giving it a try.)

what i learned:

whenever something can have several values, use a dict.
"""

# def countMatches(items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
    
#     if ruleKey == "type":
#         global i
#         i = 0
#     elif ruleKey == "color":
#         i = 1
#     elif ruleKey == "name":
#         i = 2
#     else: 
#         ruleKey == ""
    
#     count = 0
#     for sub_list in items:
#         if sub_list[i] == ruleValue:
#             count += 1
    
#     return count

# print(countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "silver"))

def countMatches1(items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
    rules = {"0":"type", "1":"color", "2":"name"}
    
    count = 0
    
    for key, value in rules.items():
        if value == ruleKey:
            for lst in items:
                if lst[int(key)] == ruleValue:
                    count += 1
    return count

print(countMatches1([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "silver"))

            




