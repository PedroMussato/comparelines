import sys
from helpman import usage
from getparameters import (
    get_left_file,
    get_right_file,
    get_join_param,
    get_unique_param,
    get_output_param,
    get_left_column_param,
    get_right_column_param
)
from joins import (
    left_join,
    right_join,
    inner_join,
    outer_join,
    full_outer_join
)

if len(sys.argv) < 5:
    print("ERROR : Not enought parameters.")
    print(usage)
    sys.exit(1)

left_file_path = get_left_file(sys.argv)
right_file_path = get_right_file(sys.argv)
join_type = get_join_param(sys.argv)
unique = get_unique_param(sys.argv)
output = get_output_param(sys.argv)
left_column_delimiter, left_column_number = get_left_column_param(sys.argv) 
right_column_delimiter, right_column_number = get_right_column_param(sys.argv) 




if left_file_path and right_file_path and join_type and join_type:
    with open(left_file_path,'r') as left_file:
        left_file_lines = left_file.read().split('\n')

    with open(right_file_path,'r') as right_file:
        right_file_lines = right_file.read().split('\n')

    if left_column_delimiter or left_column_number:
        if left_column_delimiter and left_column_number:
            left_file_lines = [i.split(left_column_delimiter)[int(left_column_number)] for i in left_file_lines]            
        else:
            print("ERROR : error on left delimiter or left column number")
            print(usage)
            sys.exit(1)

    if right_column_delimiter or right_column_number:
        if right_column_delimiter and right_column_number:
            right_file_lines = [i.split(right_column_delimiter)[int(right_column_number)] for i in right_file_lines]            
        else:
            print("ERROR : error on right delimiter or right column number")
            print(usage)
            sys.exit(1)

    if join_type == 'left':
        result_lines = left_join(left_file_lines,right_file_lines,unique)
    elif join_type == 'right':
        result_lines = right_join(left_file_lines,right_file_lines,unique)
    elif join_type == 'inner':
        result_lines = inner_join(left_file_lines,right_file_lines,unique)
    elif join_type == 'outer':
        result_lines = outer_join(left_file_lines,right_file_lines,unique)
    elif join_type == 'full-outer':
        result_lines = full_outer_join(left_file_lines,right_file_lines,unique)

    if output:
        with open(output, 'w') as output_file:
            for line in result_lines:
                output_file.write(f'{line}\n')
    else:
        for line in result_lines:
            print(line)

else:
    print("ERROR : left_file_path or right_file_path or join_type or join_type not specified")
    print(usage)
    sys.exit(1)
