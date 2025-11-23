import connection
import csv
def menu():
    while True:
            print("\nYou are now in the bed management section.")
            print("1.Add New Bed")
            print("2.View Status")
            print("3.Assign Bed to Patient")
            print("4.Free a Bed")
            print("5.Export Bed data to CSV")
            print("6.GO BACK TO MAIN MENU")
            choice = input("Enter your choice (1-6): ")
            if choice == '1':
                new()
            elif choice == '2':
                view()
            elif choice == '3':
                assign()
            elif choice == '4':
                free()
            elif choice == '5':
                export()
            elif choice == '6':
                print("Going back to main menu...")
                return
            else:
                print("Retry, invalid choice.")
def new():
    bed_id = input("Enter ID: ")
    ward = input("Type (ICU/General/Private): ")
    status = "FREE"
    patient = None
    connecti = connection.get_connection()
    curs = connecti.cursor()   
    query = """
    INSERT INTO beds (bed_id, ward_type, status, current_patient_id)
    VALUES (%s, %s, %s, %s)
    """
    curs.execute(query, (bed_id, ward, status, patient))
    connecti.commit()
    print("Bed added successfully.")
    curs.close()
    connecti.close()
def view():
    print("\n--- BED STATUS ---")
    conn = connection.get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM beds")
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    conn.close()
def assign():
    print("\n--- ASSIGN BED ---")
    bed_id = input("Enter Bed ID to assign: ")
    patient_id = input("Enter Patient ID to assign to this bed: ")

    conn = connection.get_connection()
    cur = conn.cursor()

    # update bed status
    cur.execute("""
        UPDATE beds 
        SET status='OCCUPIED', current_patient_id=%s
        WHERE bed_id=%s
    """, (patient_id, bed_id))
    conn.commit()
    print("Bed assigned successfully.")
    cur.close()
    conn.close()
def free():
    print("\n--- FREE A BED ---")
    bed_id = input("Enter Bed ID to free: ")
    connectio = connection.get_connection()
    cur = connectio.cursor()
    cur.execute("""
        UPDATE beds 
        SET status='FREE', current_patient_id=NULL
        WHERE bed_id=%s
    """, (bed_id,))
    connection.commit()
    print("Bed is now free.")
    cur.close()
    connectio.close()
def export():
    connectio = connection.get_connection()
    curst = connectio.cursor()
    curst.execute("SELECT * FROM beds")
    rows = curst.fetchall()
    with open("beds.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print("Exported to beds.csv")
    curst.close()
    connection.close()