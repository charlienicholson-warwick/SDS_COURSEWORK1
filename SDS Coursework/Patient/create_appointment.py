import tkinter as tk
import tkinter.simpledialog as sd
import csv
import os
import sys
    
def save_appointment(patient_id, condition, condition_type, appointment_date, status="Requested", doctor_id="TBD"):
    # ^^Obviously no doctor yet so doctor_id="TBD" and not approved yet by the admin so status="Requested"
    appointments_path = '../Data/appointments/appointments.txt' # Appointments_path links to the appointment.txt
    with open(appointments_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([patient_id, condition, condition_type, appointment_date, status, doctor_id])
        # Save appointments to the /Data/appointments/applications.txt

def create_appointment(patient_id): # Create the appointment
    condition = sd.askstring("New Appointment", "Enter the condition for the appointment:")
    if condition:
        condition_type = sd.askstring("New Appointment", "Is the condition physical or viral?")
        if condition_type.lower() not in ['physical', 'viral']: #Can't decide how to do the different types of conditions in the managment report
            # So I basically just made the types of illnesses into basically just a binary to make my life easier
            tk.messagebox.showwarning("Invalid Input", "Please enter 'physical' or 'viral' for the condition type.")
            return
        appointment_date = sd.askstring("New Appointment", "Enter the date for the appointment (DD/MM/YY):")
        save_appointment(patient_id, condition, condition_type, appointment_date)
        tk.messagebox.showinfo("Success", "Appointment created successfully.")
    else:
        tk.messagebox.showwarning("Cancelled", "Appointment creation cancelled.")


app = tk.Tk()
app.withdraw()

if len(sys.argv) > 1:       #Classic piece of code, passes the patientID from the patient.py script
    patient_id = sys.argv[1]
    create_appointment(patient_id)
else:
    tk.messagebox.showerror("Error", "No patient ID provided.") 
