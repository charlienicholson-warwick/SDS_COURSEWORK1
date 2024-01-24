import tkinter as tk
import csv
import sys

def get_patient_info(patient_id):
    with open('../Data/credentials/patient_credentials.txt', 'r') as file: #read from cred file
        reader = csv.reader(file)
        for row in reader:
            print(f"Row read: {row}")  # Debuggin'
            if row[0].strip() == patient_id.strip(): #if for our patient...
                return row #return thier credentials
    return None

patient_id = sys.argv[1] if len(sys.argv) > 1 else "Unknown" # Absolute classic. Truly a profound line of code, I wonder what it does???
patient_info = get_patient_info(patient_id) # fetchest the patient info from our get_patient_info function

app = tk.Tk()
app.title(f"Patient {patient_id} - Information")

if patient_info:
    tk.Label(app, text=f"Full Name: {patient_info[3]}").pack()
    tk.Label(app, text=f"Age: {patient_info[5]}").pack()
    tk.Label(app, text=f"Mobile: {patient_info[6]}").pack()
    tk.Label(app, text=f"Address: {patient_info[7]}").pack()
    # Presents all patient information except sensitive data e.g. uname & pswd done via default Top sorting .pack Label widgets
else:
    tk.Label(app, text="Patient information not found.").pack()
    # If no patient information has been found... fairly obvious

app.mainloop()
