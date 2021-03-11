"""
알고리즘 문제 링크
https://programmers.co.kr/learn/courses/30/lessons/68935
"""


def solution(n):
    rev_3jin = list()
    
    while n != 0:
        n, nam = divmod(n, 3);
        rev_3jin.append(nam)
        
    return sum( [ 3**idx * ch for idx, ch in enumerate(rev_3jin[::-1]) ] )
