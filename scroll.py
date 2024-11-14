from customtkinter import *
from PIL import Image
from tkinter import ttk, messagebox, filedialog, END
import csv  # Added csv module import

# Assuming `database` module has the required methods
import database  

def open_ems():
    window = CTk()
    window.geometry("1200x650+100+100")
    window.title("Employee Management System")
    
    # Function to handle image upload
    def upload_picture():
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png")])
        if file_path:
            profile_img = CTkImage(Image.open(file_path), size=(150, 150))
            profileImgLabel.configure(image=profile_img)
            profileImgLabel.image = profile_img  # Keep a reference to avoid garbage collection

    # Function to import data from CSV
    def import_from_csv():
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            with open(file_path, "r") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    if not database.id_exists(row[0]):
                        database.insert(*row)
            treeview_data()
            messagebox.showinfo("Import", "Data imported successfully")
        else:
            messagebox.showerror("Error", "Your fields data files do not match this format.")

    # Function to export data to CSV
    def export_to_csv():
        employees = database.fetch_employees()
        with open("employees.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Id", "Name", "Phone", "Role", "Gender", "Salary"])  # Header
            for employee in employees:
                writer.writerow(employee)
        messagebox.showinfo("Export", "Data exported to employees.csv successfully")

    def show_all():
        treeview_data()
        searchEntry.delete(0, END)
        searchBox.set("Search By")

    def delete_all():
        result = messagebox.askyesno("Confirm", "Do you really want to delete all records?")
        if result:
            database.delete_all_records()

    def search_employee():
        if not searchEntry.get():
            messagebox.showerror("Error", "Enter value to search")
        elif searchBox.get() == "Search By":
            messagebox.showerror("Error", "Please select an option")
        else:
            search_data = database.search(searchBox.get(), searchEntry.get())
            tree.delete(*tree.get_children())
            for employee in search_data:
                tree.insert('', END, values=employee)

    def delete_employee():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select data to delete")
        else:
            database.delete(idEntry.get())
            treeview_data()
            clear()
            messagebox.showinfo("Delete", "Data deleted successfully")

    def update_employee():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select data to update")
        else:
            database.update(idEntry.get(), nameEntry.get(), phoneEntry.get(), roleBox.get(), genderBox.get(), salaryEntry.get())
            treeview_data()
            clear()
            messagebox.showinfo("Success", "Data updated successfully")

    def selection(event):
        selected_item = tree.selection()
        if selected_item:
            clear()
            row = tree.item(selected_item)['values']
            idEntry.insert(0, row[0])
            nameEntry.insert(0, row[1])
            phoneEntry.insert(0, row[2])
            roleBox.set(row[3])
            genderBox.set(row[4])
            salaryEntry.insert(0, row[5])

    def treeview_data():
        employees = database.fetch_employees()
        tree.delete(*tree.get_children())
        for employee in employees:
            tree.insert('', END, values=employee)

    def clear(value=False):
        if value:
            tree.selection_remove(tree.focus())
        idEntry.delete(0, END)
        nameEntry.delete(0, END)
        phoneEntry.delete(0, END)
        roleBox.set("Software Engineer")
        genderBox.set("Male")
        salaryEntry.delete(0, END)

    def add_employee():
        if not (idEntry.get() and nameEntry.get() and phoneEntry.get() and salaryEntry.get()):
            messagebox.showerror("Error", "All fields are required")
        elif database.id_exists(idEntry.get()):
            messagebox.showerror("Error", "ID already exists")
        else:
            database.insert(idEntry.get(), nameEntry.get(), phoneEntry.get(), roleBox.get(), genderBox.get(), salaryEntry.get())
            treeview_data()
            clear()
            messagebox.showinfo("Success", "Employee added successfully")

    # Logo image
    try:
        logo = CTkImage(Image.open("aat.jpg"), size=(1077, 200))
    except FileNotFoundError:
        logo = None  # Handle if the image file is not found

    if logo:
        logoLabel = CTkLabel(window, image=logo, text='')
        logoLabel.grid(row=0, column=0, columnspan=2)

    # Left frame for employee details input
    leftFrame = CTkFrame(window)
    leftFrame.grid(row=1, column=0)

    idLabel = CTkLabel(leftFrame, text="Id", font=("Arial", 18, "bold"), padx=20, pady=15)
    idLabel.grid(row=1, column=0, sticky='w')
    idEntry = CTkEntry(leftFrame, font=("Arial", 15, "bold"), width=180)
    idEntry.grid(row=1, column=1)

    nameLabel = CTkLabel(leftFrame, text="Name", font=("Arial", 18, "bold"), padx=20, pady=15)
    nameLabel.grid(row=2, column=0, sticky='w')
    nameEntry = CTkEntry(leftFrame, font=("Arial", 15, "bold"), width=180)
    nameEntry.grid(row=2, column=1)

    phoneLabel = CTkLabel(leftFrame, text="Phone", font=("Arial", 18, "bold"), padx=20, pady=15)
    phoneLabel.grid(row=3, column=0, sticky='w')
    phoneEntry = CTkEntry(leftFrame, font=("Arial", 15, "bold"), width=180)
    phoneEntry.grid(row=3, column=1)

    role_options = ["Software Engineer", "Data Scientist", "UI/UX Designer", "Project Manager", "DevOps Engineer", "Product Manager", "Data Analyst"]
    roleLabel = CTkLabel(leftFrame, text="Role", font=("Arial", 18, "bold"), padx=20, pady=15)
    roleLabel.grid(row=4, column=0, sticky='w')
    roleBox = CTkComboBox(leftFrame, values=role_options, width=180, font=("Arial", 14, "bold"), state="readonly")
    roleBox.grid(row=4, column=1)
    roleBox.set(role_options[0])

    gender_options = ["Male", "Female", "Other"]
    genderLabel = CTkLabel(leftFrame, text="Gender", font=("Arial", 18, "bold"), padx=20, pady=15)
    genderLabel.grid(row=5, column=0, sticky='w')
    genderBox = CTkComboBox(leftFrame, values=gender_options, width=180, font=("Arial", 14, "bold"), state="readonly")
    genderBox.grid(row=5, column=1)
    genderBox.set(gender_options[0])

    salaryLabel = CTkLabel(leftFrame, text="Salary", font=("Arial", 18, "bold"), padx=20, pady=15)
    salaryLabel.grid(row=6, column=0, sticky='w')
    salaryEntry = CTkEntry(leftFrame, font=("Arial", 15, "bold"), width=180)
    salaryEntry.grid(row=6, column=1)

    profileImgLabel = CTkLabel(leftFrame, text="Profile Picture")
    profileImgLabel.grid(row=7, column=0, columnspan=2)
    uploadImgButton = CTkButton(leftFrame, text="Upload Image", command=upload_picture)
    uploadImgButton.grid(row=8, column=0, columnspan=2)

    # Right frame for search and display
    rightFrame = CTkFrame(window)
    rightFrame.grid(row=1, column=1)

    search_options = ["Id", "Name", "Phone", "Role", "Gender", "Salary"]
    searchBox = CTkComboBox(rightFrame, values=search_options, state="readonly")
    searchBox.grid(row=0, column=0)
    searchBox.set("Search By")

    searchEntry = CTkEntry(rightFrame)
    searchEntry.grid(row=0, column=1)
    searchButton = CTkButton(rightFrame, text="Search", cursor="hand2", width=180, command=search_employee)
    searchButton.grid(row=0, column=2)
    showAllButton = CTkButton(rightFrame, text="Show All", cursor="hand2", width=180, command=show_all)
    showAllButton.grid(row=0, column=3)

    # Treeview for displaying data
    tree = ttk.Treeview(rightFrame, height=11)
    tree.grid(row=1, column=0, columnspan=4)
    tree["columns"] = ("Id", "Name", "Phone", "Role", "Gender", "Salary")
    for col in tree["columns"]:
        tree.column(col, width=150)
        tree.heading(col, text=col)
    tree.config(show="headings")

    # Add scrollbar to the Treeview
    scrollbar = ttk.Scrollbar(rightFrame, orient="vertical")
    scrollbar.grid(row=1, column=4, sticky="ns")
    tree.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=tree.yview)

    # Button Frame
    buttonFrame = CTkFrame(window)
    buttonFrame.grid(row=2, column=0, columnspan=2)
    newButton = CTkButton(buttonFrame, text="New Employee", cursor="hand2", font=("Arial", 15, "bold"),
                          width=160, corner_radius=15, command=lambda: clear(True))
    newButton.grid(row=0, column=0, pady=5, padx=5)
    addButton = CTkButton(buttonFrame, text="Add Employee", cursor="hand2", font=("Arial", 15, "bold"),
                          width=160, corner_radius=15, command=add_employee)
    addButton.grid(row=0, column=1, pady=5, padx=5)
    updateButton = CTkButton(buttonFrame, text="Update Employee", cursor="hand2", font=("Arial", 15, "bold"),
                             width=160, corner_radius=15, command=update_employee)
    updateButton.grid(row=0, column=2, pady=5, padx=5)
    deleteButton = CTkButton(buttonFrame, text="Delete Employee", cursor="hand2", font=("Arial", 15, "bold"),
                             width=160, corner_radius=15, command=delete_employee)
    deleteButton.grid(row=0, column=3, pady=5, padx=5)
    deleteAllButton = CTkButton(buttonFrame, text="Delete All Employees", cursor="hand2", font=("Arial", 15, "bold"),
                                width=160, corner_radius=15, command=delete_all)
    deleteAllButton.grid(row=0, column=4, pady=5, padx=5)

    exportButton = CTkButton(buttonFrame, text="Export CSV", cursor="hand2", font=("Arial", 15, "bold"),
                             width=160, corner_radius=15, command=export_to_csv)
    exportButton.grid(row=0, column=5, pady=5, padx=5)
    importButton = CTkButton(buttonFrame, text="Import CSV", cursor="hand2", font=("Arial", 15, "bold"),
                             width=160, corner_radius=15, command=import_from_csv)
    importButton.grid(row=0, column=6, pady=5, padx=5)

    window.mainloop()

open_ems()
