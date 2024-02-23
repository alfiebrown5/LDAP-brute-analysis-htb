# LDAP-brute-analysis-htb
Python LDAP fuzzer and LDAP Brute Force to help find attributes and brute force - made for HTB's Analysis Box.

To find the user flag for Hack the Box's analysis, I had to create some scripts myself. I thought I'd share here in case anyone else needs some help finding the user flag. This flag was tricky and these scripts don't reveal the entire answer to the user flag - you'll need to play about with the script a bit to discover it for yourself! 

"attribute-fuzz.py" makes HTTP GET requests to the web app hosted on the box to find Active Directory attributes through an LDAP injection vulnerabilty. 

"ldap-brute-force.py" then also leverages this vulnerability with the unusual attribute uncovered by "attribute-fuzz.py" to brute force the string attatched to this attribute. 

References:
Scripts tweaked from a script I found on hacktricks:
https://book.hacktricks.xyz/pentesting-web/ldap-injection 
