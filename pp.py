from customtkinter import *
from PIL import Image
from tkinter import ttk

# Initialize the main window
window = CTk()
window.geometry("1077x560")
window.resizable(1, 1)  # Enable resizing
window.title("Employee Management System")

# Configure row and column expansion
window.grid_rowconfigure(1, weight=1)  # Row 1 (where leftFrame and rightFrame are) will expand
window.grid_columnconfigure(1, weight=1)  # Column 1 (where rightFrame is) will expand

# Image at the top of the page
logo = CTkImage(Image.open("aat.jpg"), size=(1077, 200))
logoLabel = CTkLabel(window, image=logo, text='')
logoLabel.grid(row=0, column=0, columnspan=2)

# Left frame for details input
leftFrame = CTkFrame(window)
leftFrame.grid(row=1, column=0, padx=15, pady=15, sticky="ns")

# Id label and entry
idLabel = CTkLabel(leftFrame, text="Id", font=("Arial", 18, "bold"), padx=20, pady=15)
idLabel.grid(row=1, column=0, sticky='w')
idEntry = CTkEntry(leftFrame, font=("Arial", 15, "bold"), width=180)
idEntry.grid(row=1, column=1)

# Name label and entry
nameLabel = CTkLabel(leftFrame, text="Name", font=("Arial", 18, "bold"), padx=20, pady=15)
nameLabel.grid(row=2, column=0, sticky='w')
nameEntry = CTkEntry(leftFrame, font=("Arial", 15, "bold"), width=180)
nameEntry.grid(row=2, column=1)

# Phone label and entry
phoneLabel = CTkLabel(leftFrame, text="Phone", font=("Arial", 18, "bold"), padx=20, pady=15)
phoneLabel.grid(row=3, column=0, sticky='w')
phoneEntry = CTkEntry(leftFrame, font=("Arial", 15, "bold"), width=180)
phoneEntry.grid(row=3, column=1)

# Role label and dropdown
roleLabel = CTkLabel(leftFrame, text="Role", font=("Arial", 18, "bold"), padx=20, pady=15)
roleLabel.grid(row=4, column=0, sticky='w')
role_options = [
    "Software Engineer", "Data Scientist", "UI/UX Designer",
    "Project Manager", "DevOps Engineer", "Product Manager", "Data Analyst"
]
roleBox = CTkComboBox(leftFrame, values=role_options, width=180, font=("Arial", 14, "bold"), state="readonly")
roleBox.grid(row=4, column=1)
roleBox.set(role_options[0])

# Gender label and dropdown
genderLabel = CTkLabel(leftFrame, text="Gender", font=("Arial", 18, "bold"), padx=20, pady=15)
genderLabel.grid(row=5, column=0, sticky='w')
gender_options = ["Male", "Female", "Other"]
genderBox = CTkComboBox(leftFrame, values=gender_options, width=180, font=("Arial", 14, "bold"), state="readonly")
genderBox.grid(row=5, column=1)
genderBox.set(gender_options[0])

# Salary label and entry in leftFrame
salaryLabel = CTkLabel(leftFrame, text="Salary", font=("Arial", 18, "bold"), padx=20, pady=15)
salaryLabel.grid(row=6, column=0, sticky='w')
salaryEntry = CTkEntry(leftFrame, font=("Arial", 15, "bold"), width=180)
salaryEntry.grid(row=6, column=1, padx=5, pady=5)

# Right frame for search functionality and table display
rightFrame = CTkFrame(window)
rightFrame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")  # Sticky set to all sides for expanding

# Configure rightFrame to expand with window resizing
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(1, weight=1)

# Search dropdown and entry
search_options = ["Id", "Name", "Phone", "Role", "Gender", "Salary"]
searchBox = CTkComboBox(rightFrame, values=search_options, state="readonly", width=120)
searchBox.grid(row=0, column=0, padx=5, pady=5)
searchBox.set("Search By")

searchEntry = CTkEntry(rightFrame, font=("Arial", 15, "bold"), width=180)
searchEntry.grid(row=0, column=1, padx=5, pady=5)

# Search and Show All buttons
searchButton = CTkButton(rightFrame, text="Search", cursor="hand2", width=90)
searchButton.grid(row=0, column=2, padx=5, pady=5)
showAllButton = CTkButton(rightFrame, text="Show All", cursor="hand2", width=90)
showAllButton.grid(row=0, column=3, padx=5, pady=5)

# Table to display employee data
tree = ttk.Treeview(rightFrame, columns=("Id", "Name", "Phone", "Role", "Gender", "Salary"), show="headings", height=11)
tree.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

# Define column headings
tree.heading("Id", text="Id")
tree.heading("Name", text="Name")
tree.heading("Phone", text="Phone")
tree.heading("Role", text="Role")
tree.heading("Gender", text="Gender")
tree.heading("Salary", text="Salary")

# Start the main loop
window.mainloop()
