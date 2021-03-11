"""
알고리즘 문제 링크
https://programmers.co.kr/learn/courses/30/lessons/42576
"""

def solution(participant, completion):
    
    participant.sort()
    completion.sort()
    answer = participant[-1]
    
    for part_idx in range(len(participant)-1):
        if participant[part_idx] != completion[part_idx]:
            answer = participant[part_idx]
            break
    
    return answer
