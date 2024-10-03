import tkinter as tk
import os
from event_handlers import register_events  # Import the event handlers

# Shared dictionary to store inputs
inputs = {}

def start_gui():
    def run_duplicate_remover():
        location = location_entry.get()
        extension = extension_entry.get()
        try:
            depth = int(depth_entry.get())
        except ValueError:
            print("Input Error: Depth must be an integer.")
            return

        if depth < 0:
            print("Input Error: Depth must be a non-negative integer.")
            return

        if not os.path.isdir(location):
            print(f"Input Error: Folder '{location}' does not exist!")
            return

        # Store inputs in the shared dictionary
        inputs['location'] = location
        inputs['extension'] = extension
        inputs['depth'] = depth
        
        # Show a confirmation message in terminal
        print("Success: Inputs collected! You can now run the main script.")
        
        # Clear the input fields
        location_entry.delete(0, tk.END)
        extension_entry.delete(0, tk.END)
        depth_entry.delete(0, tk.END)

    # Create the main window
    root = tk.Tk()
    root.title("Duplicate File Remover")
    root.geometry("400x300")  # Set the window size

    # Location input
    tk.Label(root, text="Location:").pack(pady=5)
    location_entry = tk.Entry(root, width=50)
    location_entry.pack(pady=5)

    # Extension input
    tk.Label(root, text="Extension (e.g., .txt):").pack(pady=5)
    extension_entry = tk.Entry(root, width=50)
    extension_entry.pack(pady=5)

    # Depth input
    tk.Label(root, text="Depth (0 or more):").pack(pady=5)
    depth_entry = tk.Entry(root, width=10)
    depth_entry.pack(pady=5)

    # Run button
    run_button = tk.Button(root, text="Run", command=run_duplicate_remover)
    run_button.pack(pady=20)

    # Register events for mouse and keyboard
    register_events(root)

    # Start the GUI event loop
    root.mainloop()
