from connection import get_connection
import patients
import beds
import drugs
def main():
    while True:
        print("\n====================================")
        print("      HOSPITAL MANAGEMENT SYSTEM")
        print("====================================")
        print("1. Patient Management")
        print("2. Bed Management")
        print("3. Drug Management")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            patients.menu()
        elif choice == '2':
            beds.menu()
        elif choice == '3':
            drugs.menu()
        else:
            print("Exiting")
            break
main()