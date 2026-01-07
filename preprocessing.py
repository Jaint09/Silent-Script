import numpy as np
import cv2
import os
import csv
from image_processing import process_image

# Create necessary directories if they don't exist
if not os.path.exists("data"):
    os.makedirs("data")
if not os.path.exists(os.path.join("data", "train")):
    os.makedirs(os.path.join("data", "train"))
if not os.path.exists(os.path.join("data", "test")):
    os.makedirs(os.path.join("data", "test"))

# <-- IMPORTANT: use a raw string (r"...") or double backslashes to avoid escape sequences like \t
path = r"E:\Hackathon Project\Silent_Script\data\Processed_Images\train"
path1 = "data"
a = ['label']

# quick diagnostics
print("DEBUG: Input path (raw):", path)
print("DEBUG: exists?", os.path.exists(path))
if os.path.exists(path):
    print("DEBUG: immediate entries:", os.listdir(path))
else:
    print("ERROR: Input path does not exist. Fix the path and re-run.")
    # stop early so you don't get zero results silently
    raise SystemExit("Stopping: input folder not found.")

# Create pixel header names (unused later but kept as original)
for i in range(64*64):
    a.append("pixel" + str(i))

label = 0
var = 0
c1 = 0
c2 = 0

# Walk through class folders located under 'path'
for class_name in os.listdir(path):
    class_folder = os.path.join(path, class_name)
    if not os.path.isdir(class_folder):
        continue

    print("Processing class folder:", class_name)
    # list only image files
    files = [f for f in os.listdir(class_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
    print(f"  found {len(files)} files in {class_folder}")

    # create dest folders
    train_dir = os.path.join(path1, "train", class_name)
    test_dir = os.path.join(path1, "test", class_name)
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    num = int(0.8 * len(files)) if len(files) > 0 else 0
    i = 0
    for file in files:
        var += 1
        actual_path = os.path.join(class_folder, file)
        actual_path1 = os.path.join(train_dir, file)
        actual_path2 = os.path.join(test_dir, file)

        # process image
        bw_image = process_image(actual_path)

        if bw_image is None:
            print(f"[SKIP] Could not process: {actual_path}")
            i += 1
            continue

        if i < num:
            c1 += 1
            cv2.imwrite(actual_path1, bw_image)
        else:
            c2 += 1
            cv2.imwrite(actual_path2, bw_image)

        i += 1

    label += 1

print("TOTAL scanned (var):", var)
print("TOTAL saved to train (c1):", c1)
print("TOTAL saved to test  (c2):", c2)
