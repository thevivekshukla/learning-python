temperatures = [10, -20, -289, 100]

def convert(temperatures):
  with open("fahreinheit.txt", "a+") as file:
    for c in temperatures:
      if c > -273.15:
        f = c*9/5+32
        file.write(str(f)+"\n")


convert(temperatures)