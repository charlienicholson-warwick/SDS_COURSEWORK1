import tkinter as tk
import tkinter.simpledialog as sd
import csv # Needed to read the CSV creds file
import os # Needed to fetch the filename path, <<DIFFERENT OS ON TEST PC????? DOES THIS RUN DIFFERENT ON WINDOWS 10 VS LINUX DISTRO WITHOUT THIS IMPORT?>> os ensures portability across operating systems


credentials_path = os.path.join(os.path.dirname(__file__), '..', 'Data', 'credentials', 'patient_credentials.txt') # Fetches the data from /home/user/project/Data/credentials/patient_credentials.txt regardless of running OS
treated_path = os.path.join(os.path.dirname(__file__), '..', 'Data', 'credentials', 'treated_patients.txt') #Fetches the data from /home/user/project/Data/credentials/treated_patients.txt
# ^^^ Effectivley boilerplate code
# https://docs.python.org/3/library/os.path.html

def move_to_treated(patient_id): # Takes a given patientID and moves it to the treated patient file and then removes the data from the patient creds
    with open(credentials_path, 'r', newline='') as infile, open(treated_path, 'a', newline='') as outfile:
        reader = csv.reader(infile) # Reads the creds file as infile and writes to the treated file as outfile
        writer = csv.writer(outfile) 
        lines = [row for row in reader if row[0] == patient_id] # the line is the row where the PatientID we want is the PatientID on the line as PatientID is position[0] in the patient_credentials
        for line in lines:
            writer.writerow(line) # write this line to the treated patient file

def remove_patient(patient_id): # Removes the patientID from the credentials file as to not have shared details between the treated and credentials file
    lines = [] # we are writing a blank to this line as we will fill this with all the values we dont want to delete
    with open(credentials_path, 'r', newline='') as file: 
        reader = csv.reader(file)
        lines = [row for row in reader if row[0] != patient_id] #Read creds file and set lines to the rows where the ID is not, every ID that we don't want to delete

    with open(credentials_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lines) #Now we re-write to the file the lines value which is basically just all the values that we dont wan't to delete <<NOT DIRECT DELETION JUST OVERRIDE BY PRINTING OVER WITH OTHER VALS>>
        #<<SKETCHY METHOD NEEDS ERROR CHECKING WHAT IF FORMATTING WIERD, WHAT IF DELETION IS LAST LINE ON CREDS FILE WHAT IF BLANK LINE ON FILE ETC!!>>

def discharge_patient():
    patient_id = sd.askstring("Discharge Patient", "Enter Patient ID:") #tkinter dialog askstring to get patientID
    if patient_id:
        move_to_treated(patient_id)  # Move patient to treated_patients.txt before deleting
        remove_patient(patient_id) # Remove patient from patient_credentials.txt
        tk.messagebox.showinfo("Success", "Patient discharged and moved to treated patients successfully.") #message prompt, defualt windows styling
    else:
        tk.messagebox.showinfo("Cancelled", "Operation cancelled.")
        # https://docs.python.org/3/library/tkinter.messagebox.html

app = tk.Tk()
app.withdraw()

discharge_patient() # Calls discharge_patient <<THIS SCRIPTS ONLY JOB MAYBE REWRITE TO RUN IN MAIN INSTEAD??>>

