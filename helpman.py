usage = \
"""\
NAME
    compareline - Compare lines between two files

SYNOPSIS
    compareline --left-file <file1> --right-file <file2> --join <type> [OPTIONS]

DESCRIPTION
    Compares the lines in <file1> against the lines in <file2>. By default, it checks if the lines from <file1> exist in <file2> and prints the matching lines.

OPTIONS
    -l, --left-file <file1>
        Specify the left file to compare.

    -r, --right-file <file2>
        Specify the right file to compare.

    -j, --join <type>
        Specify the type of join to perform between the two files. The following join types are supported:
        
        - `left`: Perform a left join, returning all lines from the left file and the matching lines from the right file. Lines in the left file that do not have a match in the right file will be included with `NaN` for the right file's columns.
        
        - `right`: Perform a right join, returning all lines from the right file and the matching lines from the left file. Lines in the right file that do not have a match in the left file will be included with `NaN` for the left file's columns.
        
        - `inner`: Perform an inner join, returning only the lines that have matches in both files.
        
        - `outer`: Perform an outer join, returning all unique lines from both files, including lines that do not have matches in the other file.
        
        - `full-outer`: Perform a full outer join, returning all unique lines from both files.

    -u, --unique
        Remove duplicate lines from both input files before comparison, preserving the order of appearance.
    
    --no-case-sensitive
        Perform a case-insensitive comparison of lines between the two files. When this option is specified, the comparison will treat lines as equal regardless of letter casing. By default, comparisons are case-sensitive.

    --left-column <delimiter> <column number>
        Select a specific column from the left file. The line will be split using <delimiter>, and <column number> specifies which column to select (1-based index).

    --right-column <delimiter> <column number>
        Select a specific column from the right file. The line will be split using <delimiter>, and <column number> specifies which column to select (1-based index).

    -o, --output <output file>
        Write the output to the specified <output file>.

EXAMPLES
    Compare lines in file1.txt with file2.txt:
        compareline --left-file file1.txt --right-file file2.txt

    Compare lines in file2.txt against file1.txt:
        compareline --left-file file1.txt --right-file file2.txt --reverse

    Remove duplicates and compare:
        compareline --left-file file1.txt --right-file file2.txt --unique

    Select specific columns for comparison:
        compareline --left-file file1.txt --right-file file2.txt --left-column "," 2 --right-column "," 1

    Redirect output to a file:
        compareline --left-file file1.txt --right-file file2.txt -o output.txt
"""
