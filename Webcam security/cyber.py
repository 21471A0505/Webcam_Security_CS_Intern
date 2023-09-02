import tkinter as tk
from tkinter import ttk
import subprocess

root = tk.Tk()
password = "12345"  

def button1_clicked():
    password_window = tk.Toplevel(root)
    password_window.title("Enter password")
    password_window.geometry("300x200")
    password_window.configure(bg="white")  # Set background color

    password_label = tk.Label(password_window, text="Enter password:", bg="white")  # Set label background color
    password_label.pack()

    password_entry = tk.Entry(password_window, show="*")
    password_entry.pack()

    def ok_button():
        if password_entry.get() == password:
            file_path = "C:\\Windows\\System32\\cybersecurity\\disable_cam.bat"  # Replace with the actual file path
            with open(file_path, "r") as file:
                  file_content = file.read()

            subprocess.run(["C:\\Windows\\System32\\cybersecurity\\disable_cam.bat"], text=True)
            password_window.destroy()
            success_label.config(text="Camera Disabled successfully")
        else:
            error_label.config(text="Incorrect")
            password_entry.delete(0, tk.END)

    ok_button = ttk.Button(password_window, text="OK", command=ok_button, style="Custom.TButton")  # Apply custom style
    ok_button.pack()

    error_label = tk.Label(password_window, text="", font=("Arial", 12), bg="Red", fg="black")
    error_label.pack()

def button2_clicked():
    password_window = tk.Toplevel(root)
    password_window.title("Enter password")
    password_window.geometry("300x200")
    password_window.configure(bg="white")  # Set background color

    password_label = tk.Label(password_window, text="Enter password:", bg="white")  # Set label background color
    password_label.pack()

    password_entry = tk.Entry(password_window, show="*")
    password_entry.pack()

    def ok_button():
        if password_entry.get() == password:
            subprocess.run([r'enable_cam.bat'], text=True)
            password_window.destroy()
            success_label.config(text="Camera Enabled Successfully")
        else:
            error_label.config(text="Incorrect")
            password_entry.delete(0, tk.END)

    ok_button = ttk.Button(password_window, text="OK", command=ok_button, style="Custom.TButton")  # Apply custom style
    ok_button.pack()
 
    error_label = tk.Label(password_window, text="", font=("Arial", 12), bg="Red", fg="black")
    error_label.pack()

root.title("WEB-CAM SECURITY")
root.geometry("300x200")
root.configure(bg="lightgray")  # Set background color

# Define custom button style
style = ttk.Style()
style.configure("Custom.TButton", font=("Arial", 12), foreground="black", background="white")


enable_button = ttk.Button(root, text="Disable Camera", command=button1_clicked, style="Custom.TButton",  compound="left")  # Apply custom style and add CAM icon
enable_button.pack(pady=10)

disable_button = ttk.Button(root, text="Enable Camera", command=button2_clicked, style="Custom.TButton",  compound="left")  # Apply custom style and add CAM icon
disable_button.pack(pady=10)

success_label = tk.Label(root, text="", bg="lightgray", fg="green")  # Set label background and foreground color
success_label.pack()

root.mainloop()
