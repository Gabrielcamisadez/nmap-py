import os

host = "google.com"

response = os.system("ping -c 1 " + host)

#and then check the response...
if response == 0:
  print (host, 'is up!')
else:
  print (host, 'is down!')