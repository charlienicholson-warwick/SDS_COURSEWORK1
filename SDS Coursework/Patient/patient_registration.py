import tkinter as tk
import tkinter.simpledialog as sd
import csv
import random

def register_patient(username, password, full_name, age, mobile, address): #here shows all the features saved in the patient [username, password, full_name, age, mobile, address]
    # Randomly generate a patient ID
    patient_id = str(random.randint(1, 1000000)) # Random gen for our patientID
    
    credentials_path = '../Data/credentials/patient_credentials.txt'
    with open(credentials_path, 'a', newline='') as file:
        writer = csv.writer(file) # Write to patient_credentials file
        writer.writerow([patient_id, username, password, full_name, 'Pending', age, mobile, address]) # *Note* <-- Set status to pending by default till approved by admin

    tk.messagebox.showinfo("Registration Successful", f"You are registered. Your patient ID is {patient_id}")

def prompt_registration(): # Obvious no annotation needed
    username = sd.askstring("Registration", "Enter your username:")
    if not username:
        return
    password = sd.askstring("Registration", "Enter your password:")
    if not password:
        return
    full_name = sd.askstring("Registration", "Enter your full name:")
    if not full_name:
        return
    age = sd.askstring("Registration", "Enter your age:")
    if not age:
        return
    mobile = sd.askstring("Registration", "Enter your mobile number:")
    if not mobile:
        return
    address = sd.askstring("Registration", "Enter your address:")
    if not address:
        return

    register_patient(username, password, full_name, age, mobile, address) # Call the register patient function

app = tk.Tk()
app.withdraw()

prompt_registration()
