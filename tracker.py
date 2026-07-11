import json

def add_application(company, role, status) -> None:
    applications.append({"company": company, "role": role, "status": status})

def print_applications():
    for app in applications:
        print(f"{app['company']} - {app['role']} - {app['status']}")

def save_applications():
    with open("applications.json", "w") as file:
        json.dump(applications, file)

def load_applications():
    try:
        with open("applications.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

applications = load_applications()

while(True):
    print("\n1. Add Application")
    print("2. View Applications")
    print("3. Quit")
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
        break
    else:
        print("Invalid Choice, Try Again")

#add_application("Google", "Software Engineer", "Applied")
#add_application("Microsoft", "SWE Intern", "Applied")

print_applications()

