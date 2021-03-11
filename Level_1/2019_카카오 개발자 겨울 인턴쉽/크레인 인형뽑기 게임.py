"""
알고리즘 문제 링크 
https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3
"""

def solution(board, moves):
    answer = 0
    stack = list()
        
    for col in moves: 
        for row in range(len(board)):
            
            brd_cell_value = board[row][col-1]
            
            if brd_cell_value != 0:
                
                if stack and stack[-1] == brd_cell_value:
                    del stack[-1]
                    answer += 2
                    
                else:
                    stack.append(brd_cell_value)
                    
                board[row][col-1] = 0
                break

    return answer
