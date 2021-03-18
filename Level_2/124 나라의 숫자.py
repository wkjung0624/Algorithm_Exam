  
"""
알고리즘 문제 링크
https://programmers.co.kr/learn/courses/30/lessons/12899
"""


def solution(n):
    
    _124_jinbeob = list()
    
    mok, nam = n, 0
    
    while mok != 0:
        n = mok - 1
        mok, nam = divmod(n,3)
        _124_jinbeob.append(nam)
        
    return "".join(map(lambda x : str(2**x), _124_jinbeob[::-1]))
