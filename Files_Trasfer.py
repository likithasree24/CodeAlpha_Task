import os
import shutil
source_folder = "C:\Users\LIKITHA SREE\Desktop\Images"
destination_folder = "C:\Users\LIKITHA SREE\Desktop\Images\Photos_Only"
os.makedirs(destination_folder, exist_ok=True)
for file in os.listdir(source_folder):
    if file.lower().endswith(".jpg"):  # covers .JPG also
        shutil.move(os.path.join(source_folder, file),
                    os.path.join(destination_folder, file))
print("All JPG files moved successfully!")

