"""
알고리즘 문제 링크
https://programmers.co.kr/learn/courses/30/lessons/12903
"""


def solution(s):
    return s[len(s)//2-1:len(s)//2+1] if len(s) % 2 == 0 else s[len(s)//2]
