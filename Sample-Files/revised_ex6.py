import datetime
import glob2

filenames = glob2.glob('file[1-3].txt')
contents = []

for filename in filenames:
  with open(filename, 'r') as file:
    contents.append(file.read())

new_filename = str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f"))+'.txt'

with open(new_filename, 'w') as file:
  for content in contents:
    file.write(content+"\n")