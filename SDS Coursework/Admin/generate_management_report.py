import tkinter as tk
import csv #Creds and Appointments are stored in comma seperated variable files so import needed to handle this filetype
import os #Needed for / vs \ porting from linux to windows respectivley 
from collections import Counter # Used to count tuples of data assigning key-pair values to track specific data links in the report e.g. linking appointments per moth to doctorID's 
from datetime import datetime # Used to process the date and time from the date semgent of the apointments.txt

def load_doctors():
    doctor_path = os.path.join(os.path.dirname(__file__), '..', 'Data', 'credentials', 'doctor_credentials.txt') # Reads doctor creds file
    with open(doctor_path, 'r', newline='') as file:
        reader = csv.reader(file)
        return list(reader) # Return each line of this file

def load_appointments():
    appointments_path = os.path.join(os.path.dirname(__file__), '..', 'Data', 'appointments', 'appointments.txt')# Reads appointment file
    with open(appointments_path, 'r', newline='') as file:
        reader = csv.reader(file)
        return list(reader) # Return each line of this file

def generate_report_text():
    doctors = load_doctors() #loads the csv file into doctors
    appointments = load_appointments() #same for appointments

    #Calculate values for report *Note* --> appointment.txt = [UserID, Condition, Physical/Viral, Date, Requested/Approved, DoctorID]
    total_doctors = len(doctors) # Number of doctors is the length of the Doctor credential file
    patients_per_doctor = Counter(app[5] for app in appointments if app[4] == 'Approved') # Number of "Approved" appointments per doctor by checking appointments for DoctorID (DoctorID = [5]) <output is counter>
    appointments_per_month_doctor = Counter((datetime.strptime(app[3], "%d/%m/%y").strftime("%Y-%m"), app[5]) for app in appointments if app[4] == 'Approved') # date index is [3] split and divide by doctorID's where appointment is approved
    #https://www.programiz.com/python-programming/datetime/strftime
    #https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
    
    unique_patients_physical = len(set(app[0] for app in appointments if app[2].lower() == "physical")) #The number of UserID's in appointments where the Physical/Viral is physical
    unique_patients_viral = len(set(app[0] for app in appointments if app[2].lower() == "viral"))   #The number of UserID's in appointments where the Physical/Viral is viral


    #REPORT STRING CONCAT <-- STRING BUILDER
    report_output = "Management Report:\n"
    report_output += f"Total number of doctors: {total_doctors}\n"
    report_output += "Total number of patients per doctor:\n"
    for doctor_id, count in patients_per_doctor.items():
        report_output += f"  Doctor ID {doctor_id}: {count} patients\n"
    report_output += "Total number of appointments per month per doctor:\n"
    for (month, doctor_id), count in appointments_per_month_doctor.items():
        report_output += f"  Month {month}, Doctor ID {doctor_id}: {count} appointments\n"
    report_output += f"Total number of unique patients with physical illnesses: {unique_patients_physical}\n"
    report_output += f"Total number of unique patients with viral illnesses: {unique_patients_viral}\n"
    
    return report_output

def display_management_report():
    report = generate_report_text() #Generate the report text (Big string)
    text_area = tk.Text(app, wrap=tk.WORD, width=80, height=20)
    #https://www.tutorialspoint.com/python/tk_text.htm
    #<<TODO: JUST LEARNT ABOUT TEXT WIDGET MAYBE GO THROUGH PROGRAM AND ADD THESE IN IF YOU HAVE TIME!!>>
    text_area.pack(padx=10, pady=10)
    #^^Boilerplate
    text_area.insert(tk.END, report)
    text_area.config(state=tk.DISABLED)  # Make the text area read-only

app = tk.Tk()
app.title("Management Report")
display_management_report()
app.mainloop()


