from  import arithmetic_arranger

# Test the current implementation
problems = ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]
expected_output = '   11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------'

result = arithmetic_arranger(problems)
print("Current result:")
print(repr(result))
print("\nExpected:")
print(repr(expected_output))
print(f"\nMatch: {result == expected_output}")

# Let's check each problem individually
print("\n=== INDIVIDUAL PROBLEM ANALYSIS ===")
for i, problem in enumerate(problems):
    parts = problem.split()
    num1, operator, num2 = parts
    
    second_line_content = operator + ' ' + num2
    current_width = max(len(num1) + 1, len(second_line_content))
    
    # Test this problem individually
    individual_result = arithmetic_arranger([problem])
    individual_lines = individual_result.split('\n')
    
    print(f"\nProblem {i+1}: '{problem}'")
    print(f"  Current width calculation: max({len(num1)} + 1, {len(second_line_content)}) = {current_width}")
    print(f"  Individual result:")
    for j, line in enumerate(individual_lines):
        print(f"    Line {j+1}: '{line}' (len={len(line)})")
    
    # Extract expected parts from the full expected output
    expected_lines = expected_output.split('\n')
    expected_parts = []
    for line in expected_lines:
        parts_in_line = line.split('    ')
        if i < len(parts_in_line):
            expected_parts.append(parts_in_line[i])
    
    print(f"  Expected parts:")
    for j, part in enumerate(expected_parts):
        print(f"    Line {j+1}: '{part}' (len={len(part)})")
    
    # Compare
    matches = [individual_lines[j] == expected_parts[j] for j in range(len(individual_lines))]
    print(f"  Matches: {matches}")
    
    if not all(matches):
        # Let's see what width would work
        for test_width in range(1, 10):
            test_first = num1.rjust(test_width)
            if test_first == expected_parts[0]:
                print(f"  *** SOLUTION: Width {test_width} would work for first line ***")
                break

# Let's also check the spacing between problems
print("\n=== SPACING ANALYSIS ===")
result_lines = result.split('\n')
expected_lines = expected_output.split('\n')

for i, (result_line, expected_line) in enumerate(zip(result_lines, expected_lines)):
    print(f"\nLine {i+1}:")
    print(f"  Result:   '{result_line}' (len={len(result_line)})")
    print(f"  Expected: '{expected_line}' (len={len(expected_line)})")
    print(f"  Match: {result_line == expected_line}")
    
    if result_line != expected_line:
        # Find the first difference
        for j, (r_char, e_char) in enumerate(zip(result_line, expected_line)):
            if r_char != e_char:
                print(f"  First difference at position {j}: got '{r_char}', expected '{e_char}'")
                break
        if len(result_line) != len(expected_line):
            print(f"  Length difference: got {len(result_line)}, expected {len(expected_line)}")