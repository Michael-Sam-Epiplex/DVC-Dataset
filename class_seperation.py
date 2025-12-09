import os
# Define control groups
small_controls = {0, 1, 2, 3, 4, 5, 9, 13, 14, 15, 19, 20, 25}
big_controls = {6, 7, 8, 10, 12, 18, 23, 24, 26, 27, 28}
input_dir = "C:\\Users\\Mithun.akkadka\\Downloads\\labels-20250228T065218Z-001\\labels"  
big_control_dir = "D:\\YOLO_MODEL\\Big_control_07052025"  
small_control_dir = "D:\\YOLO_MODEL\\Small_control_07052025"  

# Create output directories if they don't exist
os.makedirs(big_control_dir, exist_ok=True)
os.makedirs(small_control_dir, exist_ok=True)

# Process each .txt file
for file_name in os.listdir(input_dir):
    if file_name.endswith(".txt"):
        file_path = os.path.join(input_dir, file_name)
        small_control_lines = []
        big_control_lines = []
        # Read and classify lines
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.split()
                if not parts:
                    continue  # Skip empty lines
                try:
                    control_number = int(parts[0])  # First number in each line
                except ValueError:
                    print(f"Skipping invalid line in {file_name}: {line.strip()}")
                    continue
                # Append to the appropriate list
                if control_number in small_controls:
                    small_control_lines.append(line)
                elif control_number in big_controls:
                    big_control_lines.append(line)

        # Write the results to new files in respective folders
        if big_control_lines:
            with open(os.path.join(big_control_dir, file_name), 'w') as big_file:
                big_file.writelines(big_control_lines)

        if small_control_lines:
            with open(os.path.join(small_control_dir, file_name), 'w') as small_file:
                small_file.writelines(small_control_lines)
