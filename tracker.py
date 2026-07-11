applications = []

def add_application(company, role, status) -> None:
    applications.append({"company": company, "role": role, "status": status})

add_application("Google", "Software Engineer", "Applied")
add_application("Microsoft", "SWE Intern", "Applied")
print(applications)

