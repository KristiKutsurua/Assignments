with open('sample_file.txt', 'w') as file:
    for i in range(1, 1001):
        file.write(f"Line {i}: sample text.\n")

filled_lines = 0
with open('sample_file.txt', 'r') as file:
    lines = file.readlines()
    total_lines = len(lines)
    for line in lines:
        if line.strip():
            filled_lines += 1

print(f"Total lines: {total_lines}")
print(f"Filled lines: {filled_lines}")
