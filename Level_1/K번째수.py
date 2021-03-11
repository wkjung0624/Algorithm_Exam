"""
알고리즘 문제 링크
https://programmers.co.kr/learn/courses/30/lessons/42748
"""

def solution(array, commands):
    
    answer = []
    
    for cmd in commands:
        ret = array[cmd[0]-1:cmd[1]]
        ret.sort()
        answer.append(ret[cmd[2]-1])
        
    return answer
