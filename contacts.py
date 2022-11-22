contacts = {
    "number":4,
    "students":
        [
            {"name":"Astrid Keonna", "email":"astrid@example.com"},
            {"name":"Harry Potter", "email":"harry@example.com"},
            {"name":"Joy Keonna", "email":"joy@example.com"},
            {"name":"yadah Keonna", "email":"yadah@example.com"},
        ]
}

for student in contacts["students"]:
    print(student["email"])