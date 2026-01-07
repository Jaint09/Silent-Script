import numpy as np
import cv2
import os

folder_path = r"E:\Hackathon Project\Silent_Script\data\train"
# Specify the output folder path
output_folder_path = r"E:\Hackathon Project\Silent_Script\data\Processed_Images\train"

print("Path exists? ->", os.path.exists(folder_path))

minValue = 70

def process_image(image_path):
    frame = cv2.imread(image_path)
    if frame is None:
        print(f"Error: Could not read the image {image_path}. Check the file path.")
        return None
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 2)

    th3 = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    ret, res = cv2.threshold(th3, minValue, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    return res  


def process_images_in_folder(folder_path, output_folder_path):
    # Output ka root folder banado (Processed_Images\train)
    if output_folder_path and not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    for root, dirs, files in os.walk(folder_path):
        # root ko folder_path se relative bana rahe hain
        # Example:
        # root = E:\...\train\A  -> rel_path = A
        # root = E:\...\train\0  -> rel_path = 0
        rel_path = os.path.relpath(root, folder_path)

        for filename in files:
            if filename.lower().endswith(('.jpg')):
                image_path = os.path.join(root, filename)
                processed_image = process_image(image_path)

                if processed_image is not None:
                    # Jis folder me original thi, usi relative folder me save karo
                    save_dir = os.path.join(output_folder_path, rel_path)
                    os.makedirs(save_dir, exist_ok=True)  # subfolder exist na ho to bana do

                    processed_image_path = os.path.join(save_dir, f"processed_{filename}")
                    cv2.imwrite(processed_image_path, processed_image)
                    print(f"Processed image saved as: {processed_image_path}")


process_images_in_folder(folder_path, output_folder_path)