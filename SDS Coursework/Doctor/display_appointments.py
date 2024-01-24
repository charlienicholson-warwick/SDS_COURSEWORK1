import tkinter as tk
import csv
import os
import sys


# This file is takes code from two /Admin scripts manage_doctors.py and discharge_patient.py the rough functionality with blank list overrides are consistant througout,
# ^^^ For marker: I did this on purpose to allow for consistancy and increase accuracy whilst coding as all data is consistantly treated in only a few ways corruption and malformation is limited

def load_appointments(doctor_id):
    appointments = []
    with open('../Data/appointments/appointments.txt', 'r') as file:
        reader = csv.reader(file)
        # Now considering the status field for filtering
        for row in reader:
            # Check if the appointment is for this doctor and is approved
            if row[5] == doctor_id and row[4].lower() == 'approved':
                appointments.append(row) #if it is then display it by appending to the blank appointment row
    return appointments

def mark_as_completed(doctor_id, appointment_to_remove):
    appointments = load_appointments(doctor_id)
    appointments = [app for app in appointments if not (app[0] == appointment_to_remove[0] and app[3] == appointment_to_remove[3])]  # Remove by matching PatientID and Date
    save_appointments(appointments) # Re-save the now cleared appointment
    #<<TODO: ADD A WIDGET CLEAR FOR PREVIOUS INFORMATION??>>
    display_appointments(doctor_id) # Re-display the now cleared appointment

def save_appointments(appointments): #This has been added later to hopefully fix the program, this is why I use os.path here and not further up the program
    appointments_path = os.path.join(os.path.dirname(__file__), '..', 'Data', 'appointments', 'appointments.txt')
    with open(appointments_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(appointments)

def display_appointments(doctor_id):
    appointments = load_appointments(doctor_id)
    if not appointments:
        label = tk.Label(root, text="No current approved appointments")
        label.pack()
    else:
        for app in appointments:
            # Structure: [PatientID, Condition, Physical/Viral?, Date, Status, DoctorID]
            # For marker: This will be expanded with an explanation for each field in the patient section
            appointment_info = f"Patient ID: {app[0]}, Condition: {app[1]}, Type: {app[2]}, Date: {app[3]}"
            label = tk.Label(root, text=appointment_info)
            label.pack()
            complete_btn = tk.Button(root, text="Mark as Completed", command=lambda app=app: mark_as_completed(doctor_id, app))
            complete_btn.pack()

doctor_id = sys.argv[1] if len(sys.argv) > 1 else "Unknown"
#^For Marker: For detailed explanation of this line please read either doctor.py or admin.py
print(doctor_id) #DEBUGGIN'
root = tk.Tk()
root.title(f"Doctor {doctor_id} - Approved Appointments")
display_appointments(doctor_id)
root.mainloop()
