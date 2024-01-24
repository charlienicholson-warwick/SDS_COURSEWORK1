import tkinter as tk
from tkinter import simpledialog, messagebox
import csv
import os #inter os functionality

appointments_path = os.path.join(os.path.dirname(__file__), '..', 'Data', 'appointments', 'appointments.txt') #inter os pathing for text file

def load_appointments():
    with open(appointments_path, 'r', newline='') as file:
        return list(csv.reader(file))

def save_appointments(appointments):
    with open(appointments_path, 'w', newline='') as file:
        csv.writer(file).writerows(appointments)

def update_appointment(index, action, doctor_id=None):
    appointments = load_appointments()
    if action == "approve":
        appointments[index][4] = "Approved"  # Update status
        if doctor_id:
            appointments[index][5] = doctor_id
    elif action == "reject":
        # Remove the appointment from the list entirely
        appointments.pop(index)
    
    save_appointments(appointments)
    display_pending_appointments()  # Refresh the display


def display_pending_appointments():
    for widget in root.winfo_children(): #more documentation info in manage_applications.py
        widget.destroy() #destroy declined/approved widgets

    appointments = [app for app in load_appointments() if app[4] != "Approved"]  # Show non-approved
    for idx, app in enumerate(appointments):
        app_info = f"Patient ID: {app[0]}, Symptom: {app[1]}, Type: {app[2]}, Date: {app[3]}, Status: {app[4]}, Doctor ID: {app[5]}"
        label = tk.Label(root, text=app_info)
        label.pack()

        if app[4] != "Approved":  # Only show buttons for pending appointments
            #<<TODO: Becuase you are a complete muppet you have used different terminology througout the program sometimes its called "Pending" sometimes called "Requested">>
            #<<Check through the code an ensure syntactical consistancy for now just using NOT approved is sufficient>>
            
            assign_button = tk.Button(root, text="Assign Doctor", command=lambda idx=idx, app=app: assign_doctor(idx, app))
            assign_button.pack() #button uses lambda to pass back specific data to callback in this case we pass the index and the app

            approve_button = tk.Button(root, text="Approve", command=lambda idx=idx: update_appointment(idx, "approve"))
            approve_button.pack() #button uses lamda to pass back the index as well as the approve text

            reject_button = tk.Button(root, text="Reject", command=lambda idx=idx: update_appointment(idx, "reject"))
            reject_button.pack() #same as above but with reject text

            #idx is indexing function within tkinter 
            #https://tkdocs.com/tutorial/text.html
            #https://www.tutorialspoint.com/tkinter-button-commands-with-lambda-in-python

def assign_doctor(index, appointment):
    doctor_id = simpledialog.askstring("Assign Doctor", "Enter Doctor ID:")
    if doctor_id:
        update_appointment(index, "approve", doctor_id)  # Directly approve with doctor assignment
        messagebox.showinfo("Updated", f"Doctor ID {doctor_id} assigned to the appointment.")



root = tk.Tk()
root.title("Manage Appointments")
display_pending_appointments()
root.mainloop()
