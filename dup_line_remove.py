def remove_duplicate_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Using a set to keep track of seen lines
    seen_lines = set()
    unique_lines = []
    
    for line in lines:
        if line not in seen_lines:
            unique_lines.append(line)
            seen_lines.add(line)
    
    with open(file_path, 'w') as file:
        file.writelines(unique_lines)

# Example usage
file_path = 'pro.txt'
remove_duplicate_lines(file_path)

