import time
from datetime import datetime as dt
# we are importing the datetime module to tell the program the time from which the scheduler needs to start.


hosts_temp=r"hosts"
# its a good practice to save the folder in a temporary drive. so that first test it on that before implementing the actual code.
hosts_path=r"C:\Windows\System32\drivers\etc\hosts" # this is the actual path where the host file is saved.
# make sure to open the actual host file to check what all sites actually exist.
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","twitter.com","www.twitter.com"]

# setting up an infinite loop inside the program.
# setting up the time, when you want to block the websites.
# opening the host file in read and write mode and adding the websites name if it is not present.
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working hours...")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)
