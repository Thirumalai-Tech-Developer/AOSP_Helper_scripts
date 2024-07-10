import os
import shutil

def copy_files_with_structure(input_file, output_dir, missing_files_output):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file, 'r') as file:
        paths = file.readlines()

    missing_files = []

    for path in paths:
        path = path.strip()
        if os.path.exists(path):
            # Determine the relative path from the input file list
            rel_path = os.path.relpath(path, start=os.path.commonpath(paths))
            dest_path = os.path.join(output_dir, rel_path)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.copy(path, dest_path)
        else:
            missing_files.append(path)

    with open(missing_files_output, 'w') as file:
        for path in missing_files:
            file.write(path + '\n')

# Example usage:
input_file = 'name.txt'
output_dir = 'vendor_tree'
missing_files_output = 'missing_files.txt'
copy_files_with_structure(input_file, output_dir, missing_files_output)
