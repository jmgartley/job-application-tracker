import json

def add_application(company, role, status) -> None:
    applications.append({"company": company, "role": role, "status": status})

def print_applications():
    for index, app in enumerate(applications):
        print(f"{index+1}. {app['company']} - {app['role']} - {app['status']}")

def save_applications():
    with open("applications.json", "w") as file:
        json.dump(applications, file)

def load_applications():
    try:
        with open("applications.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def update_status(index, status):
    if 0 <= index < len(applications):
        applications[index]["status"] = status
        save_applications()
    else:
        print("Invalid Application Number")

def delete_application(index):
    if 0 <= index < len(applications):
        removed = applications.pop(index)
        print(f"Removed {removed['company']} - {removed['role']}")
        save_applications()
    else:
        print("Invalid Application Number")

applications = load_applications()

while(True):
    print("\n1. Add Application")
    print("2. View Applications")
    print("3. Update Status")
    print("4. Delete Application")
    print("5. Quit")
    choice = input("Choose an Option: ")

    if choice == '1':
        company = input("Company: ")
        role = input("Role: ")
        status = input("Status: ")
        add_application(company, role, status)
        save_applications()
    elif choice == '2':
        print_applications()
    elif choice == '3':
        print_applications()
        num = input("Which application would you like to update? ")
        new_status = input("New Status: ")
        update_status(int(num) - 1, new_status)
    elif choice == '4':
        print_applications()
        num = input("Which application would you like to delete? ")
        confirm = input(f"Are you sure you want to delete #{num}? (y/n): ")
        if confirm.lower() == "y":
            delete_application(int(num) - 1)
        else:
            print("Action Cancelled.")
    elif choice == '5':
        break
    else:
        print("Invalid Choice, Try Again")

    input("Press Enter to Continue...")
#add_application("Google", "Software Engineer", "Applied")
#add_application("Microsoft", "SWE Intern", "Applied")

#print_applications()

