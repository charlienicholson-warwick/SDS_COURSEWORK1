import tkinter as tk 
import csv #csv for patient creds

def load_all_applications():
    with open('../Data/credentials/patient_credentials.txt', 'r') as file: # PLEASE CHECK IF THIS WILL WORK ON LINUX & WINDOWS AS LINUX HAS / AND WINDOWS HAS \ SO CHECK PRE SUBMISSION!!!!!
        return list(csv.reader(file)) #No need to error check as patient creds will always be a present file in the Data repo

def update_credentials(updated_applications): 
    all_applications = load_all_applications() # Load all patient_credentials.txt csv value
    for updated_app in updated_applications: 
        for i, app in enumerate(all_applications):
            if app[0] == updated_app[0]:  # Match by patient ID
                all_applications[i] = updated_app  # Update the entire record
                break
    with open('../Data/credentials/patient_credentials.txt', 'w', newline='') as file: # Write to the patient credentials 
        writer = csv.writer(file) 
        writer.writerows(all_applications)# Write all the updated records back to file as per [all_applications[i] = updated_app]
        #https://docs.python.org/3/library/csv.html

def approve_application(patient_id):
    applications = load_all_applications()  # Load all applications
    updated_applications = [] # Set blank for now as will be used to store the new application values
    for app in applications:
        if app[0] == patient_id and app[4] == 'Pending':
            app[4] = 'Registered' #Change pending application to approved
        updated_applications.append(app)
    update_credentials(updated_applications)  # Pass the updated list to update credentials
    display_pending_applications() # <<RE-CALL THE PENDING APPLICATIONS AS SO WHEN IT IS APPROVED IT DISSAPEARS FROM THE LIST>>

def decline_application(patient_id):
    applications = load_pending_applications() # Read all pending applications
    applications = [app for app in applications if app[0] != patient_id] # Applications are now set to all pending applications except the one passed to this function
    update_credentials(applications) # Update the credentials therefore removing the one that was passed to this function
    display_pending_applications() # Re-display the pending applications thereby removing the declined application

def display_pending_applications():
    for widget in frame_applications.winfo_children():
        widget.destroy() # Clears all child widgets of the frame_applications as to refresh the list when re-called
        #https://www.tutorialspoint.com/getting-every-child-widget-of-a-tkinter-window

    applications = load_all_applications()
    pending_applications = [app for app in applications if app[4] == 'Pending']  # Filter for pending applications

    for app in pending_applications:
        patient_info = ', '.join(app[1:4]) + f" (ID: {app[0]})"
        approve_btn = tk.Button(frame_applications, text="Approve", command=lambda id=app[0]: approve_application(id)) #buttons for interaction call function and pass the id we want to interact with
        decline_btn = tk.Button(frame_applications, text="Decline", command=lambda id=app[0]: decline_application(id))
        tk.Label(frame_applications, text=patient_info).pack()
        approve_btn.pack()
        decline_btn.pack()
        
app = tk.Tk()
app.title("Manage Applications")

frame_applications = tk.Frame(app)
frame_applications.pack(pady=10)

display_pending_applications()

app.mainloop()
