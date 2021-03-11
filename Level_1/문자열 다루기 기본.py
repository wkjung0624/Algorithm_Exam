"""
알고리즘 문제 링크
https://programmers.co.kr/learn/courses/30/lessons/12918
"""

def solution(s):
    
    try:
        if len(s) not in [4,6] or not s.isdigit():
            raise ValueError
        
        return True
    
    except ValueError:
        return False
