"""
알고리즘 문제 링크
https://programmers.co.kr/learn/courses/30/lessons/12912
"""

def solution(s):
    
    gap = 0
    
    lower_text = s.lower()
    
    gap += lower_text.count('p')
    gap -= lower_text.count('y')
        
    return False if gap else True
