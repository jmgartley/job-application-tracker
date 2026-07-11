applications = []

def add_application(company, role, status) -> None:
    applications.append({"company": company, "role": role, "status": status})

def print_applications():
    for app in applications:
        print(f"{app['company']} - {app['role']} - {app['status']}")

add_application("Google", "Software Engineer", "Applied")
add_application("Microsoft", "SWE Intern", "Applied")

print_applications()

