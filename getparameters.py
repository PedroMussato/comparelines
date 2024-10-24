def get_right_file(args):
    """
    return the right file or None
    """

    file = None

    try:
        i = args.index('-r')
    except:
        pass
    else:
        file = args[i+1]

    try:
        i = args.index('--right-file')
    except:
        pass
    else:
        file = args[i+1]

    return file

def get_left_file(args):
    """
    return the left file or None
    """

    file = None

    try:
        i = args.index('-l')
    except:
        pass
    else:
        file = args[i+1]

    try:
        i = args.index('--left-file')
    except:
        pass
    else:
        file = args[i+1]

    return file

def get_unique_param(args):
    unique = False

    try:
        i = args.index('--unique')
    except:
        pass
    else:
        unique = True

    return unique

def get_join_param(args):
    """
    return the join type (left, right, inner, outer, full-outer) file or None
    """

    join_type = None

    try:
        i = args.index('-j')
    except:
        pass
    else:
        join_type = args[i+1]

    try:
        i = args.index('--join')
    except:
        pass
    else:
        join_type = args[i+1]

    if not join_type in ['left', 'right', 'inner', 'outer', 'full-outer']:
        join_type = None

    return join_type

def get_output_param(args):
    """
    return the left file or None
    """

    output = None

    try:
        i = args.index('-o')
    except:
        pass
    else:
        output = args[i+1]

    try:
        i = args.index('--output')
    except:
        pass
    else:
        output = args[i+1]

    return output

def get_left_column_param(args):
    delimiter = None
    column_number = None

    try:
        i = args.index('--left-column')
    except:
        pass
    else:
        delimiter = args[i+1]
        column_number = args[i+2]
        
    return delimiter, column_number

def get_right_column_param(args):
    delimiter = None
    column_number = None

    try:
        i = args.index('--right-column')
    except:
        pass
    else:
        delimiter = args[i+1]
        column_number = args[i+2]
        
    return delimiter, column_number

def get_no_case_sensitive_param(args):
    case_sensitive = True
    
    try:
        i = args.index('--no-case-sensitive')
    except:
        pass
    else:
        case_sensitive = False
        
    return case_sensitive