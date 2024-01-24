import tkinter as tk
import csv # for cred formatting
import os # cross OS compatability

treated_patients_path = os.path.join(os.path.dirname(__file__), '..', 'Data', 'credentials', 'treated_patients.txt') #see discharge_patient.py for more info

def display_treated_patients():
    with open(treated_patients_path, 'r', newline='') as file: #COULD DO ERROR HANDLING AND CHECK FOR FILES EXISTANCE BUT THE FILE WILL ALWAYS EXIST AS PART OF Data SEGMENT OF PROGRAM
        reader = csv.reader(file)
        for row in reader:
            patient_info = f"ID: {row[0]}, Username: {row[1]}, Full Name: {row[3]}, Status: {row[4]}, Age: {row[5]}, Mobile: {row[6]}, Address: {row[7]}" # Formatting data taken from our csv treated patients file
            #*FOR MARKER*: In above line, I have intentionally not printed the password, even though this is stored as not sure of ethics etc
            label = tk.Label(app, text=patient_info) #label widget that displays the conents of the patient_info formatting
            #https://www.tutorialspoint.com/python/tk_label.htm
            label.pack()

app = tk.Tk()
app.title("Treated Patients")
display_treated_patients() # <<COULD RUN THIS IN MAIN ANY PERFORMANCE BENEFIT?>>
app.mainloop()
