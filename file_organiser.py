import os
import shutil

# Dictionary that maps folder names to file extensions
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"],
    "Scripts": [".py", ".ipynb", ".sql"],
}

def organize_files(folder_path):
    # Check if the given folder exists
    if not os.path.exists(folder_path):
        print("❌ Folder not found!")
        return

    # Loop through all files in the given folder
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        # Skip directories (only organize files)
        if os.path.isdir(file_path):
            continue

        # Extract file extension (e.g., .txt, .jpg)
        file_ext = os.path.splitext(file)[1].lower()

        moved = False  # Flag to check if file was moved

        # Check file extension against defined categories
        for folder_name, extensions in FILE_TYPES.items():
            if file_ext in extensions:
                # Create target folder if it doesn't exist
                target_folder = os.path.join(folder_path, folder_name)
                os.makedirs(target_folder, exist_ok=True)

                # Move file to its category folder
                shutil.move(file_path, os.path.join(target_folder, file))
                moved = True
                break

        # If file type didn't match any category
        if not moved:
            other_folder = os.path.join(folder_path, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, file))

    print("✅ Files organized successfully!")


# Program entry point
if __name__ == "__main__":
    # Take folder path from user
    path = input("Enter folder path to organize: ").strip()
    organize_files(path)
