#import requests
import hashlib 
#Secure Hash Algorithm 1 (SHA-1) to hash the password to not expose it
#Website API does not accept raw passwords, to locally hashing is needed

def hashing(password):
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    #encode converts string into bytes, hexdigest into readable hex string, upper to match API format (all uppercase)
    prefix, suffix = sha1[:5], sha1[5:]
    #splitting hash into 2 parts for security reasons
    return sha1, prefix, suffix

password = input("Enter your password: ")
hashed_password = hashing(password)
print(f"SHA-1 Hash: {hashed_password}")
print("Checking if your password has been breached...")