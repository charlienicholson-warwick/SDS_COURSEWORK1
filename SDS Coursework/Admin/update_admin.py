import tkinter as tk
import csv
import os
from tkinter import messagebox

# THE ADMIN ID WILL ALWAYS BE ZERO NEVER CHANGE THIS, ALLOWS FOR CONSISTANCY AS ALL OTHER DETAILS CAN NEVER GENERATE TO ZERO THEREFORE NEVER CLASH
# ALLOWS FOR ASSUMED VALUES SPEEDS UP UPDATING AND CHECKING


ADMIN_CREDENTIALS_PATH = os.path.join(os.path.dirname(__file__), '..', 'Data', 'credentials', 'admin_credentials.txt') #*Note* <-- Just in case you forget you wrote the path
#like this because the normal .. /Data/credentials/admin_credentials.txt pathing wasn't working, I don't know why though?? Anyway this should now definatley work on Linux now as well!

def load_admin_credentials(): # Load data FROM the credential path
    with open(ADMIN_CREDENTIALS_PATH, 'r', newline='') as file:
        return next(csv.reader(file))

def save_admin_credentials(admin_details): # Load data TO the credential path
    with open(ADMIN_CREDENTIALS_PATH, 'r', newline='') as file:
        reader = list(csv.reader(file))
    # Update admin details in the list; adminID is assumed to be at index 0
    reader[0] = admin_details 
    with open(ADMIN_CREDENTIALS_PATH, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(reader)

def update_admin_info():
    admin = load_admin_credentials()

    #admin details: [id, username, password, name, status, address]
    labels = ['Username', 'Password', 'Name', 'Address']
    entries = []

    for i, label in enumerate(labels, start=1):
        tk.Label(root, text=label).grid(row=i, column=0)
        entry_var = tk.StringVar(root, value=admin[i])  # Use StringVar for easy get/set
        #https://www.askpython.com/python-modules/tkinter/stringvar-with-examples
        #https://www.geeksforgeeks.org/python-setting-and-retrieving-values-of-tkinter-variable/
        entry = tk.Entry(root, textvariable=entry_var)
        entry.grid(row=i, column=1)
        entries.append(entry_var)
        #https://realpython.com/python-append/

    def on_submit():
        updated_details = [admin[0]] + [entry.get() for entry in entries] + [admin[4]]  # Construct updated admin details, keeping ID and status unchanged
        save_admin_credentials(updated_details) # Save the new updated details
        messagebox.showinfo("Success", "Admin details updated successfully.")
        root.destroy()
    submit_btn = tk.Button(root, text="Submit", command=on_submit)
    submit_btn.grid(row=6, column=0, columnspan=2) # Grid based placing not weird pack <<COULD .pack BE DONE??>> default top placing 2x6 grid, details in 6 (y), old vs new creds in(x)
    #https://www.geeksforgeeks.org/python-grid-method-in-tkinter/

    
root = tk.Tk()
root.title("Update Admin Details")
update_admin_info()
root.mainloop()

