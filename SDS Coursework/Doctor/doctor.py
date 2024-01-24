import tkinter as tk
import subprocess # needed to execute other python scripts
import sys # needed to read the console input given from login.py
import os # Not sure this is needed (all relative pathing) best just to have it incase relative pathing breaks again :(

# This is effectivley the same as admin.py and doctor.py main role is to take the doctorID from the login script and create a doctor specific GUI
# Allowing all the functionality required for the doctor, by calling organisationally adjacent scrits

def open_patient_records():
    subprocess.Popen(["python", "patient_records.py"], cwd = "Patient") #Stored in the patient directory as used in admin as well therefore we need our current working directory to be the Patient directory

def open_display_appointments():
    subprocess.Popen(["python", "display_appointments.py", doctor_id], cwd = "Doctor") #also stored in /Doctor, we also need to pass the doctor_id to this script to get a custom output


if len(sys.argv) > 1: 
    doctor_id = sys.argv[1]
else:
    print("Doctor ID not provided.")
    sys.exit(1)
#------------------COMMENT FROM ADMIN.PY-------------------
#^^^^^ <<FORMATTING USED IN ALMOST EVERY SCRIPT WILL EXPLAIN FOR CPY FORMAT SO YOU DON'T FORGET HOW THIS WORKS WHEN YOU COME BACK LATER: >>
# sys.argv = Stores all command line arguments passed to a given script
# <<NOTES: sys.argv[1] DEFAULT: {SCRIPT NAME, SCRIPT PASSED DATA}>>
# sys.argv[1] Is the data passed to the script in this case the DoctorID passed from the login.py script
# len(sys.argv) > 1 This checks if more than one argument was passed if one or less was passed then only the script name was passed no ID therefore we don't know whos admin portal this is
# <<BASICALLY IF GREATER THAN ONE WE KNOW THAT IT HAS AN DOCTOR ID WE NEED FOR ALL PROGRAM INSTANCES FOR CUSTOM PROGRAM RESPONSES>>



app = tk.Tk()
app.title("Doctor Panel")

patient_records_btn = tk.Button(app, text="View Patient Records", command=open_patient_records)
patient_records_btn.pack()

appointments_btn = tk.Button(app, text="View Your Appointments", command=open_display_appointments)
appointments_btn.pack()

app.mainloop()
