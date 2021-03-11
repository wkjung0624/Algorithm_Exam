"""
알고리즘 문제 링크
https://programmers.co.kr/learn/courses/30/lessons/12917
"""

def solution(s):
    sort_str = sorted(s,reverse=True)

    u_str = "".join(map(lambda x : x if x > 'Z' else '', sort_str))
    l_str = "".join(map(lambda x : x if x < 'a' else '', sort_str))
    
    return u_str + l_str
