import socket
import tkinter as tk
from tkinter import messagebox

# Function to connect to ESP8266
def connect_to_esp():
    global client_socket
    try:
        # Set up socket connection
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ESP_IP, ESP_PORT))
        messagebox.showinfo("Connection", "Connected to ESP8266")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to connect: {e}")

# Function to send data to ESP8266
def send_command(command):
    try:
        client_socket.sendall(command.encode())
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send command: {e}")

# Function to close connection to ESP8266
def disconnect_from_esp():
    try:
        client_socket.close()
        messagebox.showinfo("Connection", "Disconnected from ESP8266")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to disconnect: {e}")

# Set up GUI
root = tk.Tk()
root.title("ESP8266 Controller")

ESP_IP = "192.168.1.53"  # Replace with your ESP8266 IP address
ESP_PORT = 80  # Replace with the port your ESP8266 listens on

client_socket = None

# Create buttons for different commands
connect_button = tk.Button(root, text="Connect", command=connect_to_esp)
connect_button.pack(pady=10)

disconnect_button = tk.Button(root, text="Disconnect", command=disconnect_from_esp)
disconnect_button.pack(pady=10)

btn1 = tk.Button(root, text="Command 1", command=lambda: send_command("CMD1"))
btn1.pack(pady=10)

btn2 = tk.Button(root, text="Command 2", command=lambda: send_command("CMD2"))
btn2.pack(pady=10)

btn3 = tk.Button(root, text="Command 3", command=lambda: send_command("CMD3"))
btn3.pack(pady=10)

# Run the GUI event loop
root.mainloop()
