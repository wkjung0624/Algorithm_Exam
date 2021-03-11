"""
알고리즘 문제 링크
https://programmers.co.kr/learn/courses/30/lessons/42862
"""

def solution(n, lost, reserve):

    reserve = set(reserve)

    for size in [0, 1, -2]:
        lost = set(map(lambda x : x+size, lost))
        reserve, lost = reserve - lost, lost - reserve
    
    return n - len(lost)
