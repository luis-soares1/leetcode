"""
"""

from tkinter import S


def countConsistentStrings(allowed: str, words: list[str]) -> int:
   count = 0
   for word in words:
       if len(word) == len(set(word + allowed)): count += 1
    
    return word



countConsistentStrings("abc", ["a","b","c","ab","ac","bc","abc"])
