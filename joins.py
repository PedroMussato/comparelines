def left_join(left_file_lines,right_file_lines,unique=False,case_sensitive=True):
    result_lines = []

    for i in left_file_lines:
        if case_sensitive:
            if i in right_file_lines:
                result_lines.append(f'{i}|{i}')
            else:
                result_lines.append(f'{i}|{None}')
        else:
            lower_i = i.lower()
            found = False
            
            for j in right_file_lines:
                if lower_i == j.lower():
                    result_lines.append(f'{i}|{j}')
                    found = True
                    break
            
            if not found:
                result_lines.append(f'{i}|{None}')

    if unique:
        result_lines = list(dict.fromkeys(result_lines))

    return result_lines

def right_join(left_file_lines,right_file_lines,unique=False,case_sensitive=True):
    result_lines = []
    
    if case_sensitive:
        for i in right_file_lines:
            if i in left_file_lines:
                result_lines.append(f'{i}|{i}')
            else:
                result_lines.append(f'{i}|{None}')
    else:
        for i in right_file_lines:
            found = False
            lower_i = i.lower()
            
            for j in left_file_lines:
                if lower_i == j.lower():
                    result_lines.append(f'{i}|{j}')
                    found = True
                    break
            
            if not found:
                result_lines.append(f'{i}|{None}')

    if unique:
        result_lines = list(dict.fromkeys(result_lines))

    return result_lines

def inner_join(left_file_lines,right_file_lines,unique=False,case_sensitive=True):
    result_lines = []

    if case_sensitive:
        for line in right_file_lines:
            if line in left_file_lines:
                result_lines.append(f'{line}|{line}')
    else:
        for line in right_file_lines:
            found = False
            lower_line = line.lower()
            
            for left_line in left_file_lines:
                if lower_line == left_line.lower():
                    result_lines.append(f'{line}|{left_line}')
                    found = True
                    break
            
            if not found:
                result_lines.append(f'{line}|{None}')
    
    if unique:
        result_lines = list(dict.fromkeys(result_lines))

    return result_lines

def outer_join(left_file_lines,right_file_lines,unique=False,case_sensitive=True):
    result_lines = []

    if case_sensitive:
        for i in left_file_lines:
            if not i in right_file_lines:
                result_lines.append(f'{i}|None')
        for i in right_file_lines:
            if not i in left_file_lines:
                result_lines.append(f'None|{i}')
    else:
        for i in left_file_lines:
            found = False
            lower_i = i.lower()
            
            for j in right_file_lines:
                if lower_i == j.lower():
                    found = True
                    break
            
            if not found:
                result_lines.append(f'{i}|None')

        for i in right_file_lines:
            found = False
            lower_i = i.lower()
            
            for j in left_file_lines:
                if lower_i == j.lower():
                    found = True
                    break
            
            if not found:
                result_lines.append(f'None|{i}')
    if unique:
        result_lines = list(dict.fromkeys(result_lines))

    return result_lines

def full_outer_join(left_file_lines,right_file_lines,unique=False,case_sensitive=True):
    result_lines = []

    if case_sensitive:
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
    else:
        for i in left_file_lines:
            found = False
            lower_i = i.lower()
            
            for j in right_file_lines:
                if lower_i == j.lower():
                    result_lines.append(f'{i}|{j}')
                    found = True
                    break
            
            if not found:
                result_lines.append(f'{i}|None')

        for i in right_file_lines:
            found = False
            lower_i = i.lower()
            
            for j in left_file_lines:
                if lower_i == j.lower():
                    result_lines.append(f'{i}|{j}')
                    found = True
                    break
            
            if not found:
                result_lines.append(f'None|{i}')

    if unique:
        result_lines = list(dict.fromkeys(result_lines))

    return result_lines
