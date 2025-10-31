import os
import shutil
source_folder = r"C:\Users\jagad\OneDrive\Desktop\images"
destination_folder = r"C:\Users\jagad\OneDrive\Desktop\images\Photos_Only"
os.makedirs(destination_folder, exist_ok=True)
for file in os.listdir(source_folder):
    if file.lower().endswith(".jpg"):  # covers .JPG also
        shutil.move(os.path.join(source_folder, file),
                    os.path.join(destination_folder, file))
print("All JPG files moved successfully!")
