from pathlib import Path
import shutil

def remove_empty_folders(path):
    for folder in sorted(path.rglob("*"), reverse=True):
        if folder.is_dir() and not any(folder.iterdir()): #Check if folder empty
            try:
                folder.rmdir()
                print(f"Remove empty folder {folder}")
            except OSError as e:
                print(f"Error removing folder {folder}: {e}")

def organize_file_recursively(base_path):
    archive_path = base_path / 'Archives'
    archive_path.mkdir(parents=True, exist_ok=True)
    
    for item in base_path.rglob('*'):
#Skip directories, process only files        
        if item.is_dir():
            continue

#Determine file extension
        file_extension = item.suffix.lstrip('.').lower()
        if not file_extension:
            continue

        if file_extension in ('zip', 'tar', 'gztar'):
            extract_dir = archive_path / item.stem
            extract_dir.mkdir(parents=True, exist_ok=True)

            try:
                shutil.unpack_archive(str(item), extract_dir)
            except (shutil.ReadError, FileNotFoundError) as e:
                print(f"Error extracting {item}: {e}")
            item.unlink()  #Remove the original archive
            continue

        #Move file to directories based on their extensions
        target_dir = base_path / file_extension.upper()
        target_dir.mkdir(parents=True, exist_ok=True)
        try:
            shutil.move(str(item), target_dir / item.name)
        except Exception as e:
            print(f"Error moving {item}: {e}")

    remove_empty_folders(base_path)
    print(f"Files in {base_path} organizing recursively")


if __name__ == "__main__":
    parents_folder_path = Path('file_tree')
    organize_file_recursively(parents_folder_path)
