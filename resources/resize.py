from PIL import Image
import os

# Input and output directory paths
input_dir = "D:\PROJECTS\Attendance_system\images"
output_dir = "D:\PROJECTS\Attendance_system"

# Target width and height for resizing
target_width = 216
target_height = 216

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Loop through the files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith((".jpg", ".jpeg", ".png")):
        with Image.open(os.path.join(input_dir, filename)) as img:
            img = img.resize((target_width, target_height))
            img.save(os.path.join(output_dir, filename))
            print(f"Resized {filename}")

print("All images resized.")
