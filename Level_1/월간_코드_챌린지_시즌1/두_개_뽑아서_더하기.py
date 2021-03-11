"""
알고리즘 문제 링크
https://programmers.co.kr/learn/courses/30/lessons/68644
"""

def solution(numbers):
    
    answer = []
    
    for main_idx in range(len(numbers)-1):
        for sub_idx in range(main_idx+1, len(numbers)):
            result = numbers[main_idx] + numbers[sub_idx]
            answer.append(result)
                        
    return sorted(set(answer))
