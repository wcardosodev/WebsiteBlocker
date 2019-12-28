import platform
import time
from datetime import datetime as dt

op_sys = platform.system().title()
hosts_path = ""
redirect_path = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]
start_hour = 9
start_minute = 0
end_hour = 17
end_minute = 0

def getHostsPath():
    if op_sys == "Windows":
        hosts_path = r"C:\Windows\System32\drivers\etc\hosts"    
    elif op_sys == "Darwin" or op_sys == "Linux":
        hosts_path = "/etc/hosts"

hosts_temp = r"C:\Users\willa\Documents\GitHub\WebsiteBlocker\hosts"

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, start_hour, start_minute) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,
     end_hour, end_minute):
        print("Working Hours")
        with open(hosts_temp, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(f"# {redirect_path} {website}\n")
    else:
        print("Not Working Hours")
        with open(hosts_temp, "r+") as file:
            # read lines, once you have read the lines the cursor ends up at the end of the file
            content = file.readlines()
            # resets the cursor to the first line
            file.seek(0)
            # for each line in the text file
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
    time.sleep(5)