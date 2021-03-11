"""
알고리즘 문제 링크
https://programmers.co.kr/learn/courses/30/lessons/17682
"""

import re

def solution(dartResult):

    scores = re.finditer('[0-9]*[SDT][*#]?', dartResult)
    leverage_token = {'S': 1, 'D': 2, 'T': 3}
    special_token = {'*': 2, '#': -1}
    
    results = list()
    
    for idx, item in enumerate(scores):
        
        score_raw_text = item.group()
        score = int(re.match('[0-9]*', score_raw_text).group())
        bonus = leverage_token[re.search('[SDT]', score_raw_text).group()]
        option = 1
        
        cur_token = score_raw_text[-1]
        
        try:
            option = special_token[cur_token]
            if cur_token in "*":
                results[-1] *= 2
        except:
            pass
        
        results.append(pow(score,bonus) * option)

    return sum(results)
