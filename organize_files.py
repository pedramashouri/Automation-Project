import os
import shutil

source_folder = "C:/Users/EXO/Desktop/Files"  # مسیر پوشه منبع رو چک کن
destination_folders = {
    "Images": ".jpg .png .jpeg",
    "Videos": ".mp4 .avi .mkv",
    "Documents": ".pdf .docx .txt",
    "Music": ".mp3"
}

for filename in os.listdir(source_folder):
    if os.path.isfile(os.path.join(source_folder, filename)):
        file_extension = os.path.splitext(filename)[1].lower()
        for folder, extensions in destination_folders.items():
            if file_extension in extensions.split():
                destination_path = os.path.join(source_folder, folder)
                if not os.path.exists(destination_path):
                    os.makedirs(destination_path)
                shutil.move(os.path.join(source_folder, filename), os.path.join(destination_path, filename))
                break


            



#python organize_files.py توی ترمینال


