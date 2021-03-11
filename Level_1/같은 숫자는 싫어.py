"""
알고리즘 문제 링크
https://programmers.co.kr/learn/courses/30/lessons/12906
"""

def solution(arr):
    answer = []
    head = arr[0]
    
    for val in arr[1:]:
	    if head != val:
    		answer.append(head)
    		head = val
    
    answer.append(head)
    
    return answer
