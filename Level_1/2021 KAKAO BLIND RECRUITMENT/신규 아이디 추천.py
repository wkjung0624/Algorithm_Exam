"""
알고리즘 문제 링크
https://programmers.co.kr/learn/courses/30/lessons/72410
"""

def f_remove_not_allowed_char(new_id):
    
    fixed_id = ''
    allowed_special_chars = ['-', '_', '.']
    
    for letter in new_id:

        if letter.islower() or letter.isdigit() or \
            letter in allowed_special_chars:
            fixed_id += letter

    return fixed_id


def f_dot_replace(new_id):
    
    fixed_id = ''
    isDotRepeat = False
    
    for letter in new_id:
        if not isDotRepeat and letter == '.':
            fixed_id += '.'
            isDotRepeat = True
            
        elif letter != '.':
            isDotRepeat = False
            fixed_id += letter
        
    return fixed_id



def f_side_dot_strip(new_id):
    lstrip =  1 if new_id[ 0] == '.' else 0
    rstrip = -1 if new_id[-1] == '.' else len(new_id)
        
    return new_id[lstrip:rstrip]


def f_id_replace_null(new_id):
    return 'a' if new_id == '' else new_id


def f_id_limit_length(new_id):
    if len(new_id) > 15:
        return new_id[:14] if new_id[14] == '.' else new_id[:15]
    
    return new_id

    
def f_id_fill(new_id):    
    return new_id + new_id[-1] * (3-len(new_id)) \
        if len(new_id) <= 2 else new_id


def solution(new_id):
    
    name = new_id.lower()
    name = f_remove_not_allowed_char(name)
    name = f_dot_replace(name)
    name = f_side_dot_strip(name)
    name = f_id_replace_null(name)
    name = f_id_limit_length(name)
    name = f_id_fill(name)
    
    return name
