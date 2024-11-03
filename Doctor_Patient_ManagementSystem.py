import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Doctor-Patient Application")

# Function to add patient information
def add_patient():
    patient_name = name_entry.get()
    patient_age = age_entry.get()
    patient_condition = condition_entry.get()
    
    if not patient_name or not patient_age or not patient_condition:
        messagebox.showerror("Input Error", "All fields must be filled out")
        return
    
    patient_info = f"Name: {patient_name}\nAge: {patient_age}\nCondition: {patient_condition}"
    patients_listbox.insert(tk.END, patient_info)
    
    # Clear input fields
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    condition_entry.delete(0, tk.END)



# Create frames for layout
input_frame = tk.Frame(root)
input_frame.pack(padx=10, pady=10)

list_frame = tk.Frame(root)
list_frame.pack(padx=10, pady=10)

# Labels and Entries for patient information
tk.Label(input_frame, text="Patient Name:").grid(row=0, column=0, sticky=tk.W)
name_entry = tk.Entry(input_frame, width=30)
name_entry.grid(row=0, column=1)

tk.Label(input_frame, text="Age:").grid(row=1, column=0, sticky=tk.W)
age_entry = tk.Entry(input_frame, width=30)
age_entry.grid(row=1, column=1)

tk.Label(input_frame, text="Condition:").grid(row=2, column=0, sticky=tk.W)
condition_entry = tk.Entry(input_frame, width=30)
condition_entry.grid(row=2, column=1)

# Button to add patient information
add_button = tk.Button(input_frame, text="Add Patient", command=add_patient)
add_button.grid(row=3, column=0, columnspan=2, pady=5)

# Listbox to display patient information
patients_listbox = tk.Listbox(list_frame, width=50, height=10)
patients_listbox.pack()

# Run the application
root.mainloop()
