import datetime
import glob2

filenames = glob2.glob('file[1-3].txt')

with open(str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f"))+'.txt', 'w') as file:
  for filename in filenames:
    with open(filename, 'r') as read_file:
      file.write(read_file.read()+'\n')