PatientAppointments = {
    1: ["Anas", "2023-10-01", "10:00"],2: ["Sara", "2023-10-02", "11:00"],
    3: ["Amal", "2023-10-03", "12:00"],4: ["Rami", "2023-10-04", "13:00"]
}

while True:
    print("\nPatient Appointment Management System")
    print("1.Add Appointment") 
    print("2.show Appointments")
    print("3.Delete Appointment")
    print("4.Exit")

    choice = input("Choose an option (1-4):")

    if choice == "1":
        name = input("Enter patient name: ")
        date = input("Enter appointment date (YYYY-MM-DD): ")
        time = input("Enter appointment time (HH:MM): ")

        NewKey = len(PatientAppointments) +1
        PatientAppointments[NewKey] = [name, date, time]
        print("Appointment added successfully!")

    elif choice == "2":
        if not PatientAppointments:
            print("No appointments found.")
        else:
            print("\nAll Appointments:")
            for key, value in PatientAppointments.items():
                print(f"{key}.{value[0]}, Date: {value[1]}, Time: {value[2]}")

    elif choice == "3":
            remove_key = int(input("Enter the appointment number to delete: "))
            if remove_key in PatientAppointments:
                PatientAppointments.pop(remove_key)
                print("Appointment deleted successfully!")
            else:
                print("No patient with that number.")

    elif choice == "4":
        print("Exiting the system successfully.")
        break

    else:
        print("Invalid choice. Please choose a valid option.")


        
 