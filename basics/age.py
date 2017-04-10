def foo(age):
    new_age = age + 50
    return new_age

age = float(input("Enter your age: "))

if age <= 100:
    print(foo(age))
else:
    print("how is that possible?")
