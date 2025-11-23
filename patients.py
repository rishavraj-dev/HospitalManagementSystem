import connection
import csv
def menu():
    while True:
            print("You are now in the patient management section.")
            print("1.Add Patient")
            print("2.View Patients")
            print("3.Update Patient")
            print("4.Export Patients data to csv or excel file")
            print("5.GO BACK TO MAIN MENU")
            choice = input("Enter your choice (1-5): ")
            if choice == '1':
                print("Fill the details of the new patients here.")
                new()
            elif choice == '2':
                print("Here is the list of all patients.")
                view()
            elif choice == '3':
                print("Update patient details here.")
                update()
            elif choice == '4':
                print("Export patients data to csv or excel file here.")
                export()
            elif choice == '5':
                print("Going back to the main menu.")
                return
            else:
                print("Invalid choice. Please try again.")
def new():
    name = input("Enter name:")
    age = input("Enter age:")
    gender = input("Enter gender(M/F/O):")
    phone = input("Enter phone number:")
    address = input("Enter address:")
    disease = input("Enter disease:")
    print("Enter admit date in format YYYY-MM-DD (example: 2025-11-23)")
    admit = input("Admit date: ")
    discharge = None
    conn=connection.get_connection()
    cursor=conn.cursor()
    query = """
    INSERT INTO patients (name, age, gender, phone, address, disease, admit_date)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """
    cursor.execute(query, (name, age, gender, phone, address, disease, admit))
    conn.commit()
    print("Patient added successfully.")
    cursor.close()
    conn.close()
def view():
    print("\n--- PATIENT LIST ---")
    conn = connection.get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM patients")
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    conn.close()
def update():
    print("\n--- UPDATE PATIENT ---")
    pid = input("Enter patient ID: ")
    new_phone = input("New phone (leave empty to skip): ")
    new_address = input("New address (leave empty to skip): ")
    new_disease = input("New disease (leave empty to skip): ")
    new_discharge = input("New discharge date (YYYY-MM-DD or empty): ")
    conn = connection.get_connection()
    cur = conn.cursor()
    if new_phone != "":
        cur.execute("UPDATE patients SET phone=%s WHERE patient_id=%s", (new_phone, pid))
    if new_address != "":
        cur.execute("UPDATE patients SET address=%s WHERE patient_id=%s", (new_address, pid))
    if new_disease != "":
        cur.execute("UPDATE patients SET disease=%s WHERE patient_id=%s", (new_disease, pid))
    if new_discharge != "":
        cur.execute("UPDATE patients SET discharge_date=%s WHERE patient_id=%s", (new_discharge, pid))
    conn.commit()
    print("Patient updated.")
    cur.close()
    conn.close()
def export():
    print("\nExporting data to patients.csv ...")
    conn = connection.get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM patients")
    rows = cur.fetchall()
    with open("patients.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print("Exported to patients.csv")
    cur.close()
    conn.close()