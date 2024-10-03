import tkinter as tk

def on_mouse_click(event):
    print(f"Mouse clicked at: ({event.x}, {event.y})")  # Print to terminal

def on_key_press(event):
    print(f"Key pressed: {event.char}")  # Print to terminal

def register_events(root):
    root.bind("<Button-1>", on_mouse_click)  # Left mouse button click
    root.bind("<KeyPress>", on_key_press)  # Key press event
