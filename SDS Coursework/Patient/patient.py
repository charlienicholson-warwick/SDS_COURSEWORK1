import tkinter as tk
import subprocess
import sys

#This code is very simliar to the other setup scripts admin.py and doctor.py, taking input from login.py creating a customised GUI to the required user and linking this script to all the needed patient functionality
def open_patient_info():
    print(f"Passing patient ID: {patient_id}") #debuggin'
    subprocess.Popen(["python", "patient_info.py", patient_id]) #used to show patients personal info as per brief

def open_patient_appointments():
    print(f"Passing patient ID: {patient_id} in THE OPEN_PATIENT_APPOINTMENTS") #debuggin'
    subprocess.Popen(["python", "patient_appointments.py", patient_id])  #used to show patient's current appointements and status therefore requires us to pass their ID as an argument

def open_create_appointment():
    subprocess.Popen(["python", "create_appointment.py", patient_id])


if len(sys.argv) > 1:
    patient_id = sys.argv[1]
else:
    print("Patient ID not provided.")
    sys.exit(1)

#-------------Copied From admin.py
#^^^^^ <<FORMATTING USED IN ALMOST EVERY SCRIPT WILL EXPLAIN FOR CPY FORMAT SO YOU DON'T FORGET HOW THIS WORKS WHEN YOU COME BACK LATER: >>
# sys.argv = Stores all command line arguments passed to a given script
# <<NOTES: sys.argv[1] DEFAULT: {SCRIPT NAME, SCRIPT PASSED DATA}>>
# sys.argv[1] Is the data passed to the script in this case the PATIENT passed from the login.py script
# len(sys.argv) > 1 This checks if more than one argument was passed if one or less was passed then only the script name was passed no ID therefore we don't know whos admin portal this is
# <<BASICALLY IF GREATER THAN ONE WE KNOW THAT IT HAS AN PATIENT ID WE NEED FOR ALL PROGRAM INSTANCES FOR CUSTOM PROGRAM RESPONSES>>


app = tk.Tk()
app.title("Patient Dashboard")

info_btn = tk.Button(app, text="View My Information", command=open_patient_info)
info_btn.pack()

appointments_btn = tk.Button(app, text="View My Appointments", command=open_patient_appointments)
appointments_btn.pack()

create_appointment_btn = tk.Button(app, text="Create New Appointment", command=open_create_appointment)
create_appointment_btn.pack()

#^ All default Top based .pack GUI sorting


app.mainloop()
