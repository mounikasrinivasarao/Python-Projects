import tkinter as tk
from tkinter import filedialog, messagebox
import os
import json
import utils
import customtkinter

APP_ICON = os.path.join(os.path.dirname(__file__), "icon.ico")

def popup_invalid_length():
    title = "Invalid Input"
    message = "Password length must be\nbetween 8 and 64."
    root = customtkinter.CTkToplevel()
    root.geometry("250x120")
    root.resizable(width=False, height=False)
    root.title(title)
    root.iconbitmap(APP_ICON)
    # Background frame
    background_frame = customtkinter.CTkFrame(root, width=1000, height=1000, bg_color="#111111", fg_color="#111111")
    background_frame.grid(row=0, column=0, rowspan=1, sticky="nsew")
    background_frame.grid_rowconfigure(index=2, weight=1)
    background_frame.place(x=0, y=0)
    label = customtkinter.CTkLabel(root, text=message, font=("Arial", 12), text_color="red", bg_color="#111111")
    label.pack(padx=20, pady=20)
    ok_button = customtkinter.CTkButton(root, text="OK", command=root.destroy, hover_color="#3D0000", bg_color="#111111", fg_color="#950101")
    ok_button.pack(padx=0, pady=0)
    root.grab_set()

def popup_no_length():
    title = "Invalid Input"
    message = "Please enter a password length."
    root = customtkinter.CTkToplevel()
    root.geometry("250x120")
    root.resizable(width=False, height=False)
    root.title(title)
    root.iconbitmap(APP_ICON)
    # Background frame
    background_frame = customtkinter.CTkFrame(root, width=1000, height=1000, bg_color="#111111", fg_color="#111111")
    background_frame.grid(row=0, column=0, rowspan=1, sticky="nsew")
    background_frame.grid_rowconfigure(index=2, weight=1)
    background_frame.place(x=0, y=0)
    label = customtkinter.CTkLabel(root, text=message, font=("Arial", 12), text_color="red", bg_color="#111111")
    label.pack(padx=20, pady=20)
    ok_button = customtkinter.CTkButton(root, text="OK", command=root.destroy, hover_color="#3D0000", bg_color="#111111", fg_color="#950101")
    ok_button.pack(padx=0, pady=0)
    root.grab_set()

def popup_password_length():
    title = "Invalid Input"
    message = "Password length must be\nbetween 8 and 64."
    root = customtkinter.CTkToplevel()
    root.geometry("250x120")
    root.resizable(width=False, height=False)
    root.title(title)
    root.iconbitmap(APP_ICON)
    # Background frame
    background_frame = customtkinter.CTkFrame(root, width=1000, height=1000, bg_color="#111111", fg_color="#111111")
    background_frame.grid(row=0, column=0, rowspan=1, sticky="nsew")
    background_frame.grid_rowconfigure(index=2, weight=1)
    background_frame.place(x=0, y=0)
    label = customtkinter.CTkLabel(root, text=message, font=("Arial", 12), text_color="red", bg_color="#111111")
    label.pack(padx=20, pady=20)
    ok_button = customtkinter.CTkButton(root, text="OK", command=root.destroy, hover_color="#3D0000", bg_color="#111111", fg_color="#950101")
    ok_button.pack(padx=0, pady=0)
    root.grab_set()

def popup_invalid_num_passwords():
    title = "Invalid Input"
    message = "Number of passwords must be\nbetween 1 and 4294967295."
    root = customtkinter.CTkToplevel()
    root.geometry("250x120")
    root.resizable(width=False, height=False)
    root.title(title)
    root.iconbitmap(APP_ICON)
    # Background frame
    background_frame = customtkinter.CTkFrame(root, width=1000, height=1000, bg_color="#111111", fg_color="#111111")
    background_frame.grid(row=0, column=0, rowspan=1, sticky="nsew")
    background_frame.grid_rowconfigure(index=2, weight=1)
    background_frame.place(x=0, y=0)
    label = customtkinter.CTkLabel(root, text=message, font=("Arial", 12), text_color="red", bg_color="#111111")
    label.pack(padx=20, pady=10)
    ok_button = customtkinter.CTkButton(root, text="OK", command=root.destroy, hover_color="#3D0000", bg_color="#111111", fg_color="#950101")
    ok_button.pack(padx=0, pady=0)
    root.grab_set()

def popup_no_num_passwords():
    title = "Invalid Input"
    message = "Number of passwords must be\nbetween 1 and 4294967295."
    root = customtkinter.CTkToplevel()
    root.geometry("250x120")
    root.resizable(width=False, height=False)
    root.title(title)
    root.iconbitmap(APP_ICON)
    # Background frame
    background_frame = customtkinter.CTkFrame(root, width=1000, height=1000, bg_color="#111111", fg_color="#111111")
    background_frame.grid(row=0, column=0, rowspan=1, sticky="nsew")
    background_frame.grid_rowconfigure(index=2, weight=1)
    background_frame.place(x=0, y=0)
    label = customtkinter.CTkLabel(root, text=message, font=("Arial", 12), text_color="red", bg_color="#111111")
    label.pack(padx=20, pady=20)
    ok_button = customtkinter.CTkButton(root, text="OK", command=root.destroy, hover_color="#3D0000", bg_color="#111111", fg_color="#950101")
    ok_button.pack(padx=0, pady=0)
    root.grab_set()

def popup_settings_saved():
    title = "Settings Saved"
    message = "Settings have been\nsaved successfully."
    root = customtkinter.CTkToplevel()
    root.geometry("250x120")
    root.resizable(width=False, height=False)
    root.title(title)
    root.iconbitmap(APP_ICON)
    # Background frame
    background_frame = customtkinter.CTkFrame(root, width=1000, height=1000, bg_color="#111111", fg_color="#111111")
    background_frame.grid(row=0, column=0, rowspan=1, sticky="nsew")
    background_frame.grid_rowconfigure(index=2, weight=1)
    background_frame.place(x=0, y=0)
    font = customtkinter.CTkFont(family="Arial", size=12, weight="bold")
    label = customtkinter.CTkLabel(root, text=message, font=font, text_color="green", bg_color="#111111")
    label.pack(padx=20, pady=20)
    ok_button = customtkinter.CTkButton(root, text="OK", command=root.destroy, font=font, hover_color="#3D0000", bg_color="#111111", fg_color="#950101")
    ok_button.pack(padx=0, pady=0)
    root.grab_set()

def popup_passwords_generated(num_passwords, file_path):
    title = "Passwords Generated"
    message = f"{num_passwords} passwords\nhave been generated and saved to\n{file_path}"
    root = customtkinter.CTkToplevel()
    root.geometry("400x140")
    root.resizable(width=False, height=False)
    root.title(title)
    root.iconbitmap(APP_ICON)
    # Background frame
    background_frame = customtkinter.CTkFrame(root, width=1000, height=1000, bg_color="#111111", fg_color="#111111")
    background_frame.grid(row=0, column=0, rowspan=1, sticky="nsew")
    background_frame.grid_rowconfigure(index=2, weight=1)
    background_frame.place(x=0, y=0)
    font = customtkinter.CTkFont(family="Arial", size=12, weight="bold")
    label = customtkinter.CTkLabel(root, text=message, font=font, text_color="green", bg_color="#111111")
    label.pack(padx=20, pady=20)
    ok_button = customtkinter.CTkButton(root, text="OK", command=root.destroy, font=font, hover_color="#3D0000", bg_color="#111111", fg_color="#950101")
    ok_button.pack(padx=0, pady=0)
    root.grab_set()

def get_default_save_directory():
    return os.path.join(os.path.expanduser("~"), "Documents", "PasswordGenerator")

def generate_passwords(length, num_passwords, output_file):
    if not os.path.exists(os.path.dirname(output_file)):
        os.makedirs(os.path.dirname(output_file))
    
    passwords = utils.generate_passwords(length, num_passwords)
    with open(output_file, "w") as f:
        for password in passwords:
            f.write(password + "\n")
    return num_passwords, output_file

class PasswordGeneratorGUI:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry("400x300")
        self.root.resizable(width=False, height=False)
        self.root.title("Password Generator")
        self.root.iconbitmap(APP_ICON)

        self.length_label = customtkinter.CTkLabel(self.root, text="Password Length:", bg_color="#111111", text_color="white")
        self.length_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.length_entry = customtkinter.CTkEntry(self.root, width=200, bg_color="#111111", fg_color="#333333", text_color="white")
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        self.num_passwords_label = customtkinter.CTkLabel(self.root, text="Number of Passwords:", bg_color="#111111", text_color="white")
        self.num_passwords_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.num_passwords_entry = customtkinter.CTkEntry(self.root, width=200, bg_color="#111111", fg_color="#333333", text_color="white")
        self.num_passwords_entry.grid(row=1, column=1, padx=10, pady=10)

        self.output_file_label = customtkinter.CTkLabel(self.root, text="Output File:", bg_color="#111111", text_color="white")
        self.output_file_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.output_file_entry = customtkinter.CTkEntry(self.root, width=200, bg_color="#111111", fg_color="#333333", text_color="white")
        self.output_file_entry.grid(row=2, column=1, padx=10, pady=10)
        self.output_file_button = customtkinter.CTkButton(self.root, text="Browse", command=self.browse_file, hover_color="#3D0000", bg_color="#111111", fg_color="#950101")
        self.output_file_button.grid(row=2, column=2, padx=10, pady=10)

        self.generate_button = customtkinter.CTkButton(self.root, text="Generate Passwords", command=self.generate_passwords, hover_color="#3D0000", bg_color="#111111", fg_color="#950101")
        self.generate_button.grid(row=3, column=1, padx=10, pady=20)

    def browse_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            self.output_file_entry.delete(0, tk.END)
            self.output_file_entry.insert(0, file_path)

    def generate_passwords(self):
        try:
            length = int(self.length_entry.get())
            if length < 8 or length > 64:
                popup_password_length()
                return
        except ValueError:
            popup_no_length()
            return

        try:
            num_passwords = int(self.num_passwords_entry.get())
            if num_passwords < 1 or num_passwords > 4294967295:
                popup_invalid_num_passwords()
                return
        except ValueError:
            popup_no_num_passwords()
            return

        output_file = self.output_file_entry.get().strip()
        if not output_file:
            output_file = os.path.join(get_default_save_directory(), "passwords.txt")

        num_passwords, file_path = generate_passwords(length, num_passwords, output_file)
        popup_passwords_generated(num_passwords, file_path)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = PasswordGeneratorGUI()
    gui.run()
