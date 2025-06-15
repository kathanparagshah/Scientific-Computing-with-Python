def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_line = []
    second_line = []
    dash_line = []
    answer_line = []
    
    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."
        
        a, operator, b = parts
        
        # Check if operator is valid
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        # Check if operands contain only digits
        if not a.isdigit() or not b.isdigit():
            return "Error: Numbers must only contain digits."
        
        # Check if operands are not more than 4 digits
        if len(a) > 4 or len(b) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Calculate the width needed
        second_line_content = operator + ' ' + b
        width = max(len(a) + 1, len(second_line_content))
        
        # Format the lines
        first_line.append(a.rjust(width))
        second_line.append(second_line_content.rjust(width))
        dash_line.append('-' * width)
        
        # Calculate answer if needed
        if show_answers:
            if operator == '+':
                answer = str(int(a) + int(b))
            else:
                answer = str(int(a) - int(b))
            answer_line.append(answer.rjust(width))
    
    # Join the lines with 4 spaces between problems
    result = '    '.join(first_line) + '\n'
    result += '    '.join(second_line) + '\n'
    result += '    '.join(dash_line)
    
    if show_answers:
        result += '\n' + '    '.join(answer_line)
    
    return result