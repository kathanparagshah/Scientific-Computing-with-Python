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
            continue
        
        num1, operator, num2 = parts
        
        # Check for valid operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        # Check if numbers contain only digits
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        
        # Check if numbers are more than four digits
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Calculate the width needed for this problem
        width = max(len(num1), len(num2)) + 2
        
        # Format the first line (first number, right-aligned)
        first_line.append(num1.rjust(width))
        
        # Format the second line: operator + space + num2 right-aligned in remaining space
        second_line.append(operator + ' ' + num2.rjust(width - 2))
        
        # Format the dash line
        dash_line.append('-' * width)
        
        # Calculate and format the answer if needed
        if show_answers:
            if operator == '+':
                result = int(num1) + int(num2)
            else:
                result = int(num1) - int(num2)
            answer_line.append(str(result).rjust(width))
    
    # Join the lines with appropriate spacing
    result_lines = [
        '    '.join(first_line),
        '    '.join(second_line),
        '    '.join(dash_line)
    ]
    
    if show_answers:
        result_lines.append('    '.join(answer_line))
    
    return '\n'.join(result_lines)

# Test all cases
test_cases = [
    # Test 1 - FAILING
    (["3801 - 2", "123 + 49"], False, "  3801      123\n-    2    +  49\n------    -----"),
    
    # Test 2 - PASSING
    (["1 + 2", "1 - 9380"], False, "  1         1\n+ 2    - 9380\n---    ------"),
    
    # Test 3 - FAILING
    (["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], False, "    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----"),
    
    # Test 4 - FAILING
    (["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"], False, "   11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------"),
    
    # Test 5 - PASSING
    (["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"], False, "Error: Too many problems."),
    
    # Test 6 - PASSING
    (["3 / 855", "3801 - 2", "45 + 43", "123 + 49"], False, "Error: Operator must be '+' or '-'."),
    
    # Test 7 - PASSING
    (["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"], False, "Error: Numbers cannot be more than four digits."),
    
    # Test 8 - PASSING
    (["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"], False, "Error: Numbers must only contain digits."),
    
    # Test 9 - FAILING
    (["3 + 855", "988 + 40"], True, "    3      988\n+ 855    +  40\n-----    -----\n  858     1028"),
    
    # Test 10 - FAILING
    (["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True, "   32         1      45      123      988\n- 698    - 3801    + 43    +  49    +  40\n-----    ------    ----    -----    -----\n -666     -3800      88      172     1028")
]

print("Testing all cases...\n")

for i, (problems, show_answers, expected) in enumerate(test_cases, 1):
    result = arithmetic_arranger(problems, show_answers)
    passed = result == expected
    status = "PASS" if passed else "FAIL"
    
    print(f"Test {i}: {status}")
    if not passed:
        print(f"  Input: {problems}, show_answers={show_answers}")
        print(f"  Expected: {repr(expected)}")
        print(f"  Got:      {repr(result)}")
        print()

print("\nSummary:")
passing = sum(1 for i, (problems, show_answers, expected) in enumerate(test_cases) 
              if arithmetic_arranger(problems, show_answers) == expected)
print(f"Passing: {passing}/{len(test_cases)} tests")