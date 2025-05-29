import os

def rename_images(folder_path):
    for filename in os.listdir(folder_path):
        name, ext = os.path.splitext(filename)
        
        # Only process if "_out" is at the end of the name (before extension)
        if name.endswith("_out"):
            new_name = name[:-4] + ext  # Remove the last 4 characters ('_out')
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} → {new_name}")

if __name__ == "__main__":
    folder = input("Enter the folder path with images: ").strip()
    if os.path.isdir(folder):
        rename_images(folder)
    else:
        print("❌ Folder not found. Please check the path.")
