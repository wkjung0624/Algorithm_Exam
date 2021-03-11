"""
알고리즘 문제 링크
https://programmers.co.kr/learn/courses/30/lessons/42840
"""

def solution(answers):
    answer = []
    
    patterns = (
            (1, 2, 3, 4, 5),
            (2, 1, 2, 3, 2, 4, 2, 5),
            (3, 3, 1, 1, 2, 2, 4, 4, 5, 5)
        )
    
    max = 0
    
    for supo_idx, ptrn in enumerate(patterns):
        chunk_size = len(ptrn)
        chunked_list = [answers[offset:offset+chunk_size] 
                        for offset in range(0, len(answers), chunk_size)]
        correct = 0
        
        for frgmnt_list in *chunked_list:
            for idx, item in enumerate(frgmnt_list):
                if ptrn[idx] == item:
                    correct += 1
        
        if correct >= max:
            if answer and correct != max:
                answer.pop()
            max = correct
            answer.append(supo_idx+1)

    return answer
