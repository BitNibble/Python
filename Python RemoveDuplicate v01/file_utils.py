import os
import hashlib

def get_file_hash(file_path):
    """Generate a hash for a file to compare its content."""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def find_duplicates(location, extension, depth):
    """Find duplicate files with the specified extension up to the given depth."""
    file_dict = {}
    for root, dirs, files in os.walk(location):
        current_depth = root.count(os.sep) - location.count(os.sep)
        if current_depth > depth:
            continue
        for file in files:
            if file.lower().endswith(extension.lower()):
                file_path = os.path.join(root, file)
                file_hash = get_file_hash(file_path)
                if file_hash in file_dict:
                    file_dict[file_hash].append(file_path)
                else:
                    file_dict[file_hash] = [file_path]
    return {k: v for k, v in file_dict.items() if len(v) > 1}

def remove_duplicates(duplicates):
    """Remove duplicate files, keeping the one higher in the directory tree."""
    for file_hash, file_paths in duplicates.items():
        # Sort paths to ensure we remove the one lower in the hierarchy
        file_paths.sort(key=lambda x: x.count(os.sep))
        # Remove all but the first file in the sorted list
        for file_path in file_paths[1:]:
            print(f"Removing duplicate file: {file_path}")
            os.remove(file_path)
