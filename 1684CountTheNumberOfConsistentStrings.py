"""
"""

from tkinter import S


def countConsistentStrings(allowed: str, words: list[str]) -> int:
   print(sum([1 for element in [[char in word for char in allowed] for word in words] if len(element) == sum(element)]))



countConsistentStrings("abc", ["a","b","c","ab","ac","bc","abc"])
