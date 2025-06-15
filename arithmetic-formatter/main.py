def arithmetic_arranger(problems, show_answers=False):
    # Error checks
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_lines = []
    second_lines = []
    dash_lines = []
    answer_lines = []
    
    for prob in problems:
        parts = prob.split()
        a, op, b = parts
        
        if op not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not a.isdigit() or not b.isdigit():
            return "Error: Numbers must only contain digits."
        if len(a) > 4 or len(b) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        width = max(len(a), len(b)) + 2
        
        # Line 1: top operand
        first_lines.append(a.rjust(width))
        # Line 2: operator and bottom operand
        second_lines.append(op + b.rjust(width - 1))
        # Line 3: dashes
        dash_lines.append('-' * width)
        
        # Line 4: answer (if needed)
        if show_answers:
            result = str(int(a) + int(b)) if op == '+' else str(int(a) - int(b))
            answer_lines.append(result.rjust(width))
    
    spacer = '    '
    arranged = spacer.join(first_lines) + '\n' + spacer.join(second_lines) + '\n' + spacer.join(dash_lines)
    if show_answers:
        arranged += '\n' + spacer.join(answer_lines)
    return arranged

# Test cases
test_cases = [
    (["3801 - 2", "123 + 49"], False),
    (["1 + 2", "1 - 9380"], False),
    (["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], False),
    (["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"], False),
    (["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"], False),
    (["3 / 855", "3801 - 2", "45 + 43", "123 + 49"], False),
    (["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"], False),
    (["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"], False),
    (["3 + 855", "988 + 40"], True),
    (["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)
]

for i, (probs, show) in enumerate(test_cases, 1):
    print(f"Test {i}:")
    print(arithmetic_arranger(probs, show))
    print()