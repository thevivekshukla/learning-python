emails = ["me@gmail.com", "you@gmail.com", "they@gmail.com", "asw@hotmail.com", "ss@outlook.com"]

print("Printing all emails")
for email in emails:
    print(email)

print("printing only gmail email")
for email in emails:
    if 'gmail' in email:
        print(email)
