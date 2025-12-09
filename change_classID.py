import os

# Define the mapping for big control indices
big_control_mapping = {
    6: 0,   # List box
    7: 1,   # Tree
    8: 2,   # Grid
    10: 3,  # Menu bar
    12: 4,  # Title bar
    18: 5,  # Tool bar
    23: 6,  # Calendar Control
    24: 7,  # Cursor button (mouse)
    26: 8,  # Horizontal scroll bar
    27: 9,  # Vertical scroll bar
    28: 10  # Title
}

# Paths for big control folder
big_control_dir = "D:\\YOLO_MODEL\\big_control"  # Replace with your big control folder path
output_dir = "D:\\YOLO_MODEL\\big_Output_control"  # Replace with your desired output folder path

# Create the output folder if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Process each .txt file in the big control folder
for file_name in os.listdir(big_control_dir):
    if file_name.endswith(".txt"):
        input_file_path = os.path.join(big_control_dir, file_name)
        output_file_path = os.path.join(output_dir, file_name)
        modified_lines = []

        # Read and modify lines
        with open(input_file_path, 'r') as file:
            for line in file:
                parts = line.split()
                if not parts:
                    continue  # Skip empty lines
                try:
                    control_number = int(parts[0])  # First number in each line
                except ValueError:
                    print(f"Skipping invalid line in {file_name}: {line.strip()}")
                    continue
                # Update the control number based on the mapping
                if control_number in big_control_mapping:
                    parts[0] = str(big_control_mapping[control_number])
                    modified_lines.append(" ".join(parts) + "\n")

        # Write the modified lines to the output file
        with open(output_file_path, 'w') as file:
            file.writelines(modified_lines)

        print(f"Modified file saved: {output_file_path}")
