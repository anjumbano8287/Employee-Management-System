import os
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import sqlite3
import tkinter as tk
from customtkinter import *

# Function to open file dialog and add profile picture
def add_profile_picture():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if file_path:
        try:
            # Open the image
            img = Image.open(file_path)
            img = img.resize((100, 100))  # Resize to fit in the GUI

            # Convert image to Tkinter-compatible format
            photo = ImageTk.PhotoImage(img)

            # Display the image in a Label
            profile_picture_label.config(image=photo)
            profile_picture_label.image = photo  # Keep a reference to avoid garbage collection

            # Save the file path to the database (this example assumes you store the path in the database)
            # You can adjust it based on your table structure
            database.update_profile_picture(idEntry.get(), file_path)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {e}")

# Function to fetch and display profile picture from the database
def display_profile_picture(employee_id):
    image_path = database.fetch_profile_picture(employee_id)
    if image_path:
        try:
            img = Image.open(image_path)
            img = img.resize((100, 100))  # Resize to fit in the GUI
            photo = ImageTk.PhotoImage(img)

            # Display the image in the Label
            profile_picture_label.config(image=photo)
            profile_picture_label.image = photo  # Keep a reference to avoid garbage collection
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {e}")
    else:
        profile_picture_label.config(image=None)
        profile_picture_label.image = None

# Update database function to save image path
def update_profile_picture(employee_id, image_path):
    conn = sqlite3.connect('employee.db')  # Replace with your actual database path
    cursor = conn.cursor()
    cursor.execute("UPDATE employees SET profile_picture = ? WHERE id = ?", (image_path, employee_id))
    conn.commit()
    conn.close()

# Function to fetch profile picture path from database
def fetch_profile_picture(employee_id):
    conn = sqlite3.connect('employee.db')  # Replace with your actual database path
    cursor = conn.cursor()
    cursor.execute("SELECT profile_picture FROM employees WHERE id = ?", (employee_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# GUI Setup
window = CTk()

# Example employee ID entry
idEntry = CTkEntry(window, font=("Arial", 15), width=180)
idEntry.grid(row=0, column=1)

# Label to display the profile picture
profile_picture_label = CTkLabel(window, text="No Profile Picture", width=100, height=100)
profile_picture_label.grid(row=1, column=1)

# Button to add profile picture
add_picture_button = CTkButton(window, text="Add Profile Picture", command=add_profile_picture)
add_picture_button.grid(row=2, column=1)

# Example function to load profile picture when an employee is selected
def load_employee_profile(employee_id):
    display_profile_picture(employee_id)

window.mainloop()
