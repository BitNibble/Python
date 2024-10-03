# callback_logic.py
import os
from file_utils import find_duplicates, remove_duplicates

def process_inputs(location, extension, depth):
    """Process the inputs received from the GUI."""
    if not os.path.isdir(location):
        return f"Folder '{location}' does not exist!"
    
    duplicates = find_duplicates(location, extension, depth)
    if not duplicates:
        return "No duplicates found."
    
    remove_duplicates(duplicates)
    return "Duplicate removal complete."
