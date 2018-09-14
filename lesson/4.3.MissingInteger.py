"""
4.3. MissingInteger
Find the smallest positive integer that does not occur in a given sequence.
https://app.codility.com/c/run/demoXY37UE-S3D

Easy: 100
Detected time complexity: O(N) or O(N * log(N))

"""
def solution(A):
    # write your code in Python 3.6
    seen = {}
    upper = 0
    for a in A:
        seen[a] = True
        if a > upper:
            upper = a
    
    missing = 1
    while missing <= upper:
        if missing in seen:
            missing += 1
        else:
            break
    return missing