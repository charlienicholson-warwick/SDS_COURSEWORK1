import tkinter as tk
import csv

#This script is in a misleading location. This is actually a script intended to be run by the admin and the doctor
#Scripts function is to print a searchable "database" that can display the medical details for any desired patient
#As this is required by the brief to be executable by the Admin & Doctor having it in either directory felt wrong so the patient directory felt like an appropriate sacrifice
#It also allowed me to only worry about one set of relative pathing for credential files

#Length of this script is because it is kinda two scripts in one:
#A searching script for patient credentials <<CHECK/TODO: CAN WE USE PATIENT_INFO.PY CALL??>>
#A search script for appointments

def load_patients(): 
    with open('../Data/credentials/patient_credentials.txt', 'r') as file:
        reader = csv.reader(file)
        return {row[0]: row[3] for row in reader}  # Loads patient credentials and maps the patientID value to the full name value

def load_patient_appointments(patient_id):
    with open('../Data/appointments/appointments.txt', 'r') as file:
        reader = csv.reader(file)
        return [row for row in reader if row[0] == patient_id] # Returns the appointments for the patientID specified in the search query

def display_patient_info(patient_id):
    for widget in frame_patient_info.winfo_children():
        widget.destroy() # If you do a successive search you need to destroy the previous information [Everything is a widget...]

    # Display patient information (excluding username and password)
    with open('../Data/credentials/patient_credentials.txt', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == patient_id:
                info = f"ID: {row[0]}, Full Name: {row[3]}, Age: {row[5]}, Mobile: {row[6]}, Address: {row[7]}"
                tk.Label(frame_patient_info, text=info).pack()

    # Display patient appointments
    appointments = load_patient_appointments(patient_id)
    if appointments:
        for app in appointments:
            app_info = f"Condition: {app[2]}, Status: {app[3]}"
            tk.Label(frame_patient_info, text=app_info).pack()
            #basic appointment display
    else:
        tk.Label(frame_patient_info, text="No appointments found").pack()

def search_patient():
    patient_id = entry_search.get()
    display_patient_info(patient_id)

app = tk.Tk()
app.title("Patient Records")

patients = load_patients()

# Display all patients
frame_patients = tk.Frame(app)
frame_patients.pack(pady=10)

for id, name in patients.items():
    tk.Label(frame_patients, text=f"ID: {id}, Name: {name}").pack()

# Search functionality
frame_search = tk.Frame(app)
frame_search.pack(pady=10)

entry_search = tk.Entry(frame_search)
entry_search.pack(side=tk.LEFT) # NON DEFAULT .pack !!!! What a development!
search_button = tk.Button(frame_search, text="Search", command=search_patient)
search_button.pack(side=tk.LEFT)

# Patient information display
frame_patient_info = tk.Frame(app)
frame_patient_info.pack(pady=10)

app.mainloop()
