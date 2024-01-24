import tkinter as tk
from tkinter import messagebox
import subprocess # Needed to call scripts in script
import csv # Data in credential file formatted as csv
import sys

def validate_login(username, password, role):
    credentials_path = f'Data/credentials/{role}_credentials.txt' # Broad relative path to any role_credential file
    with open(credentials_path, 'r') as file: # Open credential file
        reader = csv.reader(file) 
        for row in reader:
            if row[1] == username and row[2] == password: # Creds row[1] = uname & row[2] = pwd -> find a row where uname & pass of login = cred file
                return row[0]  # Return {role}ID for the logged in user
   

def open_patient_registration():
   subprocess.Popen(["python", "patient_registration.py"], cwd="Patient") # Runs the patient_registration script from /Patient


def on_login(): 
    role = role_var.get().lower() # Takes role value from selector <--*Note* please do not remove .lower as you named cred files as all lowercase
    username = username_entry.get() # Takes value in username .Entry widget
    password = password_entry.get() # Takes value in password .Entry widget 

    user_id = validate_login(username, password, role) # Calls the above function validate_login
    if user_id: # If a userID was returned we know login was successful
        app.destroy() # Close current window
        if role == "admin":
            subprocess.Popen(["python", "Admin/admin.py", user_id])             # vvvv
        elif role == "doctor":
            doctor_id = user_id
            subprocess.Popen(["python", "Doctor/doctor.py", doctor_id])
            # Above and below lines are effectivley the same, run the corresponding scripts from correct directory <--*Note* "python","path",ID We need ID to make sure the script opened is user specific for appointment display etc
        if role == "patient":
            patient_id = user_id
            subprocess.Popen(["python", "patient.py", patient_id], cwd="Patient") # ^^^^ <<WHY I HAVE TO USE CWD HERE AND NOT OTHERS, CANT GET THIS ONE TO WORK WITH RELATIVE PATHS, AM I STUPID?!??!>>
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.") #Login failed as no userID was returned by validate_login

app = tk.Tk() # Explicity starts a TK interpreter window to translate tkinter commands into <<CAN IMPLICTLY START BY CREATING WIDGET! ANY BENEFIT TO EXPLICIT CREATION??? BUG PREVENTION???>>

app.title("Login") # Top left app title

#.pack <-- *Note* geometry managment used to pack each widget into unique block in parent app
#.Entry <-- *Note* user input widget, takes a single line user inputted string <<Check: Is this also using default top ordering??? or would ordering be needed via grid method>>
            #{https://www.geeksforgeeks.org/python-tkinter-entry-widget/}

tk.Label(app, text="Username:").pack() # Packs username label widget with default top ordering
username_entry = tk.Entry(app) # Takes single line text string from the user using the Entry widget
username_entry.pack() # Displays the username entry prompt on screen using default ordering

tk.Label(app, text="Password:").pack()
password_entry = tk.Entry(app, show="*") # Same as above just show the entered characters as little asterix *
password_entry.pack()

role_var = tk.StringVar(app)
role_var.set("Patient")  # Default role selection value
role_options = tk.OptionMenu(app, role_var, "Admin", "Doctor", "Patient") # Option menu widget with role options included, selection stored in role_var
role_options.pack() # Displays on screen using default top ordering

login_button = tk.Button(app, text="Login", command=on_login) #button when pressed calls command this command is a function call to on_login
login_button.pack()

register_button = tk.Button(app, text="Register as New Patient", command=open_patient_registration) #button when pressed calls command this command is a function call to open_patient_registration
register_button.pack()

app.mainloop()
