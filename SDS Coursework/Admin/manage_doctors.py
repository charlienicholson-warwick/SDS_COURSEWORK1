import tkinter as tk
from tkinter import simpledialog, messagebox
import csv
import random


def load_doctors():
    doctors = [] # Blank for writing to for overwriting, the same functionality as in managing applicaitions
    with open('../Data/credentials/doctor_credentials.txt', 'r') as file: #TODO: CHECK OS FUNCTIONALITY VS LINUX
        # No needed error handling as creds file will always exist, hard baked into /Data/Credentials
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 4:  # Data has the format (ID, username, password, name)
                doctors.append(row) # Add to the doctors list (previously blank)
            else:
                print(f"Skipping malformed line: {row}") # *Note* <-- This is needed as sometimes fomatting of doctor creds gets screwed up and becomes unusable
    return doctors # Return the list of doctors now from the csv is in the data called 'doctors'

def update_doctors(doctors):
    try:
        with open('../Data/credentials/doctor_credentials.txt', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(doctors) #write updated doctor to file
    except Exception as e: #broad error handling
        print(f"Error updating doctors: {e}")

def display_doctors():
    for widget in frame_doctors.winfo_children(): # When you remove a doctor you need a way to update the list to make them dissapear & when you update creds
        widget.destroy() # Destroy the old widget and allow for regeneration

    doctors = load_doctors() # Reload doctors
    if not doctors:
        tk.Label(frame_doctors, text="No doctors currently registered").pack()
    else:
        for doctor in doctors:
            doctor_info = ', '.join(doctor)
            tk.Label(frame_doctors, text=doctor_info).pack()
            update_btn = tk.Button(frame_doctors, text="Update", command=lambda id=doctor[0]: update_doctor(id, doctor)) #call Update passing id we want to update and doctor values to write in the values
            update_btn.pack()
            remove_btn = tk.Button(frame_doctors, text="Remove", command=lambda id=doctor[0]: remove_doctor(id)) #call remove passing the id we want to remove
            remove_btn.pack()

def update_doctor(doctor_id, doctor_data):
    new_username = simpledialog.askstring("Update Doctor", "Enter doctor's new username:", initialvalue=doctor_data[1])
    new_password = simpledialog.askstring("Update Doctor", "Enter doctor's new password:", initialvalue=doctor_data[2])
    new_name = simpledialog.askstring("Update Doctor", "Enter doctor's new full name:", initialvalue=doctor_data[3])

    if new_username and new_password and new_name:
        doctors = load_doctors()
        for doctor in doctors:
            if doctor[0] == doctor_id:
                doctor[1] = new_username
                doctor[2] = new_password
                doctor[3] = new_name
                break
        update_doctors(doctors)
        display_doctors()
        #FAIRLY OBV FUNCTION NO NEED FOR DETAILED COMMENTING


def remove_doctor(doctor_id):
    doctors = load_doctors() # Load all doctors
    doctors = [doc for doc in doctors if doc[0] != doctor_id] # Change doctors to all doctors that aren't the one we want to remove
    update_doctors(doctors) # Update the doctors, therefore new doctors are all the old ones that we didn't want to remove
    display_doctors() # Regens the doctors therefore effectivley removing the doctor we wanted 

def register_doctor():
    new_id = str(random.randint(1, 99999))  # Randomly generate a doctorID
    new_username = simpledialog.askstring("Register Doctor", "Enter new doctor username:")
    new_password = simpledialog.askstring("Register Doctor", "Enter new doctor password:")
    new_name = simpledialog.askstring("Register Doctor", "Enter new doctor full name:")
    if new_username and new_password and new_name:
        doctors = load_doctors()
        while new_id in [doctor[0] for doctor in doctors]:
            new_id = str(random.randint(1, 99999))
        doctors.append([new_id, new_username, new_password, new_name])
        update_doctors(doctors)
        display_doctors()

app = tk.Tk()
app.title("Manage Doctors")

frame_doctors = tk.Frame(app)
frame_doctors.pack(pady=10)

display_doctors()

register_btn = tk.Button(app, text="Register New Doctor", command=register_doctor)
register_btn.pack()

app.mainloop()



