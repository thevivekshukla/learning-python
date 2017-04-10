from datetime import datetime as dt
import time


hosts = r"hosts"

website_list = ["www.facebook.com", "facebook.com"]
redirect = "127.0.0.1"


while True:

  if dt(dt.now().year, dt.now().month, dt.now().day, 13) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):

    with open(hosts, 'r+') as file:
      content = file.read()
      for website in website_list:
        if website in content:
          pass
        else:
          file.write(redirect +" "+ website +"\n")

  else:

    with open(hosts, 'r+') as file:
      content = file.readlines()
      file.seek(0)

      for line in content:
        if not any(website in line for website in website_list):
          file.write(line)

      file.truncate()


  time.sleep(5)
