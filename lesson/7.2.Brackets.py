"""
1. Brackets
Determine whether a given string of parentheses (multiple types) is properly nested.

Easy: 100
Detected time complexity: O(N)
---
Task description
A string S consisting of N characters is considered to be properly nested if any of 
the following conditions is true:

    1. S is empty;
    2. S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
    3. S has the form "VW" where V and W are properly nested strings.
    
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly 
nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given 
S = "([)()]", the function should return 0, as explained above.

Assume that:

1. N is an integer within the range [0..200,000];
2. string S consists only of the following characters: "(", "{", "[", "]", "}" 
and/or ")".

Complexity:

1. expected worst-case time complexity is O(N);
2. expected worst-case space complexity is O(N) (not counting the storage required for input arguments).

"""
def solution(S):
    # write your code in Python 3.6
    stack = []
    
    left = ["(", "[", "{"]
    right = [")", "]", "}"]
    
    for s in S:
        if s in left:
            stack.append(s)
        else:
            if stack:
                if right.index(s) != left.index(stack.pop()):
                    return 0
            else:
                return 0
    
    if stack:
        return 0
    else: 
        return 1
                