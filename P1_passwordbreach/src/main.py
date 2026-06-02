from api import checkforbreach
from hashing import hashing 

import getpass
#adding another security feature besides hashing and splitting into prefix/suffix


password = getpass.getpass("Enter your password: ")

hashed_password = hashing(password)

print(f"SHA-1 Hash: {hashed_password}")
print("Checking if your password has been breached...")
result = checkforbreach(hashed_password[1], hashed_password[2])
print(result)