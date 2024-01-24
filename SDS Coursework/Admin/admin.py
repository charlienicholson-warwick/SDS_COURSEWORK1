import tkinter as tk
import subprocess #needed to execute other scripts
import sys

#main job of this script is to print options using button widgets
#link buttons to script executions passing any needed information

#cwd= "admin" needed to ensure that all relative paths are consistant for the program testers pc
def open_manage_doctors():
    subprocess.Popen(["python", "manage_doctors.py"], cwd="admin")
    # *Note* <-- this script allow the admin to manage [delete and update] doctors

def open_manage_appointments():
    subprocess.Popen(["python", "manage_appointments.py"], cwd="admin")
    # *Note* <-- this script allows the admin to approve and assign doctors to appointments

def open_manage_applications():
    subprocess.Popen(["python", "manage_applications.py"], cwd="admin")
    # *Note* <-- this script allows the admin to approve or delcine patient applications
    
def open_patient_records():
    subprocess.Popen(["python", "../Patient/patient_records.py"], cwd="admin") #<<CAN'T SEEM TO USE cwd=Patient AND THEN JUST USE patient_records.py DIRECTLY!!, HAVE TO USE "admin" FOR RELATIVE?>>
    # *Note* <-- this script allows the admin to open patient records
    # <<THIS IS STORED IN PATIENT AS THIS SCRIPT WILL ALSO BE CALLED IN DOCTOR AS BOTH NEED TO ACCESS PATIENT RECORDS AS PER BRIEF>>

def open_discharge_patient():
    subprocess.Popen(["python", "discharge_patient.py"], cwd="admin")
    # *Note* <-- this script allows the admin discharge patients and save the patients creds to treated patient file

def open_display_treated():
    subprocess.Popen(["python", "display_treated.py"], cwd="admin")
    # *Note* <-- this script allows the admin to show all the treated patients
    
def generate_report():
    subprocess.Popen(["python", "generate_management_report.py"], cwd="admin")
    # *Note* <-- this script allows the admin to generate a management report
    # <<PART OF THE ADDED FUNCTIONALITY, CHECK DATA HERE AS SINCE CHANGED APPLICATION FORMATTING!!>>

def update_admin():
    subprocess.Popen(["python", "update_admin.py"], cwd="admin")
    # *Note* <-- this script allows the admin to update thier credentials
    # <<ADDED FUNCTIONALITY, WHY DOES ADMIN EVEN NEED AN ADDRESS??? CAN'T IT BE SUPERUSER LIKE ROOT? EMAIL PROF. ABOUT BRIEF ADMIN MAY NOT NEED SPECIFIC PERSONAL DETAILS.>>
    
admin_id = sys.argv[1] if len(sys.argv) > 1 else "Unknown"
#^^^^^ <<FORMATTING USED IN ALMOST EVERY SCRIPT WILL EXPLAIN FOR CPY FORMAT SO YOU DON'T FORGET HOW THIS WORKS WHEN YOU COME BACK LATER: >>
# sys.argv = Stores all command line arguments passed to a given script
# <<NOTES: sys.argv[1] DEFAULT: {SCRIPT NAME, SCRIPT PASSED DATA}>>
# sys.argv[1] Is the data passed to the script in this case the AdminID passed from the login.py script
# len(sys.argv) > 1 This checks if more than one argument was passed if one or less was passed then only the script name was passed no ID therefore we don't know whos admin portal this is
# <<BASICALLY IF GREATER THAN ONE WE KNOW THAT IT HAS AN ADMIN ID WE NEED FOR ALL PROGRAM INSTANCES FOR CUSTOM PROGRAM RESPONSES>>

app = tk.Tk()
app.title(f"Admin Panel - ID: {admin_id}")


#vvv Basically all default top sorted button widgets used to call the functions above [THE SAME FUNCTIONALITY AS login.py SO CHECK FOR MORE INFO ON WIDGETS]
#<<MAYBE COLOUR BUTTONS??>>
#<<WOULD THIS SCRIPT BE MORE LIGHTWEIGHT SHOULD I SPLIT FUNCTIONS INTO TWO PROGRAMS: ID SPECIFIC AND ADMIN GENERAL FUNCTIONS???>>
manage_doctors_btn = tk.Button(app, text="Manage Doctors", command=open_manage_doctors)
manage_doctors_btn.pack()

manage_appointments_btn = tk.Button(app, text="Manage Appointments", command=open_manage_appointments)
manage_appointments_btn.pack()

manage_applications_btn = tk.Button(app, text="Manage Applications", command=open_manage_applications)
manage_applications_btn.pack()

patient_records_btn = tk.Button(app, text="View Patient Records", command=open_patient_records)
patient_records_btn.pack()

discharge_patient_btn = tk.Button(app, text="Discharge Patient", command=open_discharge_patient)
discharge_patient_btn.pack()

display_treated_btn = tk.Button(app, text="Display Treated Patients", command=open_display_treated)
display_treated_btn.pack()

display_treated_btn = tk.Button(app, text="Generate Management Report", command=generate_report)
display_treated_btn.pack()

display_treated_btn = tk.Button(app, text="Update Admin", command=update_admin)
display_treated_btn.pack()

app.mainloop()
