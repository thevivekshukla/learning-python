import datetime

text = []

for i in range(1, 4):
  with open("file"+str(i)+".txt", "r") as file:
    text.append(file.read())


filename = str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%s-%f"))+".txt"

with open(filename, "w") as file:
  for i in text:
    file.write(i+"\n")