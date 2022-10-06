#Practice: Reverse in place (THere are more than method)

"""
def our_reverse(lists):
    for idx in range(len(lists)):
        print(lists[len(lists) - idx -1])

lists = input().split()
our_reverse(lists)

"""

"""
list = input().split()
list.reverse()
print(list)
"""
#Practice: Find pair values of maximum sum
"""
"""

def pair_maxsum_bug_slow(lst):
    pos1, pos2 = 0, 1

    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[pos1] + lst[pos2] < lst[i] + lst[j]:
                pos1, pos2 = i, j

        return pos1, pos2


def main():
    lst = list(map(int, input('Enter your list: '). split())) 
    assert len(lst) > 1

    pos1, pos2 = pair_maxsum_bug_slow(lst)

    


#Nested loop with bug
#Nested loop
#Practice: Find the index of the top 2 maximum values
#Find the index of maximum value in a list
#Practice: Find the index of the top 2 maximum values
#Top max 2: Slow
#Faster solution
#Practice: Find most frequent number
#Practice: Find most frequent number: Faster
##############################
#Homework 1: Is increasing array?
#Homework 2: Replace MinMax
#Homework 3: Search for a number
#Homework 4: Unique Numbers of unordered 
#Homework 5: Unique Numbers of ordered
#Homework 6: Smallest pair
#Homework 7: Find the 3 minimum values
#Homework 1: Find most frequent number
#Homework 2: Digits frequency
#Recall Definitions for sequences
#Homework 3: Is subsequence
#Homework 3: Is subsequence
#Homework 5: Remove evens inplace
#Homework 1: Minimum of a type!
#Homework 3: Is sublist
#Homework 3: Fixed sliding window
#Homework 4: Count increasing sublists
#Homework 5: Josephus problem
#Homework 6: longest sublist
