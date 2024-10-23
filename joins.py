def left_join(left_file_lines,right_file_lines,unique):
    result_lines = []

    for i in left_file_lines:
        if i in right_file_lines:
            result_lines.append(f'{i}|{i}')
        else:
            result_lines.append(f'{i}|{None}')

    if unique:
        result_lines = list(dict.fromkeys(result_lines))

    return result_lines

def right_join(left_file_lines,right_file_lines,unique):
    result_lines = []
    
    for i in right_file_lines:
        if i in left_file_lines:
            result_lines.append(f'{i}|{i}')
        else:
            result_lines.append(f'{i}|{None}')

    if unique:
        result_lines = list(dict.fromkeys(result_lines))

    return result_lines

def inner_join(left_file_lines,right_file_lines,unique=False):
    result_lines = []

    for line in right_file_lines:
        if line in left_file_lines:
            result_lines.append(f'{line}|{line}')
    
    if unique:
        result_lines = list(dict.fromkeys(result_lines))

    return result_lines

def outer_join(left_file_lines,right_file_lines,unique):
    result_lines = []

    for i in left_file_lines:
        if not i in right_file_lines:
            result_lines.append(f'{i}|None')
    for i in right_file_lines:
        if not i in left_file_lines:
            result_lines.append(f'None|{i}')

    if unique:
        result_lines = list(dict.fromkeys(result_lines))

    return result_lines

def full_outer_join(left_file_lines,right_file_lines,unique):
    result_lines = []

    for i in left_file_lines:
        if i in right_file_lines:
            result_lines.append(f'{i}|{i}')
        else:
            result_lines.append(f'{i}|None')
    
    for i in right_file_lines:
        if i in left_file_lines:
            result_lines.append(f'{i}|{i}')
        else:
            result_lines.append(f'None|{i}')

    if unique:
        result_lines = list(dict.fromkeys(result_lines))

    return result_lines
