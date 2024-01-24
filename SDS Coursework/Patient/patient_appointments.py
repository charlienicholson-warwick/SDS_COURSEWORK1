import tkinter as tk
import csv
import sys

def load_appointments(patient_id): # Takes patient ID
    appointments = [] # Empty appointment ID <-- Classic empty list override should be familiar by now
    with open('../Data/appointments/appointments.txt', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == patient_id: # If appointment is for our patient...
                appointments.append(row) # Add it to the list
    return appointments

def display_appointments(appointments):
    for app in appointments:
        app_info = f"Condition: {app[1]}, Date: {app[3]} , Status: {app[4]} , Assigned Doctor: {app[5]}" 
        tk.Label(frame, text=app_info).pack()

patient_id = sys.argv[1] if len(sys.argv) > 1 else "Unknown" # Gets ID from console just like in the main patient.py same main commenting as over there except here returns error not a sys exit

app = tk.Tk()
app.title(f"Patient {patient_id} - Appointments")

frame = tk.Frame(app)
frame.pack(pady=10)

appointments = load_appointments(patient_id)
display_appointments(appointments)

app.mainloop()
