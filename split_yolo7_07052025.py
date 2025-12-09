'''
Split the dataset into train, test, and valid (80%, 10%, 10%) 
'''

import os
import shutil
import random
from pathlib import Path

# Input paths
label_dir = r"D:\Michael Sam\Projects\YoloTraining\Dataset\Z_DVC_Dataset_Z\Z_Final Dataset After Annotation with Label_Z\Missed Label\Missed_Labels(Yolov8)\labels"
image_dir = r"D:\Michael Sam\Projects\YoloTraining\Dataset\Z_DVC_Dataset_Z\Z_Final Dataset After Annotation with Label_Z\Missed Label\Missed_Labels(Yolov8)\images"

# Output base
output_base = r"D:\Michael Sam\Projects\YoloTraining\Output\DVC\Missed Small Controls"
image_out = os.path.join(output_base, "images")
label_out = os.path.join(output_base, "labels")

# Create folders
for split in ["train", "test", "valid"]:
    os.makedirs(os.path.join(image_out, split), exist_ok=True)
    os.makedirs(os.path.join(label_out, split), exist_ok=True)

# Get all image files with extensions
image_exts = [".jpg", ".jpeg", ".png", ".bmp"]
image_files = {Path(f).stem: f for f in os.listdir(image_dir) if Path(f).suffix.lower() in image_exts}

# Get all label files
label_files = [f for f in os.listdir(label_dir) if f.endswith(".txt")]

# Match labels with available images
matched_pairs = []
for label_file in label_files:
    stem = Path(label_file).stem
    if stem in image_files:
        matched_pairs.append((os.path.join(image_dir, image_files[stem]), os.path.join(label_dir, label_file)))

print(f"Total matched label-image pairs: {len(matched_pairs)}")

# Shuffle and split
random.shuffle(matched_pairs)
total = len(matched_pairs)
train_split = int(0.8 * total)
valid_split = int(0.1 * total)

splits = {
    "train": matched_pairs[:train_split],
    "valid": matched_pairs[train_split:train_split + valid_split],
    "test": matched_pairs[train_split + valid_split:]
}

# Copy files
for split, pairs in splits.items():
    for img_path, lbl_path in pairs:
        shutil.copy(img_path, os.path.join(image_out, split, os.path.basename(img_path)))
        shutil.copy(lbl_path, os.path.join(label_out, split, os.path.basename(lbl_path)))

print("✅ Split completed and files copied.")
