def c_to_f(c):
    if c < -273.15:
        return "What!"
    else:
        f = c*9/5+32
        return f

c = float(input("Enter the temperature in celsius: "))
print(c_to_f(c))

temperature = [10, -20, -289, 100]

for t in temperature:
    print(c_to_f(t))
