import connection
import csv
def menu():
    while True:
            print("You are now in the drug management section.")
            print("1.Add Drug")
            print("2.View Drugs")
            print("3.Update Drug")
            print("4.Export Drugs data to csv or excel file")
            print("5.GO BACK TO MAIN MENU")
            choice = input("Enter your choice (1-5): ")
            if choice == '1':
                print("Fill the details of the new drug here.")
                new()
            elif choice == '2':
                print("Here is the list of all drugs.")
                view()
            elif choice == '3':
                print("Update drug details here.")
                update()
            elif choice == '4':
                print("Export drugs data to csv or excel file here.")
                export()
            elif choice == '5':
                print("Going back to the main menu.")
                return
            else:
                print("Invalid choice. Please try again.")
def new():
    name = input("Name:")
    type = input("Type:")
    stock = input("Quantity: ")
    price = input("Price: ")
    expiry = input("Expiry Date (YYYY-MM-DD): ")
    connect = connection.get_connection()
    cursor = connect.cursor()
    query = """
    INSERT INTO drugs (name, type, stock_qty, price, expiry_date)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (name, type, stock, price, expiry))
    connect.commit()
    print("Drug added successfully.")
    cursor.close()
    connect.close()
def view():
    conn=connection.get_connection()
    cur=conn.cursor()
    cur.execute("SELECT * FROM drugs")
    rows = cur.fetchall()   
    for i in rows:
        print(i)
    cur.close()
    conn.close()
def update():
    did = input("Enter ID: ")
    new_stock = input("New Stock (leave empty to skip): ")
    new_price = input("New Price (leave empty to skip): ")
    new_expiry = input("New Expiry Date (YYYY-MM-DD or empty): ")
    conne = connection.get_connection()
    curs = conne.cursor()
    if new_stock != "":
        curs.execute("UPDATE drugs SET stock_qty=%s WHERE drug_id=%s", (new_stock, did))
    if new_price != "":
        curs.execute("UPDATE drugs SET price=%s WHERE drug_id=%s", (new_price, did))
    if new_expiry != "":
        curs.execute("UPDATE drugs SET expiry_date=%s WHERE drug_id=%s", (new_expiry, did))
    conne.commit()
    print("Drug updated successfully.")
    curs.close()
    conne.close()
def export():
    print("\nExporting data to drugs.csv ...")
    connetion = connection.get_connection()
    cur = connetion.cursor()
    cur.execute("SELECT * FROM drugs")
    rows = cur.fetchall()
    with open("drugs.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print("Exported to drugs.csv")

    cur.close()
    connetion.close()