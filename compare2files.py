def compare_files(file1_path, file2_path, common_path, no1_path, no2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        file1_lines = set(file1.readlines())
        file2_lines = set(file2.readlines())
    
    common_lines = file1_lines & file2_lines
    only_file1_lines = file1_lines - file2_lines
    only_file2_lines = file2_lines - file1_lines

    with open(common_path, 'w') as common_file:
        common_file.writelines(common_lines)
    
    with open(no1_path, 'w') as no1_file:
        no1_file.writelines(only_file1_lines)
    
    with open(no2_path, 'w') as no2_file:
        no2_file.writelines(only_file2_lines)

# File paths
file1_path = 'name1.txt'
file2_path = 'name2.txt'
common_path = 'common.txt'
no1_path = 'name1_extra.txt'
no2_path = 'name2_extra.txt'

# Compare files
compare_files(file1_path, file2_path, common_path, no1_path, no2_path)

